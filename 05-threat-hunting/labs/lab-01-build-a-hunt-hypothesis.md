# Lab 01 — Build a Hunt Hypothesis

**Type:** Lab Guide (research/planning — no live systems required)

## Objective
Pick a MITRE ATT&CK technique and build a testable, falsifiable hunt hypothesis around it.

## Prerequisites
- None beyond internet access to browse ATT&CK.

## Steps
1. Browse [MITRE ATT&CK](https://attack.mitre.org/) and pick one technique relevant to your lab environment (e.g., T1059 Command and Scripting Interpreter, T1053 Scheduled Task/Job, or T1071 Application Layer Protocol for C2).
2. Write a one-sentence hypothesis in the form: "If technique X were used in this environment, we would expect to see evidence Y in data source Z."
3. List the specific data source(s) needed to test it (e.g., process creation logs, DNS logs, scheduled-task logs).
4. Draft the search logic (a plain-language query, or an actual SIEM/Sigma-style query if you have log access) you'd run to look for that evidence.

## Expected outcome
A documented hypothesis, target data source, and draft query — ready to execute in Lab 02.

## Evidence to capture
- The written hypothesis and draft query (save under [`../project/docs/`](../project/docs)).
