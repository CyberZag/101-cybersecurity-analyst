# Lab 01 — IOC Enrichment Workflow

**Type:** Lab Guide (uses public/open-source threat intel lookups only)

## Objective
Practice enriching a raw indicator (IP, domain, or hash) using open-source threat intelligence tools.

## Prerequisites
- Internet access.
- Free accounts (optional but useful) on VirusTotal, AbuseIPDB, or similar OSINT platforms.
- A sample indicator — use a well-known, publicly documented malicious IOC from a published threat report (never enrich or publish real IOCs tied to your employer's actual incidents).

## Steps
1. Pick a public, well-documented IOC from a reputable published threat report (cite the report).
2. Look it up in VirusTotal, AbuseIPDB, and/or a WHOIS lookup tool.
3. Record: reputation/detection score, first/last-seen dates, associated campaigns or malware families (if reported), and geolocation/ASN.
4. Summarize the enriched indicator in a short table: raw indicator → enrichment fields → source(s) → confidence assessment.

## Expected outcome
One fully enriched IOC record with cited sources and a stated confidence level.

## Evidence to capture (sanitized)
- Screenshots of the lookups (redact your own account/session details).
- The enrichment summary table.

Save sanitized captures under [`../evidence/`](../evidence/README.md).
