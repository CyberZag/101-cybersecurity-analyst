# Lab 01 — Header and Authentication Analysis

**Type:** Lab Guide (use a sample/synthetic phishing email — never a real internal one without authorization)

## Objective
Practice reading raw email headers to trace delivery path and interpret SPF/DKIM/DMARC results.

## Prerequisites
- A sample phishing email — use a publicly available phishing-sample dataset or construct a synthetic one; never use a real, unredacted internal email without explicit authorization.
- A header analysis tool (e.g., Google's "Message header" analyzer, MXToolbox header analyzer, or manual reading).

## Steps
1. View the raw source/headers of your sample email.
2. Trace the `Received:` chain from bottom (originating server) to top (final delivery).
3. Locate the `Authentication-Results` header and note SPF, DKIM, and DMARC outcomes.
4. Compare the "From" display name to the actual sending domain in the headers — note any mismatch.
5. Summarize your findings: does the header evidence support or contradict the claimed sender?

## Expected outcome
A short written summary of the header trace and authentication results with a preliminary spoofing assessment.

## Evidence to capture (sanitized)
- Screenshot of the header analyzer output (redact any real personal data).
- Your written summary.

Save sanitized captures under [`../evidence/`](../evidence/README.md).
