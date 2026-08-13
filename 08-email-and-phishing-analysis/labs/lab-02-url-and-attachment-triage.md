# Lab 02 — URL and Attachment Triage

**Type:** Lab Guide (sample/synthetic data only — no live malicious URLs or attachments)

## Objective
Safely analyze a suspicious URL and attachment from a sample phishing email without directly visiting or executing either.

## Prerequisites
- Completed Lab 01.
- CyberChef (for URL decoding) and access to VirusTotal/URL reputation checkers.

## Steps
1. Extract the URL(s) from your sample email; decode/expand any shortened or obfuscated links using CyberChef.
2. Check the expanded URL's reputation via VirusTotal or a similar service — do not visit it directly in a normal browser.
3. If your sample includes an attachment, compute its hash and check reputation (per Module 07 static-analysis practice) rather than opening it.
4. Write a final triage verdict: malicious / suspicious / benign, with your supporting evidence, and a recommended action (block sender domain, quarantine, notify users, etc.).

## Expected outcome
A completed triage report combining header, URL, and attachment findings into a single verdict and recommendation.

## Evidence to capture (sanitized)
- CyberChef decode screenshot.
- Reputation-check screenshots.
- Final triage report (place under [`../project/docs/`](../project/docs)).

Save sanitized captures under [`../evidence/`](../evidence/README.md).
