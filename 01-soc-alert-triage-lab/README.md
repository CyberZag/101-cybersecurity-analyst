# SOC Alert Triage Lab — Authentication Attack Investigation

## Objective

This beginner-to-intermediate SOC project demonstrates how to turn raw authentication telemetry into a repeatable analyst workflow. The lab uses **synthetic data only** and focuses on three common alert patterns:

1. Brute-force login attempts followed by success
2. MFA-fatigue activity followed by successful authentication
3. Impossible-travel / suspicious geo-velocity sign-ins

The goal is not just to detect an event. The goal is to show the full analyst process: **collect -> normalize -> detect -> prioritize -> investigate -> document -> recommend containment**.

## Skills demonstrated

- SOC alert triage and incident documentation
- Python log analysis
- Authentication and identity-security concepts
- Detection logic and false-positive thinking
- Microsoft Sentinel / KQL translation
- MITRE ATT&CK mapping
- Risk scoring and escalation decisions

## MITRE ATT&CK mapping

| Detection | Technique | Why it matters |
|---|---|---|
| Brute-force sequence | T1110 - Brute Force | Repeated authentication failures may indicate credential attacks |
| MFA fatigue | T1621 - MFA Request Generation | Repeated push requests can pressure a user into approval |
| Valid account after suspicious auth | T1078 - Valid Accounts | A successful login after suspicious activity may indicate account compromise |

## Repository structure

```text
01-soc-alert-triage-lab/
├── data/
│   └── auth_events.csv
├── detections/
│   └── suspicious_signins.kql
├── reports/
│   └── sample-incident-report.md
├── src/
│   └── triage.py
└── tests/
    └── test_triage.py
```

## Run the lab

From the repository root:

```bash
python 01-soc-alert-triage-lab/src/triage.py 01-soc-alert-triage-lab/data/auth_events.csv
```

No third-party Python packages are required.

Run the tests:

```bash
python -m unittest discover -s 01-soc-alert-triage-lab/tests -p "test_*.py"
```

## Analyst workflow

### 1. Establish context
For each alert, identify the user, source IP, timestamp, location, device, authentication result, and MFA result.

### 2. Build a timeline
Do not investigate events in isolation. Sort the user's activity chronologically and look for sequences such as:

```text
failed login -> failed login -> failed login -> MFA denials -> successful login
```

### 3. Ask whether the success changed the risk
A successful login after repeated failures is more important than failures alone. Validate whether the source IP, geography, device, or user behaviour changed.

### 4. Prioritize
The Python script applies simple, transparent severity logic so an analyst can explain *why* one finding should be escalated before another.

### 5. Document the evidence
The sample incident report demonstrates a concise SOC-style write-up with evidence, assessment, containment recommendations, and follow-up actions.

## Interview-ready explanation

> I built a small SOC authentication-triage lab using synthetic sign-in telemetry. I wrote Python logic to identify brute-force behaviour, MFA-fatigue patterns, and suspicious geo-velocity, then translated the same ideas into Microsoft Sentinel KQL. The important part was not only generating alerts; I built a timeline, risk-ranked the findings, mapped them to MITRE ATT&CK, and documented an analyst-style incident report with containment recommendations. It taught me how to move from raw logs to an investigation decision.

## What I would improve in production

- Replace static thresholds with baselines per user and organization
- Enrich IPs with threat-intelligence and ASN data
- Add device trust, Conditional Access, EDR, and identity-risk context
- Correlate with password resets, mailbox activity, and privilege changes
- Use ticketing/SOAR integrations for evidence capture and escalation
- Tune detections using false-positive metrics

## Scope and ethics

All events are fabricated for defensive training. No real credentials, personal data, or external targets are included.
