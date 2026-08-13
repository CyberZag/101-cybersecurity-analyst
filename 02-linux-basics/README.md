# 02 Linux Basics

A portfolio-ready study module based on the Linux Basics section of *The Complete Hands-On Cybersecurity Analyst Course*. It builds the command-line fluency an analyst needs to investigate Linux hosts, review permissions, and automate repetitive triage steps.

## Learning objectives

By the end of this module, I can:

- Navigate the Linux filesystem and interpret standard directory purposes (`/etc`, `/var/log`, `/home`, `/proc`, `/tmp`).
- Read and reason about file/directory permissions, ownership, and special bits (SUID/SGID/sticky).
- Use core investigative commands (`ps`, `netstat`/`ss`, `who`, `last`, `grep`, `find`, `journalctl`) to triage a host.
- Write small Bash scripts to automate a repetitive security task (log filtering, user/permission auditing).
- Explain why Linux fluency matters for SOC work — most servers, SIEM backends, and security tools run on Linux.

## Concept map

| Topic | What it does | Analyst relevance |
|---|---|---|
| Filesystem hierarchy | Standard layout of `/`, `/etc`, `/var`, `/home`, `/proc` | Know where configs, logs, and user data live during an investigation |
| Users & permissions | `rwx` bits, ownership, `chmod`/`chown`, SUID/SGID | Spot over-permissioned files, backdoored binaries, privilege-escalation paths |
| Process & network commands | `ps`, `top`, `ss`, `netstat`, `lsof` | Identify suspicious processes, listening ports, and active connections |
| Logs | `/var/log/*`, `journalctl`, `auth.log`/`secure` | Reconstruct login activity, sudo usage, and service errors |
| Shell scripting | Bash variables, loops, conditionals, piping | Automate log parsing, permission audits, and repeatable triage steps |

## Key notes

### Filesystem & navigation
Linux organizes the system under a single root (`/`). Config lives in `/etc`, logs in `/var/log`, user data in `/home`, and `/proc` exposes live kernel/process state. Knowing this layout is the fastest way to orient on an unfamiliar host during an incident.

### Permissions & ownership
Every file has an owner, group, and `rwx` bits for owner/group/others. SUID/SGID bits let a binary run with the file owner's/group's privileges — a classic privilege-escalation vector when misconfigured, so auditing world-writable files and unexpected SUID binaries is a standard hardening and IR step.

### Process & network visibility
`ps aux`, `ss -tulpn`, and `lsof -i` reveal what's running and what's listening. Comparing this against a known-good baseline is a fast way to catch a rogue process or unauthorized listener.

### Logs
`/var/log/auth.log` (Debian/Ubuntu) or `/var/log/secure` (RHEL/CentOS) records authentication and sudo events; `journalctl` queries the systemd journal. These are primary sources for reconstructing "who logged in, from where, and did what" during triage.

### Shell scripting for security tasks
Bash scripting turns one-off manual commands into repeatable checks — e.g., a script that greps auth logs for failed logins above a threshold, or audits `/etc/passwd` and SUID files on a schedule.

## Labs

See [`labs/`](./labs) for hands-on exercises:
- [`lab-01-filesystem-permissions-audit.md`](./labs/lab-01-filesystem-permissions-audit.md)
- [`lab-02-bash-log-triage-script.md`](./labs/lab-02-bash-log-triage-script.md)

## Portfolio project

See [`project/`](./project) — **Linux Security Triage Toolkit**, a small set of Bash/Python scripts that audit permissions and summarize authentication logs on a Linux host.

## Resources

See [`resources.md`](./resources.md) for tools and reference links.
