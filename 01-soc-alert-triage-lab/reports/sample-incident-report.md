# Sample SOC Incident Report — Suspicious Authentication Sequence

## Incident summary

**Severity:** Critical  
**Status:** Escalate for containment  
**Affected identity:** `carol`  
**Primary source:** `192.0.2.44`  
**MITRE ATT&CK:** T1621 (MFA Request Generation), T1078 (Valid Accounts)

## What happened

Synthetic authentication telemetry shows five denied MFA prompts for the same user between 14:00 and 14:04 UTC, followed by a successful authentication at 14:05 UTC from the same source IP.

## Why this is suspicious

Repeated MFA denials followed by an approval can indicate MFA fatigue: an attacker who already has valid credentials repeatedly generates prompts until the user accepts one. The successful sign-in increases the urgency because the activity is no longer only attempted access.

## Evidence reviewed

| Time (UTC) | User | Source IP | Result | MFA result |
|---|---|---|---|---|
| 14:00 | carol | 192.0.2.44 | Failed | Denied |
| 14:01 | carol | 192.0.2.44 | Failed | Denied |
| 14:02 | carol | 192.0.2.44 | Failed | Denied |
| 14:03 | carol | 192.0.2.44 | Failed | Denied |
| 14:04 | carol | 192.0.2.44 | Failed | Denied |
| 14:05 | carol | 192.0.2.44 | Success | Approved |

## Analyst assessment

**Assessment:** Likely suspicious; requires immediate user validation and session review.

Potential false positives include a legitimate user repeatedly rejecting prompts caused by a misconfigured application or an authentication retry loop. However, the successful approval after multiple denials is enough to justify escalation.

## Recommended containment

1. Validate the activity directly with the user through a trusted channel.
2. Revoke active sessions if the login is not recognized.
3. Reset the password and require re-registration of MFA where appropriate.
4. Review Conditional Access, sign-in risk, device identity, and source-IP reputation.
5. Hunt for post-authentication activity such as mailbox changes, privilege changes, token use, downloads, or unusual endpoint activity.
6. Preserve the timeline and evidence in the case record.

## Follow-up questions

- Was the source device known and compliant?
- Was the user traveling or using a corporate VPN?
- Did any risky account changes occur after 14:05 UTC?
- Were other users targeted by the same IP?
- Did the source IP appear in threat-intelligence or prior incidents?

## Scope note

This report is based entirely on fabricated training data and demonstrates defensive SOC documentation technique only.
