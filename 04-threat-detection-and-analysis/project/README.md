# Detection Engineering Pack

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

**Status:** Scaffold — labs not yet completed. This README will be filled in against the [project readiness checklist](../../CHECKLIST.md) once real detections and triage evidence exist.

A small pack of documented detection rules (Sigma-style) plus a triage case study demonstrating true-positive vs. false-positive reasoning and tuning.

## Problem Statement

*(mandatory — fill in after completing the labs)*

- **What problem does this solve?** Raw EDR/SIEM telemetry is high-volume and noisy; a well-tuned detection rule turns it into an actionable, low-noise alert.
- **Who is this for?** SOC teams and individual analysts building/maintaining detection content.
- **Why does it matter?** Quantify once measured — e.g., false-positive rate before/after tuning.

## Technical Implementation

*(mandatory — fill in with real details once the rules are finalized)*

- **Architecture:**
  ```
  EDR/host telemetry → Detection rule (Sigma/SPL/KQL) → Alert → Analyst triage note (TP/FP + reasoning)
  ```
- **Tech stack rationale:** Sigma chosen for vendor-agnostic portability across SIEM backends.
- **Core logic:** One rule per documented behavior, each with a before/after tuning note.
- **Design decisions & trade-offs:** Prioritized a small number of well-documented rules over a large but shallow set.

## Demo Instructions

*(mandatory — fill in once rules are finalized)*

1. Review each rule under `docs/` or `scripts/` along with its accompanying test log.
2. Run the rule against the provided sample log (sanitized/synthetic) to reproduce the alert.
3. Review the triage write-up explaining the TP/FP decision.

## Results / Impact

*To be filled in after measuring false-positive rate before/after tuning.*

## Tech Stack

| Layer | Tools |
|---|---|
| Detection format | Sigma (or native SIEM query language) |
| Telemetry source | Sysmon / auditd (home lab) |
| Testing | Manual replay against lab-generated logs |

## Disclaimer

For educational and authorized lab use only. All logs/telemetry included are generated in an isolated home lab and sanitized before commit.

## License

Distributed under the [MIT License](../../LICENSE).
