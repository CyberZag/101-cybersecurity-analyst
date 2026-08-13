# Phishing Analysis Casebook

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

**Status:** Scaffold — labs not yet completed. This README will be filled in against the [project readiness checklist](../../CHECKLIST.md) once real triage write-ups exist.

A casebook of phishing triage write-ups (using sample/synthetic emails) covering header, URL, and attachment analysis, each ending in a documented verdict and recommended action.

## Problem Statement

*(mandatory — fill in after completing the labs)*

- **What problem does this solve?** Phishing is one of the highest-volume SOC queues; a documented, repeatable triage method keeps decisions consistent and defensible.
- **Who is this for?** SOC analysts and anyone reviewing this portfolio for phishing-triage competency.
- **Why does it matter?** Quantify once measured — e.g., average triage time per case, or number of indicators checked per verdict.

## Technical Implementation

*(mandatory — fill in with real details once cases are finalized)*

- **Architecture:**
  ```
  Sample email → Header/auth analysis → URL decode + reputation check → Attachment hash/metadata → Verdict + recommendation
  ```
- **Tech stack rationale:** CyberChef and free reputation lookups chosen to keep the workflow reproducible without paid tooling.
- **Core logic:** Every case follows the same four-step structure ending in an explicit verdict.
- **Design decisions & trade-offs:** No live URL visits or attachment execution — reputation/metadata analysis only.

## Demo Instructions

*(mandatory — fill in once cases are finalized)*

1. Open a case write-up under `docs/`.
2. Review the header trace, URL decode/reputation results, and attachment metadata.
3. Compare your own conclusion to the documented verdict.

## Results / Impact

*To be filled in once real cases are completed.*

## Tech Stack

| Layer | Tools |
|---|---|
| Header analysis | MXToolbox / Google Message Header tool |
| URL analysis | CyberChef, VirusTotal |
| Attachment triage | Hashing tools, VirusTotal |

## Disclaimer

For educational use only. All emails used are sample/synthetic or from public phishing datasets — no real unredacted internal correspondence. No suspicious URLs are visited directly and no attachments are executed.

## License

Distributed under the [MIT License](../../LICENSE).
