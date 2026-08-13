# Threat Hunting Playbooks

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

**Status:** Scaffold — labs not yet completed. This README will be filled in against the [project readiness checklist](../../CHECKLIST.md) once real hunts have been executed.

A small set of ATT&CK-mapped hunt playbooks, each with a hypothesis, target data sources, search logic, and a sample findings write-up.

## Problem Statement

*(mandatory — fill in after completing the labs)*

- **What problem does this solve?** Existing detections don't cover every technique; proactive hunts close gaps and validate coverage on a recurring basis.
- **Who is this for?** SOC teams and analysts building repeatable, ATT&CK-mapped hunt processes.
- **Why does it matter?** Quantify once measured — e.g., number of techniques covered, gaps found, new detections produced from hunt findings.

## Technical Implementation

*(mandatory — fill in with real details once playbooks are finalized)*

- **Architecture:**
  ```
  ATT&CK technique → Hypothesis → Data source(s) → Search/query → Findings → Hunt report → (optional) new detection rule
  ```
- **Tech stack rationale:** ATT&CK chosen as the common vocabulary for technique selection and reporting.
- **Core logic:** Each playbook is hypothesis-driven and documents both positive and negative findings.
- **Design decisions & trade-offs:** Prioritized TTP-based hunts over IOC-based ones for durability.

## Demo Instructions

*(mandatory — fill in once playbooks are finalized)*

1. Pick a playbook under `docs/`.
2. Review its hypothesis and target data source.
3. Run the included query against the provided sample/sanitized log data.
4. Compare your result against the documented findings.

## Results / Impact

*To be filled in after running hunts and recording findings/coverage.*

## Tech Stack

| Layer | Tools |
|---|---|
| Framework | MITRE ATT&CK |
| Query format | SIEM-native query or Sigma-style |
| Telemetry source | Sysmon / auditd (home lab) |

## Disclaimer

For educational and authorized lab use only. All logs/telemetry included are generated in an isolated home lab and sanitized before commit.

## License

Distributed under the [MIT License](../../LICENSE).
