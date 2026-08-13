# Lab 02 — Bash Log Triage Script

**Type:** Lab Guide (authorized lab/home-lab use only)

## Objective
Write a Bash script that summarizes authentication activity from a Linux log file — the seed for the Module 02 portfolio project.

## Prerequisites
- Completed Lab 01.
- A Linux VM with some login history (successful and a few failed attempts are fine to generate yourself in your own lab).

## Steps
1. Locate the auth log: `/var/log/auth.log` (Debian/Ubuntu) or `/var/log/secure` (RHEL/CentOS), or use `journalctl -u ssh` / `journalctl _COMM=sshd`.
2. Generate a couple of failed logins intentionally in your own lab (e.g., `ssh baduser@localhost` with a wrong password) so you have sample data.
3. Write a Bash script `auth-summary.sh` that:
   - Counts failed login attempts, grouped by source IP or username.
   - Counts successful logins.
   - Prints a simple summary table to stdout.
4. Test the script against your log file and review the output for accuracy.
5. Note any thresholds you'd use to flag "suspicious" activity (e.g., more than N failed attempts from one source in a short window).

## Expected outcome
A working script and a short write-up of what it reports and why those thresholds make sense.

## Evidence to capture (sanitized)
- The script itself (place a copy under [`../project/scripts/`](../project/scripts)).
- Sanitized sample output (no real hostnames/IPs from production systems).

Save sanitized captures under [`../evidence/`](../evidence/README.md).
