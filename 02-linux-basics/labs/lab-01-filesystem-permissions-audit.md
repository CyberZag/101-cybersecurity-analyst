# Lab 01 — Filesystem & Permissions Audit

**Type:** Lab Guide (authorized lab/home-lab use only)

## Objective
Practice navigating the Linux filesystem and auditing file/directory permissions for common misconfigurations.

## Prerequisites
- A Linux VM in your own virtual lab (see Module 03 — Virtual Lab Setup) — never run this against a system you do not own or have explicit authorization to test.
- Basic terminal access (local user is fine; some steps benefit from `sudo`).

## Steps
1. Explore the filesystem hierarchy: `ls -la /`, then inspect `/etc`, `/var/log`, `/home`, `/proc`.
2. List permissions for your home directory and a system directory: `ls -la ~` and `ls -la /etc`.
3. Find world-writable files: `find / -xdev -type f -perm -0002 2>/dev/null`.
4. Find SUID/SGID binaries: `find / -xdev -type f \( -perm -4000 -o -perm -2000 \) 2>/dev/null`.
5. Pick one SUID binary and research (via `man` or vendor docs) why it needs that bit.
6. Change a test file's permissions with `chmod` and ownership with `chown` (on a file you created, not a system file) and confirm the change with `ls -l`.

## Expected outcome
A short list of world-writable files and SUID/SGID binaries found on your lab VM, with a one-line note per item on whether it looks expected or worth flagging.

## Evidence to capture (sanitized)
- Terminal output/screenshots of the `find` commands and their results.
- Your written assessment of any binaries/files that looked unusual.

Save sanitized captures under [`../evidence/`](../evidence/README.md).
