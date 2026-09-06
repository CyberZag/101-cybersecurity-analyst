# SOC Authentication Triage Lab

An offline, beginner-to-intermediate defensive investigation project. **Synthetic data only. AI-assisted implementation; learner validation pending.** No real account, tenant, incident, or production deployment is represented.

## Demonstrated result

On September 6, 2026 the assistant ran the supplied 16-row fixture in its Python 3.13 execution environment. The revised code produced **three findings** (Bob: non-MFA failure sequence; Carol: MFA-denial sequence; Dana: suspicious geo-velocity). **All 30 unit tests passed.** See [actual test output](reports/test-output.txt) and [actual JSON output](reports/findings.json). These are fixture results, not measured real-world accuracy. GitHub Actions results are separate from this local execution.

## Quick start: Windows PowerShell, macOS, or Linux

Install Python 3.10 or newer and Git, then run:

```text
git clone https://github.com/CyberZag/101-cybersecurity-analyst.git
cd 101-cybersecurity-analyst
python 01-soc-alert-triage-lab/src/triage.py 01-soc-alert-triage-lab/data/auth_events.csv
python -m unittest discover -s 01-soc-alert-triage-lab/tests -v
python 01-soc-alert-triage-lab/src/triage.py 01-soc-alert-triage-lab/data/auth_events.csv --json
```

Use `python3` instead of `python` where required. No pip packages, cloud subscriptions, API keys, or paid platforms are needed. After downloading the ZIP instead, open a terminal in its `soc-portfolio` directory and run the last three commands. Exit code 0 means analysis completed, not that no alerts were found; invalid input returns 2.

## Workflow and rules

`CSV -> schema validation -> UTC normalization -> exact-row deduplication -> chronological ordering -> three rules -> prioritized evidence -> analyst report`

* **Non-MFA failure sequence:** at least five failed non-MFA events for the same user and IP within 600 seconds strictly before a successful sign-in. A candidate for investigation, not proof of password guessing: this simplified CSV has no password-failure reason.
* **MFA-fatigue candidate:** at least five denied/timed-out MFA events for the same user within 600 seconds, followed by an explicitly MFA-approved success. IP rotation is allowed. A success ends the sequence so earlier failures are not reused.
* **Suspicious geo-velocity:** consecutive successful sign-ins over 500 km apart, requiring over 900 km/h, or with simultaneous timestamps. This uses four fictional city-location fixtures, not IP geolocation. Unknown locations are skipped and are not evidence of safety.

Scores 85/80/60 are transparent educational queue priorities, not calibrated risk probabilities. Geo-velocity alone is MEDIUM: VPNs, proxies, inaccurate geolocation, and token/session behaviour require investigation. Repeated incorrect input, stale credentials, service activity, or an approved test may also explain authentication failures.

## What changed from the starter

The previous implementation counted MFA denials as brute-force failures. The revised categories separate non-MFA failures from MFA-denial events. Tests now cover negative cases, threshold boundaries, input errors, duplicated/out-of-order logs, explicit MFA approval, and repeated successes. Timezone-free timestamps are rejected rather than silently interpreted in the machine's local timezone.

The earlier KQL used fixed time bins and did not establish event order. The replacement has a time-ordered non-MFA correlation example and explicitly labels the other hunting queries as context, not equivalent production detections. **KQL has not been executed in a Microsoft tenant.**

## Evidence and learning

- [Incident report](reports/sample-incident-report.md): observations, uncertainty, validation and conditional containment.
- [Interview and learner guide](docs/interview-guide.md): explain the design and prove your own understanding.
- [Sentinel query drafts](detections/suspicious_signins.kql): environment validation required.

Before presenting this as personal implementation experience, run it yourself, explain every rule, change one threshold, add a test, and record your own results. Describe AI assistance accurately. Do not say you handled a live compromise, deployed Sentinel, or achieved a detection-accuracy percentage.

## Limitations and next steps

The fixture is intentionally tiny. Exact-row deduplication can merge genuinely distinct identical events; production logs need stable event IDs. The schema cannot represent every authentication flow, including failure after an approved MFA step. City-level data are fixtures, unknown locations are skipped, and there is no EDR/ASN/user-baseline context. This is a batch tool with in-memory data, not scalable streaming detection. Next: add stable event IDs and failure reasons, collect authorized lab telemetry, and validate schema-specific Sentinel queries. Never test against accounts or systems without permission.

## References

- Microsoft SigninLogs schema: https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/signinlogs
- Microsoft Entra error codes: https://learn.microsoft.com/en-us/entra/identity-platform/reference-error-codes
- MITRE T1110 (Brute Force): https://attack.mitre.org/techniques/T1110/
- MITRE T1621 (MFA Request Generation): https://attack.mitre.org/techniques/T1621/
- MITRE T1078 (Valid Accounts): https://attack.mitre.org/techniques/T1078/

ATT&CK mappings describe possible adversary behaviours; an alert does not prove the technique occurred. No external network calls or automated containment are performed.
