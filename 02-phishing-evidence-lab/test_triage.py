import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from email.message import EmailMessage
from pathlib import Path
from unittest.mock import patch

from triage import analyze, render_report, MAX_BYTES
from make_samples import generate, message


def rules(case):
    return {f['rule'] for f in case['findings']}


class EvidenceTests(unittest.TestCase):
    def test_routine_is_not_safe_verdict(self):
        m = message('Routine'); m.set_content('hello')
        c = analyze(m.as_bytes())
        self.assertEqual(c['disposition'], 'no_rule_match')
        self.assertFalse(c['authentication_verified'])

    def test_source_hash_matches_original_bytes(self):
        raw = b'From: a@b.example\r\nSubject: X\r\n\r\nhello'
        self.assertEqual(analyze(raw)['source_sha256'], hashlib.sha256(raw).hexdigest())

    def test_empty_rejected(self):
        with self.assertRaises(ValueError): analyze(b'')

    def test_size_limit(self):
        with self.assertRaises(ValueError): analyze(b'x' * (MAX_BYTES + 1))

    def test_duplicate_from(self):
        raw = b'From: a@one.example\nFrom: b@two.example\n\nhello'
        self.assertIn('HEADER_AMBIGUITY', rules(analyze(raw)))

    def test_multiple_from_addresses(self):
        self.assertIn('HEADER_AMBIGUITY', rules(analyze(b'From: a@a.example, b@b.example\n\nhello')))

    def test_reply_domain_case_insensitive(self):
        m = message('x', 'a@COMPANY.EXAMPLE', 'b@company.example'); m.set_content('hi')
        self.assertNotIn('REPLY_DOMAIN_DIFFERS', rules(analyze(m.as_bytes())))

    def test_different_reply_domain_is_review_not_malicious(self):
        m = message('x', reply='b@partner.example'); m.set_content('hi')
        c = analyze(m.as_bytes())
        self.assertIn('REPLY_DOMAIN_DIFFERS', rules(c))
        self.assertEqual(c['disposition'], 'review_required')

    def test_passing_header_never_proves_safety(self):
        m = message('x', auth='forged.example; dmarc=pass'); m.set_content('hi')
        c = analyze(m.as_bytes())
        self.assertFalse(c['authentication_verified'])
        self.assertEqual(len(c['authentication_header_claims']), 1)

    def test_auth_failure_is_reported_claim(self):
        m = message('x', auth='gateway.example; SPF=softfail'); m.set_content('hi')
        self.assertIn('REPORTED_AUTH_FAILURE', rules(analyze(m.as_bytes())))

    def test_display_link_host_mismatch(self):
        m = message('x'); m.set_content('<a href="https://other.example/">https://company.example/</a>', subtype='html')
        self.assertIn('LINK_LABEL_MISMATCH', rules(analyze(m.as_bytes())))

    def test_matching_html_link(self):
        m = message('x'); m.set_content('<a href="https://company.example/b">https://company.example/a</a>', subtype='html')
        self.assertNotIn('LINK_LABEL_MISMATCH', rules(analyze(m.as_bytes())))

    def test_nested_label_text(self):
        m = message('x'); m.set_content('<a href="https://other.example"><b>https://company.example</b></a>', subtype='html')
        self.assertIn('LINK_LABEL_MISMATCH', rules(analyze(m.as_bytes())))

    def test_url_userinfo(self):
        m = message('x'); m.set_content('https://company.example@other.example/path')
        c = analyze(m.as_bytes())
        self.assertIn('URL_USERINFO', rules(c))
        self.assertEqual(c['urls'][0]['host'], 'other.example')

    def test_attachment_hash_and_no_write(self):
        m = message('x'); m.set_content('hi')
        m.add_attachment(b'inert', maintype='application', subtype='octet-stream', filename='../../invoice.XLSM')
        c = analyze(m.as_bytes())
        self.assertEqual(c['attachments'][0]['sha256'], hashlib.sha256(b'inert').hexdigest())
        self.assertIn('REVIEW_ATTACHMENT_TYPE', rules(c))

    def test_attached_html_not_used_as_outer_body(self):
        m = message('x'); m.set_content('hi')
        m.add_attachment('<a href="https://other.example">https://company.example</a>', subtype='html', filename='attachment.html')
        self.assertEqual(analyze(m.as_bytes())['urls'], [])

    def test_nested_email_not_used_as_outer_body(self):
        m = message('outer'); m.set_content('hi')
        inner = message('inner'); inner.set_content('https://nested.example')
        m.add_attachment(inner)
        self.assertEqual(analyze(m.as_bytes())['urls'], [])

    def test_unknown_charset_degrades_visibly(self):
        raw = b'From: a@b.example\nContent-Type: text/plain; charset=not-a-charset\n\nhttps://example.example'
        c = analyze(raw)
        self.assertIn('PARSER_DEFECT', rules(c))
        self.assertEqual(len(c['urls']), 1)

    def test_deduplicated_urls(self):
        m = message('x'); m.set_content('https://a.example https://a.example')
        self.assertEqual(len(analyze(m.as_bytes())['urls']), 1)

    def test_report_escapes_hostile_text_and_no_active_links(self):
        m = message('<script>alert(1)</script>'); m.set_content('https://evil.example')
        report = render_report([analyze(m.as_bytes())])
        self.assertNotIn('<script>', report)
        self.assertNotIn('<a ', report)
        self.assertIn('hxxps://evil[.]example', report)
        self.assertIn("default-src 'none'", report)

    def test_no_socket_connections(self):
        import socket
        m = message('x'); m.set_content('https://a.example')
        with patch.object(socket.socket, 'connect', side_effect=AssertionError('network')):
            analyze(m.as_bytes())

    def test_cli_batch_and_partial_error(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            generate(root / 'samples')
            script = str(Path(__file__).with_name('triage.py'))
            result = subprocess.run([sys.executable, script, str(root/'samples'), '--out', str(root/'out')], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            output = json.loads((root/'out/findings.json').read_text(encoding='utf-8'))
            self.assertEqual(len(output['cases']), 6)
            self.assertEqual(sum(c['disposition']=='review_required' for c in output['cases']), 5)
            (root/'samples/broken.eml').write_bytes(b'')
            result = subprocess.run([sys.executable, script, str(root/'samples'), '--out', str(root/'out')], capture_output=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn('PARTIAL RUN', (root/'out/report.html').read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
