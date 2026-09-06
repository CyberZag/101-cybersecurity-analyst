# Interview and learner guide

## Your immediate goal

Do not memorize a claim that you independently built something you have not yet run. This project was improved with AI assistance. Your ownership comes from being able to execute, explain, test, change, and critique it. Treat the following as a learning guide, not permission to invent experience.

## Five practical exercises

1. Run the CLI and the 30 tests. Save your own output separately with date and Python version.
2. Change `--min-count` from 5 to 6. Predict which findings remain, then verify. Expected: only Dana's geo-velocity finding remains.
3. Change one of Carol's denials to `timeout`. Explain why the MFA rule should still trigger.
4. Replace Dana's Tokyo location with a city absent from CITY_COORDS. Explain why no geo finding is not a clean bill of health.
5. Add a test using stable event IDs, then implement ID-based deduplication. Explain the current exact-row limitation.

## 60-second explanation — use after completing those exercises

“I worked through an AI-assisted Python lab for authentication-alert triage. It validates and normalizes synthetic sign-in logs, then investigates non-MFA failure bursts, MFA-denial sequences, and suspicious geo-velocity. I focused on distinguishing an alert from a confirmed incident and avoiding misleading detections. For example, the starter counted denied MFA prompts as brute-force failures. I studied the fix separating those categories and tested the threshold and event-order edge cases. The supplied fixture has three findings, and I can reproduce the tests and explain their limits. This is lab work, not production incident-response experience.”

Replace the sentence about studying/testing with the precise changes you personally made. Do not claim the assistant's execution environment as your home lab.

## Questions interviewers may ask

**What business problem does this solve?**
An analyst needs a consistent way to turn authentication records into an evidence-backed queue rather than treating every failed login as a breach. The tool demonstrates validation, correlation, prioritization and written handoff.

**What is your architecture?**
CSV input -> validation -> UTC timestamps -> deduplication -> sorting -> rule evaluation -> structured findings -> analyst documentation. It runs offline using Python's standard library. The source is separated from test and report artifacts.

**Why is a successful login after failures suspicious, but not conclusive?**
It may be credential guessing followed by access, but could be a legitimate user correcting an error, stale stored credentials, automation, or an approved test. Verify failure reason, device/session, source, user baseline, and subsequent activity before declaring compromise.

**Why not call every failed login brute force?**
A generic failure can be MFA denial, a policy block or another authentication error. The CSV rule only excludes known MFA failures; it still lacks a password-failure reason. The draft Entra query narrows to a documented credential-error code but even that does not prove an attack.

**How does MFA fatigue differ?**
Repeated denied/timed-out requests followed by explicit approval can justify investigation of push fatigue. The code tracks the user across IPs because an attacker can rotate sources. It is still a hypothesis requiring authentication-flow and user context.

**Why are time bins risky for sequence detection?**
Counting failures and successes in a ten-minute bucket does not prove failures came first. A real sequence can also straddle a bucket boundary. Correlate event timestamps around each success and reset the sequence after a success.

**What does 30 passing tests establish?**
Expected behaviour on specified fixtures and edge cases in the tested runtime. It does not establish production accuracy, detection completeness, or compatibility with a tenant schema. No precision/recall claim is justified without representative labelled data.

**What false positives would you investigate?**
VPN/proxy egress, geolocation errors, a forgotten password, stale service credentials, legitimate repeated MFA attempts, shared accounts, and authorized testing. Obtain trustworthy user/device/session context. Do not blanket-allowlist a country or every VPN.

**Why MEDIUM for geo-velocity?**
It warrants context gathering, but network geolocation does not reliably establish a person's physical location. Stronger evidence such as unfamiliar device, risky account changes or unauthorized activity can justify escalation.

**How would you respond in a real SOC?**
Validate the alert and source, preserve evidence, correlate identity/device/post-login logs, establish scope and impact, and escalate under the incident process. If authorized and supported by evidence, contain accounts/sessions/devices following the runbook. This program intentionally performs no containment.

**What would you build next?**
Stable event IDs; explicit authentication-failure reasons; better tests; an authorized real-log adapter; user/device/ASN context; schema-validated Sentinel queries; controlled alert suppression; and a reviewed ticketing integration.

## Existing trading-account monitor: a second interview story

Your separate repository describes a Python detection pipeline over synthetic trading-account telemetry, with Pydantic validation, five detection ideas, correlated cases, Markdown reports and a Streamlit dashboard. Its committed demo log records six alerts and five cases. That is a historical repository result, not a new execution in this task.

Explain why it monitors account security rather than investment signals. Be ready to trace one event through schema -> rule -> alert -> correlated case -> dashboard. Study why MFA-fatigue and risky-account-change alerts can belong to one investigation. Do not claim financial returns, real account monitoring, or professional trading experience from the existence of the project.

Repository: https://github.com/CyberZag/trading-account-security-monitor
Evidence: https://github.com/CyberZag/trading-account-security-monitor/blob/main/evidence/logs/demo_pipeline_output.txt

## Readiness check

Ready to feature when you can demo without reading a script, explain a failure and a fix, add a passing test, state limitations, and clearly distinguish your own changes from AI-generated scaffolding. Add your own learning notes and commit them; do not generate fake screenshots, backdated commits or invented incident evidence.
