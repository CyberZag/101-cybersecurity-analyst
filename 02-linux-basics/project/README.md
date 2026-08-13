# Linux Security Triage Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

**Status:** Scaffold — labs not yet completed. This README will be filled in against the [project readiness checklist](../../CHECKLIST.md) once real lab evidence exists.

A small toolkit of Bash/Python scripts that audits a Linux host for common security-relevant conditions: risky file permissions, SUID/SGID binaries, and authentication-log anomalies.

## Problem Statement

*(mandatory — fill in after completing the labs)*

- **What problem does this solve?** SOC analysts and sysadmins need a fast way to spot risky permission configurations and suspicious login activity on a Linux host without manually grepping logs every time.
- **Who is this for?** Junior SOC analysts, sysadmins, home-lab learners.
- **Why does it matter?** Quantify once measured — e.g., "reduced manual audit time from N minutes to a single command."

## Technical Implementation

*(mandatory — fill in with real details once scripts are finalized)*

- **Architecture:**
  ```
  Log file / filesystem → Bash/Python parser → Findings summary (stdout / report file)
  ```
- **Tech stack rationale:** Bash for direct filesystem/log commands; Python optional for structured output/reporting.
- **Core logic:** Permission audit (`find` for world-writable + SUID/SGID files) and auth-log summarizer (failed vs. successful logins, grouped by source).
- **Design decisions & trade-offs:** Started with `find`/`grep`-based Bash for zero dependencies; a Python rewrite is a roadmap item for structured JSON output.

## Demo Instructions

*(mandatory — fill in once the script is finalized and tested)*

1. Clone the repo and `cd` into this project folder.
2. Run the permission audit script against a lab VM (never against a system without authorization).
3. Run the auth-log summarizer against a sample or sanitized log.
4. Review the printed summary.

## Results / Impact

*To be filled in after running the toolkit against real (sanitized) lab data.*

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Bash, Python 3.x (optional) |
| Target OS | Linux (Debian/Ubuntu, RHEL/CentOS) |
| Testing | Manual verification in home-lab VM |

## Disclaimer

For educational and authorized lab use only. Run only against systems you own or are explicitly authorized to test. Any logs or output included in this repo are sanitized or synthetic.

## License

Distributed under the [MIT License](../../LICENSE).
