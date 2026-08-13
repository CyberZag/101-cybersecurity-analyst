# Splunk/Wazuh Detection Lab

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

**Status:** Scaffold — labs not yet completed. This README will be filled in against the [project readiness checklist](../../CHECKLIST.md) once a real Wazuh deployment and tested alert exist.

A documented Wazuh (or Splunk) home-lab SIEM deployment: log forwarding setup, a dashboard panel, and a custom alert rule tied to the detection content from Module 04.

## Problem Statement

*(mandatory — fill in after completing the labs)*

- **What problem does this solve?** Demonstrates hands-on SIEM deployment and detection-authoring skills, not just query syntax knowledge.
- **Who is this for?** Anyone reviewing this portfolio to assess practical SIEM/detection-engineering ability.
- **Why does it matter?** Quantify once measured — e.g., time from event to alert, or detection rule accuracy.

## Technical Implementation

*(mandatory — fill in with real details once the lab is finalized)*

- **Architecture:**
  ```
  Victim VM (Wazuh agent) → Wazuh manager (monitoring VM) → Dashboard + custom alert rule
  ```
- **Tech stack rationale:** Wazuh chosen for free/open-source SIEM + host agent monitoring in a home lab.
- **Core logic:** Custom rule fires on a failed-login threshold within a time window; dashboard visualizes the same metric.
- **Design decisions & trade-offs:** Wazuh over Splunk Enterprise to avoid licensing constraints in a home lab; documented so it's portable to Splunk/Elastic syntax later.

## Demo Instructions

*(mandatory — fill in once the lab is finalized)*

1. Review the rule definition and dashboard screenshot under `docs/`/`scripts/`.
2. Reproduce the setup in your own Wazuh instance using the documented steps.
3. Trigger the same test condition and confirm the alert fires.

## Results / Impact

*To be filled in once the lab is fully tested.*

## Tech Stack

| Layer | Tools |
|---|---|
| SIEM | Wazuh (Elastic/OpenSearch-based) |
| Agents | Wazuh agent on victim VM |
| Alternative | Splunk Free / Elastic Stack (if used instead) |

## Disclaimer

For educational and authorized home-lab use only. All logs and alerts are generated in an isolated lab and sanitized before commit.

## License

Distributed under the [MIT License](../../LICENSE).
