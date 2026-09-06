"""Generate original, inert examples using reserved .example domains."""
from email.message import EmailMessage
from email import policy
from pathlib import Path


def message(subject, sender='training@company.example', reply=None, auth=None):
    m = EmailMessage(policy=policy.SMTP)
    m['From'] = sender
    m['To'] = 'analyst@company.example'
    m['Date'] = 'Sun, 06 Sep 2026 12:00:00 +0000'
    m['Subject'] = subject
    if reply:
        m['Reply-To'] = reply
    if auth:
        m['Authentication-Results'] = auth
    return m


def generate(out=Path('samples')):
    out.mkdir(parents=True, exist_ok=True)
    cases = {}
    m = message('Synthetic case 01 — routine training update')
    m.set_content('The training schedule is available at https://training.company.example/schedule')
    cases['01-routine.eml'] = m
    m = message('Synthetic case 02 — account review', 'support@company.example', 'collect@external.example',
                'unverified-gateway.example; spf=fail; dmarc=fail')
    m.set_content('Please review your account. This message is an inert training fixture.')
    m.add_alternative('<p>Training fixture only</p><a href="https://collect.external.example/login">https://portal.company.example/login</a>', subtype='html')
    cases['02-link-mismatch.eml'] = m
    m = message('Synthetic case 03 — inert attachment')
    m.set_content('A placeholder attachment for hashing practice. It contains no executable code.')
    m.add_attachment(b'INERT TRAINING PLACEHOLDER\n', maintype='application', subtype='octet-stream', filename='invoice.xlsm')
    cases['03-attachment.eml'] = m
    m = message('Synthetic case 04 — partner reply workflow', 'news@company.example', 'events@partner.example')
    m.set_content('Expected partner replies can trigger an exact-domain mismatch. Validate the relationship out of band.')
    cases['04-benign-control.eml'] = m
    m = message('Synthetic case 05 — userinfo URL and passing claim', auth='attacker-supplied.example; spf=pass; dkim=pass; dmarc=pass')
    m.set_content('The host is after the @ symbol: https://portal.company.example@collect.external.example/login')
    cases['05-auth-pass-trap.eml'] = m
    m = message('Synthetic case 06 — reported failure alone', auth='unverified-gateway.example; spf=softfail')
    m.set_content('A claimed authentication failure needs gateway confirmation and context. It does not prove phishing.')
    cases['06-auth-failure.eml'] = m
    for name, item in cases.items():
        if item.is_multipart():
            item.set_boundary('synthetic-boundary-' + name)
        (out / name).write_bytes(item.as_bytes())
    print(f'Generated {len(cases)} inert messages')


if __name__ == '__main__':
    generate()
