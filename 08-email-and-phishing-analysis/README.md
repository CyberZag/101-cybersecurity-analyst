# 08 Email and Phishing Analysis

A portfolio-ready study module based on the Email & Phishing Analysis section of *The Complete Hands-On Cybersecurity Analyst Course*. Phishing triage is one of the highest-volume queues in most SOCs — this module builds the header, URL, and attachment analysis skills needed to triage it efficiently.

## Learning objectives

By the end of this module, I can:

- Read raw email headers and trace the delivery path (Received headers, SPF/DKIM/DMARC results).
- Identify common phishing indicators: spoofed sender domains, lookalike URLs, urgency language, mismatched display names.
- Safely analyze a suspicious URL without visiting it directly (URL decoding, sandboxed browsing, reputation lookups).
- Safely review a suspicious attachment's metadata without executing it.
- Write a phishing triage report with a clear verdict and recommended action (block/quarantine/user notification).

## Concept map

| Topic | What it does | Analyst relevance |
|---|---|---|
| Email headers | Full delivery path plus authentication results | First place to check for spoofing/relay anomalies |
| SPF / DKIM / DMARC | Sender authentication mechanisms | A fail on these is a strong (not definitive) phishing signal |
| URL analysis | Decoding/expanding links, reputation checks | Reveals redirect chains and malicious landing pages without visiting them live |
| Attachment triage | Hash + metadata review (no execution) | Connects back to Module 07's static-analysis skills |
| Triage verdict & response | Documented decision + action | Turns analysis into a concrete SOC outcome |

## Key notes

### Headers tell the real story
The `Received:` header chain shows the actual path a message took across mail servers — often revealing a mismatch between the claimed sender domain and the actual originating infrastructure. SPF, DKIM, and DMARC results (usually visible in `Authentication-Results`) indicate whether the sending domain passed its own authentication policies.

### Common phishing patterns
Lookalike domains (e.g., a single character swapped), mismatched display name vs. actual address, urgency/fear language, and unexpected attachment types are recurring signals worth checking every time, even when one signal alone isn't conclusive.

### Safe URL analysis
Tools like CyberChef (URL decode) or a sandboxed/disposable browsing environment let an analyst expand shortened/obfuscated links and see where they redirect without exposing a real endpoint to a potentially malicious page.

### Attachments — inspect, don't open
Attachment triage should stay at the "hash it, check reputation, review metadata" stage (same discipline as Module 07) unless there's a proper isolated sandbox for detonation.

## Labs

See [`labs/`](./labs) for hands-on exercises:
- [`lab-01-header-and-authentication-analysis.md`](./labs/lab-01-header-and-authentication-analysis.md)
- [`lab-02-url-and-attachment-triage.md`](./labs/lab-02-url-and-attachment-triage.md)

## Portfolio project

See [`project/`](./project) — **Phishing Analysis Casebook**, a set of triage write-ups (using safe/sample or synthetic phishing emails) covering header, URL, and attachment analysis with a documented verdict.

## Resources

See [`resources.md`](./resources.md) for tools and reference links.
