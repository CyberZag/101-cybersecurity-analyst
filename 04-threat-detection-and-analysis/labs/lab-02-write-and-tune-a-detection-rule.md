# Lab 02 — Write and Tune a Detection Rule

**Type:** Lab Guide (home-lab VM only)

## Objective
Write a basic detection rule for a specific behavior and tune it against benign activity to reduce false positives.

## Prerequisites
- Completed Lab 01.
- Familiarity with Sigma rule syntax (or your SIEM's native query language, if you have SIEM access — otherwise this can be done as a Sigma YAML rule against the logs from Lab 01).

## Steps
1. Choose one specific behavior to detect (e.g., "PowerShell spawned from Microsoft Word" or "a shell spawned from a web server process").
2. Write a first-draft detection rule (Sigma YAML or your SIEM query) expressing that logic.
3. Test the rule against your Lab 01 logs — does it fire on the behavior you intended?
4. Generate a benign activity that might trigger a false positive, run the rule again, and note whether it fires when it shouldn't.
5. Refine the rule (add an exclusion, tighten a field match) to reduce the false positive while still catching the original test case.
6. Document the before/after and your reasoning.

## Expected outcome
A tuned detection rule plus a short before/after note explaining the false-positive fix.

## Evidence to capture (sanitized)
- The rule text (place a copy under [`../project/scripts/`](../project/scripts) or `../project/docs/`).
- Before/after test results.

Save sanitized captures under [`../evidence/`](../evidence/README.md).
