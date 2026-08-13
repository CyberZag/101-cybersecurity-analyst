# Lab 01 — EDR Telemetry Review

**Type:** Lab Guide (home-lab VM only)

## Objective
Generate and review basic EDR-style telemetry (process creation, network connections) on a lab VM to understand what an analyst actually looks at during triage.

## Prerequisites
- The victim VM from Module 03's lab topology.
- A free/trial EDR-like tool or built-in OS logging (e.g., Windows Sysmon, or `auditd` on Linux) configured to log process creation and network events.

## Steps
1. Install and configure Sysmon (Windows) or `auditd` (Linux) on your lab victim VM with a sensible default config (e.g., SwiftOnSecurity's Sysmon config is a common starting point).
2. Generate a few benign process-creation events yourself (open a browser, run a script, launch a shell from another process).
3. Review the resulting logs — identify parent/child process relationships and any network connections tied to those processes.
4. Pick one process chain and diagram it (parent → child → network connection if any).

## Expected outcome
A short diagram/write-up of one process chain observed in your lab, annotated with what each step represents.

## Evidence to capture (sanitized)
- Screenshot of the relevant log entries.
- Your process-tree diagram.

Save sanitized captures under [`../evidence/`](../evidence/README.md).
