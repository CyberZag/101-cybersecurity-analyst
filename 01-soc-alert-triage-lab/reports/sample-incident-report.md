# Synthetic incident-triage report

**Case:** LAB-AUTH-001 | **Data:** fabricated sign-ins dated August 20, 2026 | **Review date:** September 6, 2026

**Status:** Three detection candidates; no real compromise established. No production data, user contact, containment or external lookup was performed. The assistant executed the tool locally; the learner must reproduce it.

## Evidence

- **Bob, 13:00–13:05 UTC:** five non-MFA failures followed by a successful sign-in from the same synthetic source, 203.0.113.77. Queue priority HIGH (80, illustrative). Possible credential attack; failure reasons and legitimate-user context are missing.
- **Carol, 14:00–14:05 UTC:** five denied MFA events followed by explicit approved success. Priority HIGH (85, illustrative). Possible push-fatigue sequence; the source, 192.0.2.44, is a documentation address. This no longer creates a duplicate brute-force finding.
- **Dana, 15:00–15:25 UTC:** successful Toronto and Tokyo fixture locations about 10,352 km apart in 25 minutes. Priority MEDIUM (60, illustrative). This cannot establish actual travel or unauthorized access.
- **Alice:** no detection candidate on the supplied two successful Toronto events. Absence of an alert is not proof of account safety.

All source IPs are reserved documentation examples; country/city values were supplied as synthetic data, not looked up from these addresses. Event timestamps are normalized to UTC. Exact output is in findings.json; all 30 supplied tests passed in the recorded local run.

## Recommended investigation in an authorized environment

Verify event IDs, collection quality, authentication error and method, tenant policy, device trust, source ASN and known VPN egress, sessions, user baseline, and sign-ins around the alert. Correlate with password/MFA resets, newly created credentials, mailbox rules, privileged actions, endpoint events and other account changes. Contact the user through a trusted channel under the organization's incident process. Preserve original logs and document facts separately from assumptions.

## Escalation and containment

Escalate based on evidence, asset sensitivity and the organization's severity matrix, not these illustrative scores. If unauthorized access is corroborated, follow the approved runbook for revoking sessions, credential/MFA recovery and any device containment. Obtain required authority, capture evidence, consider business impact, and validate recovery. This lab did not take any such actions.

## Limitations

Sixteen fabricated events are insufficient to measure precision, recall, false-positive rate or business impact. No tenant deployment or KQL execution occurred. The current schema and city fixture are deliberately limited. This document is a practice analyst handoff, not a historical breach report.
