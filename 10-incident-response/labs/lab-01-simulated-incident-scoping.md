# Lab 01 — Simulated Incident Scoping

**Type:** Lab Guide / Simulated Case Study (home-lab VMs)

## Objective
Practice scoping a simulated incident using telemetry from earlier modules' lab VMs.

## Prerequisites
- The lab topology and telemetry sources from Modules 03, 04, and 09 (victim VM with Sysmon/auditd, Wazuh dashboard).

## Steps
1. Define a simple simulated scenario (e.g., "a suspicious PowerShell process was observed on the victim VM, followed by an outbound connection to an unrecognized IP").
2. Intentionally generate matching activity in your lab so there's real telemetry to work from.
3. Using your Wazuh dashboard/EDR logs, identify: which host(s), which user account(s), and which process(es) are involved.
4. Write a scoping note: what's confirmed affected, what's still unknown, and what additional data you'd need to close the gaps.

## Expected outcome
A written scoping note clearly separating "confirmed" from "unknown," with a plan for closing the unknowns.

## Evidence to capture (sanitized)
- Screenshots of the relevant telemetry.
- The scoping note (place under [`../project/docs/`](../project/docs)).

Save sanitized captures under [`../evidence/`](../evidence/README.md).
