# Documented SOC Home Lab

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

**Status:** Scaffold — labs not yet completed. This README will be filled in against the [project readiness checklist](../../CHECKLIST.md) once the lab is actually built and documented.

A written and diagrammed record of the isolated home-lab environment (network topology, VM roles, IP plan) that underpins every hands-on module in this course — presented as infrastructure/documentation evidence for a portfolio.

## Problem Statement

*(mandatory — fill in after completing the labs)*

- **What problem does this solve?** Recruiters and hiring managers want proof of hands-on lab experience, not just course completion — a documented, reproducible lab shows real infrastructure skills.
- **Who is this for?** Aspiring SOC analysts building a home lab; anyone reviewing this portfolio to assess hands-on capability.
- **Why does it matter?** A safely isolated, well-documented lab is the foundation every later detection/IR/forensics project depends on.

## Technical Implementation

*(mandatory — fill in with real details once the lab is built)*

- **Architecture:** Hypervisor → isolated internal network → victim VM / attacker-tools VM / monitoring VM, each with a static IP on the lab subnet.
- **Tech stack rationale:** VMware/VirtualBox chosen for free/low-cost local virtualization without cloud costs.
- **Core design:** Network isolation as the primary safety control; snapshotting for safe repeatable testing.
- **Design decisions & trade-offs:** Host-only/internal networking chosen over bridged to guarantee no accidental exposure to the home network.

## Demo Instructions

*(mandatory — fill in once the lab is finalized)*

1. Review the network diagram and IP addressing table in `docs/`.
2. Follow the setup steps to reproduce the lab on your own hypervisor.
3. Verify connectivity between VMs and isolation from the home network.

## Results / Impact

*To be filled in once the lab is fully built and validated.*

## Tech Stack

| Layer | Tools |
|---|---|
| Hypervisor | VMware Workstation/Player or VirtualBox |
| Guest OSes | Lightweight Linux (victim), Kali (attacker/tools), Linux server (monitoring placeholder) |
| Networking | Host-only / internal virtual network |

## Disclaimer

This lab is for personal, authorized, isolated home-lab use only. No production systems or third-party networks are involved.

## License

Distributed under the [MIT License](../../LICENSE).
