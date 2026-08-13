# Threat Intel Enrichment Workflow

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

**Status:** Scaffold — labs not yet completed. This README will be filled in against the [project readiness checklist](../../CHECKLIST.md) once real enrichment work exists.

A documented workflow (plus optional helper script) for enriching a raw indicator using open-source threat intel sources, and a short Diamond-Model threat-actor profile built from public reporting.

## Problem Statement

*(mandatory — fill in after completing the labs)*

- **What problem does this solve?** Raw indicators (an IP or hash in a log) carry little value without context; a repeatable enrichment workflow turns them into actionable intelligence.
- **Who is this for?** SOC analysts and CTI teams triaging indicators day to day.
- **Why does it matter?** Quantify once measured — e.g., time saved per indicator, or number of sources cross-referenced automatically.

## Technical Implementation

*(mandatory — fill in with real details once the workflow is finalized)*

- **Architecture:**
  ```
  Raw indicator → OSINT lookups (VirusTotal / AbuseIPDB / WHOIS) → Enrichment summary → Confidence rating
  ```
- **Tech stack rationale:** Public/free OSINT APIs chosen to keep the workflow reproducible without paid intel feeds.
- **Core logic:** Each indicator gets a standard enrichment table plus a source-reliability rating (e.g., admiralty code).
- **Design decisions & trade-offs:** Started manual/documented; API automation (VirusTotal API) is a roadmap item.

## Demo Instructions

*(mandatory — fill in once the workflow is finalized)*

1. Take a sample public IOC (see `docs/`).
2. Run it through the documented enrichment steps.
3. Compare your result against the included sample enrichment record.

## Results / Impact

*To be filled in once a real enrichment case and threat-actor profile are completed.*

## Tech Stack

| Layer | Tools |
|---|---|
| OSINT lookups | VirusTotal, AbuseIPDB, WHOIS |
| Framework | MITRE ATT&CK, Diamond Model |
| Automation (optional) | Python (VirusTotal API) — roadmap |

## Disclaimer

For educational use only. Only publicly documented indicators and threat actors are referenced — no real employer incident data.

## License

Distributed under the [MIT License](../../LICENSE).
