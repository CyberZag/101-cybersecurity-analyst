"""Offline, evidence-first email triage. Python 3.10+; no network calls."""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
from email import policy
from email.parser import BytesParser
from email.utils import getaddresses
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

MAX_BYTES = 5 * 1024 * 1024
URL_RE = re.compile(r"https?://[^\s<>\"']+", re.I)
REVIEW_EXTENSIONS = {'.exe', '.js', '.vbs', '.scr', '.hta', '.ps1', '.lnk', '.iso', '.img', '.docm', '.xlsm'}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def defang(value: str) -> str:
    return value.replace('https://', 'hxxps://').replace('http://', 'hxxp://').replace('.', '[.]')


def domain(address: str) -> str:
    return address.rsplit('@', 1)[-1].lower().rstrip('.') if '@' in address else ''


def host(url: str) -> str:
    try:
        return (urlsplit(url).hostname or '').lower().rstrip('.')
    except ValueError:
        return ''


class Links(HTMLParser):
    """Extract anchors without loading or rendering message HTML."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.anchors = []
        self.active = None

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'a':
            self.active = [dict(attrs).get('href', ''), '']

    def handle_data(self, data):
        if self.active is not None:
            self.active[1] += data

    def handle_endtag(self, tag):
        if tag.lower() == 'a' and self.active is not None:
            self.anchors.append(tuple(self.active))
            self.active = None


def analyze(raw: bytes, name: str = 'message.eml') -> dict:
    if len(raw) > MAX_BYTES:
        raise ValueError('Message exceeds the 5 MiB analysis limit')
    msg = BytesParser(policy=policy.default).parsebytes(raw)
    if not list(msg.keys()):
        raise ValueError('No email headers found')
    findings = []

    def finding(rule, reason, evidence):
        findings.append({'rule': rule, 'reason': reason, 'evidence': evidence})

    from_values = [str(x) for x in msg.get_all('From', [])]
    senders = getaddresses(from_values)
    reply = getaddresses([str(x) for x in msg.get_all('Reply-To', [])])
    if len(from_values) != 1 or len(senders) != 1 or not domain(senders[0][1]):
        finding('HEADER_AMBIGUITY', 'Missing, duplicate, or ambiguous From identity requires review.', from_values)
    sender_domains = {domain(a) for _, a in senders if domain(a)}
    reply_domains = {domain(a) for _, a in reply if domain(a)}
    if sender_domains and reply_domains and not reply_domains.issubset(sender_domains):
        finding('REPLY_DOMAIN_DIFFERS', 'Reply-To domain differs from From; legitimate workflows can do this.',
                {'from_domains': sorted(sender_domains), 'reply_domains': sorted(reply_domains)})

    # These are statements inside the file, never independently verified auth results.
    auth_claims = [str(x) for x in msg.get_all('Authentication-Results', [])]
    if any(re.search(r'\b(?:spf|dkim|dmarc)\s*=\s*(?:fail|softfail)\b', x, re.I) for x in auth_claims):
        finding('REPORTED_AUTH_FAILURE', 'Unverified header reports an authentication failure; confirm at the receiving gateway.', auth_claims)

    urls, attachments, parser_defects = set(), [], []
    text_bodies = []
    for part in msg.walk():
        parser_defects.extend(type(d).__name__ for d in part.defects)
        # Never descend into an attached email as if it were the outer message.
        # walk still visits its children; only top-level text parts are handled below.
        if part.is_multipart():
            continue
        payload = part.get_payload(decode=True) or b''
        filename = part.get_filename()
        disposition = part.get_content_disposition()
        if filename or disposition == 'attachment':
            filename = str(filename or '(unnamed attachment)')
            suffix = Path(filename.replace('\\', '/')).suffix.lower()
            attachments.append({'filename': filename, 'bytes': len(payload), 'sha256': sha256(payload),
                                'content_type': part.get_content_type()})
            if suffix in REVIEW_EXTENSIONS:
                finding('REVIEW_ATTACHMENT_TYPE', 'Attachment type can carry active content; bytes were hashed, never executed.', filename)

    # Recursion stops at attachments, including message/rfc822 containers.
    def body_parts(part):
        if part.get_filename() or part.get_content_disposition() == 'attachment' or part.get_content_type() == 'message/rfc822':
            return
        if part.is_multipart():
            for child in part.iter_parts():
                yield from body_parts(child)
        elif part.get_content_type() in ('text/plain', 'text/html'):
            yield part

    for part in body_parts(msg):
        payload = part.get_payload(decode=True) or b''
        try:
            body = payload.decode(part.get_content_charset() or 'utf-8', errors='replace')
        except LookupError:
            body = payload.decode('utf-8', errors='replace')
            parser_defects.append('UnknownCharset')
        text_bodies.append(body)
        urls.update(u.rstrip('.,);]') for u in URL_RE.findall(body))
        if part.get_content_type() == 'text/html':
            parser = Links()
            parser.feed(body)
            for target, label in parser.anchors:
                if target.lower().startswith(('https://', 'http://')):
                    urls.add(target)
                    label_host = host(label.strip())
                    if label_host and host(target) and label_host != host(target):
                        finding('LINK_LABEL_MISMATCH', 'Visible URL and destination host differ; redirects can also cause this.',
                                {'label': label.strip(), 'destination': target})
    for url in sorted(urls):
        try:
            parsed = urlsplit(url)
        except ValueError:
            finding('MALFORMED_URL', 'URL could not be parsed.', url)
            continue
        if parsed.username is not None:
            finding('URL_USERINFO', 'Text before @ is userinfo, not the destination host.', url)
    if parser_defects:
        finding('PARSER_DEFECT', 'Parsing was imperfect; inspect the source and treat extraction as incomplete.', sorted(set(parser_defects)))
    # De-duplicate findings without suppressing distinct evidence.
    findings = list({json.dumps(f, sort_keys=True): f for f in findings}.values())
    return {
        'schema_version': 1, 'file': name, 'source_sha256': sha256(raw), 'source_bytes': len(raw),
        'subject': str(msg.get('Subject', '')), 'from': from_values,
        'reply_to': [str(x) for x in msg.get_all('Reply-To', [])],
        'authentication_header_claims': auth_claims,
        'authentication_verified': False,
        'urls': [{'original': u, 'defanged': defang(u), 'host': host(u)} for u in sorted(urls)],
        'attachments': attachments, 'findings': findings,
        'disposition': 'review_required' if findings else 'no_rule_match',
        'limitations': ['No-rule-match does not mean safe.', 'No URLs, DNS, reputation services, or attachments were opened.',
                       'Header claims are untrusted until corroborated by trusted gateway evidence.',
                       'Exact host comparisons do not implement organizational-domain or DMARC alignment.',
                       'No archive expansion, OCR, JavaScript, DKIM validation, or nested-message investigation.',
                       'Attached message containers need separate analysis; leaf attachments are inventoried.'],
    }


def render_report(cases: list[dict]) -> str:
    def e(value):
        return html.escape(str(value), quote=True)
    cards = []
    for c in cases:
        findings = ''.join('<li><strong>' + e(f['rule']) + '</strong>: ' + e(f['reason']) +
                           '<pre>' + e(defang(json.dumps(f['evidence'], ensure_ascii=False, indent=2))) + '</pre></li>' for f in c['findings'])
        urls = ''.join('<li><code>' + e(u['defanged']) + '</code></li>' for u in c['urls']) or '<li>None extracted</li>'
        attachments = ''.join('<li>' + e(a['filename']) + ' — ' + str(a['bytes']) + ' bytes<pre>' + e(a['sha256']) + '</pre></li>' for a in c['attachments']) or '<li>None inventoried</li>'
        cards.append('<article><h2>' + e(c['file']) + '</h2><p class="badge">' + e(c['disposition']) +
                     '</p><p>' + e(c['subject']) + '</p><p>Source SHA-256</p><pre>' + e(c['source_sha256']) +
                     '</pre><h3>Evidence to review</h3><ul>' + (findings or '<li>No rule matched. This is not a safe verdict.</li>') +
                     '</ul><h3>Defanged URLs</h3><ul>' + urls + '</ul><h3>Attachments</h3><ul>' + attachments + '</ul></article>')
    return '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'">
<title>Phishing evidence lab</title><style>body{background:#101925;color:#e8eef5;font:16px/1.6 system-ui;margin:0}main{max-width:1050px;margin:auto;padding:40px 24px}h1{font-size:36px;line-height:1.2}h2{color:#76d7cb}article{background:#1b2939;border:1px solid #34495f;border-radius:12px;padding:24px;margin:24px 0}pre,code{white-space:pre-wrap;overflow-wrap:anywhere;font-size:13px}pre{background:#101925;padding:12px;border-radius:6px}.badge{color:#ffd18a;font-weight:bold}li{margin:12px 0}.sub{color:#b9c9da}</style><main>
<p class="sub">SOC PORTFOLIO · SYNTHETIC EMAILS · OFFLINE ANALYSIS</p><h1>Phishing evidence lab</h1>
<p>Observations first. Analyst verdict second.</p><p class="sub">No links were visited or attachments executed. Authentication headers are unverified claims. No rule match does not establish safety.</p>''' + ''.join(cards) + '</main></html>'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('inputs', nargs='+', type=Path)
    parser.add_argument('--out', type=Path, default=Path('reports'))
    args = parser.parse_args()
    files = sorted({p for source in args.inputs for p in (source.glob('*.eml') if source.is_dir() else [source])})
    if not files:
        parser.error('No .eml inputs found')
    cases, errors = [], []
    for path in files:
        try:
            if path.stat().st_size > MAX_BYTES:
                raise ValueError('Message exceeds the 5 MiB analysis limit')
            cases.append(analyze(path.read_bytes(), path.name))
        except (OSError, ValueError, RecursionError) as exc:
            errors.append({'file': path.name, 'error': str(exc)})
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / 'findings.json').write_text(json.dumps({'cases': cases, 'errors': errors}, indent=2, ensure_ascii=False), encoding='utf-8')
    report = render_report(cases)
    if errors:
        report = report.replace('<h1>', '<p class="badge">PARTIAL RUN: some inputs failed. See findings.json errors.</p><h1>', 1)
    (args.out / 'report.html').write_text(report, encoding='utf-8')
    print(f'Analyzed {len(cases)} messages; {sum(bool(c["findings"]) for c in cases)} require review; {len(errors)} errors')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
