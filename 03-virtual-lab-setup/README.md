# 03 Virtual Lab Setup

A portfolio-ready study module based on the Virtual Lab Environments section of *The Complete Hands-On Cybersecurity Analyst Course*. This module builds the self-contained, isolated lab that every later module's labs and projects run inside — segmented networking, a SOC-style monitoring VM, and safe attacker/victim VMs.

## Learning objectives

By the end of this module, I can:

- Install and configure a hypervisor (VMware Workstation/Player or VirtualBox) for nested lab use.
- Design a segmented lab network (isolated/host-only vs. NAT vs. bridged) so lab traffic never touches a production or home network unintentionally.
- Stand up a minimal SOC home lab: a victim VM, an attacker/tools VM, and a monitoring VM (e.g., for Wazuh/Splunk later).
- Explain the safety rationale for network isolation before running any offensive tooling.

## Concept map

| Topic | What it does | Analyst relevance |
|---|---|---|
| Hypervisor | Runs multiple isolated VMs on one host | Foundation for every hands-on lab in this course |
| Network modes (NAT / host-only / bridged / internal) | Controls what a VM can reach | Prevents lab traffic (malware, scans, exploits) from leaking to production/home networks |
| Segmentation | Separates victim, attacker, and monitoring VMs into their own subnet | Mirrors real SOC network zoning and blast-radius containment |
| Snapshots | Point-in-time VM state save/restore | Safely reset a VM after running malware or an exploit |
| Monitoring VM | A dedicated VM to host SIEM/EDR tooling (later modules) | Central place to collect logs/alerts from the rest of the lab |

## Key notes

### Choosing a hypervisor
VMware Workstation/Player and VirtualBox are the two most common free/low-cost options for a home lab; either works for this course. Enabling nested virtualization (if running the hypervisor inside another VM/cloud instance) is worth checking early to avoid surprises later.

### Network isolation is the safety control
Before running anything resembling malware, an exploit, or a scanner, the lab network should be set to an isolated/host-only or internal network mode with no route to the home network or internet unless explicitly required (e.g., downloading a tool). This is the single most important habit from this module.

### Lab topology
A minimal SOC home lab typically includes: one victim VM (Windows or Linux), one attacker/tools VM (e.g., Kali), and one monitoring VM (destined for Wazuh/Splunk in Module 09). All three sit on the same isolated internal network/subnet.

### Snapshots as a safety net
Taking a snapshot before running anything risky (malware detonation, exploit testing) lets you revert instantly instead of rebuilding a VM from scratch.

## Labs

See [`labs/`](./labs) for hands-on exercises:
- [`lab-01-hypervisor-and-network-setup.md`](./labs/lab-01-hypervisor-and-network-setup.md)
- [`lab-02-three-vm-soc-topology.md`](./labs/lab-02-three-vm-soc-topology.md)

## Portfolio project

See [`project/`](./project) — **Documented SOC Home Lab**, a written/diagrammed record of the lab topology used for the rest of this course, suitable as portfolio evidence of infrastructure setup skills.

## Resources

See [`resources.md`](./resources.md) for tools and reference links.
