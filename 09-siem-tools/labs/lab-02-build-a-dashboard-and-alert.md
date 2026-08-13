# Lab 02 — Build a Dashboard and Alert

**Type:** Lab Guide (home-lab VMs only)

## Objective
Build a simple dashboard panel and a custom alert rule in Wazuh, and test that the alert fires correctly.

## Prerequisites
- Completed Lab 01.

## Steps
1. In the Wazuh dashboard, create a visualization/panel summarizing a metric — e.g., failed login attempts per hour on the victim VM.
2. Write a custom Wazuh rule (or use/adjust an existing ruleset) that fires when failed logins exceed a threshold in a time window.
3. Generate enough failed-login events on the victim VM to intentionally trigger the rule.
4. Confirm the alert fires and review the resulting alert details.
5. Document the rule logic and the test result.

## Expected outcome
A working dashboard panel plus a tested, firing custom alert rule with documented logic.

## Evidence to capture (sanitized)
- Screenshot of the dashboard panel.
- Screenshot of the fired alert.
- The rule definition (place a copy under [`../project/scripts/`](../project/scripts)).

Save sanitized captures under [`../evidence/`](../evidence/README.md).
