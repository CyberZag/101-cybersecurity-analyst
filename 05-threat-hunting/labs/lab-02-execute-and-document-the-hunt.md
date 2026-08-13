# Lab 02 — Execute and Document the Hunt

**Type:** Lab Guide (home-lab VM/logs)

## Objective
Run the hypothesis from Lab 01 against real (lab-generated) logs and write a hunt report.

## Prerequisites
- Completed Lab 01.
- Access to logs from your lab VMs (e.g., the Sysmon/auditd logs from Module 04, or fresh logs generated for this hunt).

## Steps
1. Generate the activity your hypothesis targets in your own lab (safely and intentionally — e.g., run an encoded PowerShell command, or set up a scheduled task) so there's something to find.
2. Run your draft query/search against the logs.
3. Record what you found: matching events, false positives, or nothing at all.
4. Write a short hunt report: Hypothesis → Data sources → Method → Findings → IOCs/TTPs identified (if any) → Recommendation (new detection rule? no action needed? more data required?).

## Expected outcome
A completed hunt report, even if the finding is "no evidence of this technique in the tested window" — that's still a valid, documented result.

## Evidence to capture (sanitized)
- The hunt report (place under [`../project/docs/`](../project/docs)).
- Query/search results (sanitized screenshots or exported text).

Save sanitized captures under [`../evidence/`](../evidence/README.md).
