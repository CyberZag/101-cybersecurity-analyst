# Incident Response Case Study

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

**Status:** Scaffold — labs not yet completed. This README will be filled in against the [project readiness checklist](../../CHECKLIST.md) once a real simulated case is finished.

An end-to-end simulated incident response case: scoping note, chronological timeline built from lab telemetry, a justified containment decision, and a final report written for both technical and executive audiences.

## Problem Statement

*(mandatory — fill in after completing the labs)*

- **What problem does this solve?** Demonstrates the full IR lifecycle in practice — not just knowledge of the NIST phases, but the ability to scope, timeline, decide, and report on a real (simulated) incident.
- **Who is this for?** Anyone reviewing this portfolio to assess end-to-end IR capability.
- **Why does it matter?** Quantify once measured — e.g., time from detection to containment decision in the simulated case.

## Technical Implementation

*(mandatory — fill in with real details once the case is finalized)*

- **Architecture:**
  ```
  Simulated scenario → Lab telemetry (EDR/Wazuh/auth logs) → Scoping note → Timeline → Containment decision → Final report
  ```
- **Tech stack rationale:** Reuses the Module 03/04/09 lab stack rather than introducing new tooling, to focus purely on IR process.
- **Core logic:** Timeline construction merges multiple log sources into one chronological view; containment decisions are documented with explicit reasoning.
- **Design decisions & trade-offs:** Scenario is intentionally simulated/synthetic rather than a real incident, for safety and reproducibility.

## Demo Instructions

*(mandatory — fill in once the case is finalized)*

1. Read the scoping note under `docs/`.
2. Review the timeline table.
3. Review the containment decision and final report.

## Results / Impact

*To be filled in once the case is fully documented.*

## Tech Stack

| Layer | Tools |
|---|---|
| Telemetry sources | Sysmon/auditd, Wazuh dashboard |
| Documentation | Markdown timeline tables, structured report template |

## Disclaimer

This is a simulated case study for educational/portfolio purposes. No real, unauthorized incident data is used.

## License

Distributed under the [MIT License](../../LICENSE).
