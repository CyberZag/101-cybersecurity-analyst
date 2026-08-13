# Lab 02 — Three-VM SOC Topology

**Type:** Lab Guide (personal/home-lab hardware only)

## Objective
Stand up the minimal three-VM topology (victim, attacker/tools, monitoring) that later modules will build on.

## Prerequisites
- Completed Lab 01 (isolated network ready).
- ISOs/images for a lightweight Linux victim VM, a Kali (or similar) attacker/tools VM, and a placeholder monitoring VM (can be a minimal Linux server for now — Wazuh install comes in Module 09).

## Steps
1. Deploy the victim VM on the isolated network from Lab 01; assign it a static IP within the lab subnet.
2. Deploy the attacker/tools VM on the same network with its own static IP.
3. Deploy the monitoring VM placeholder on the same network.
4. Verify all three VMs can reach each other (e.g., ping between them) but not the home network.
5. Document the topology: IP addressing plan, VM roles, and hypervisor network settings.
6. Take a clean snapshot of each VM now, before any later module modifies them.

## Expected outcome
Three VMs on one isolated subnet, each reachable from the others, documented with an IP addressing table and a simple network diagram.

## Evidence to capture (sanitized)
- A network diagram (hand-drawn or tool-generated) showing the three VMs and subnet.
- Screenshot of successful ping/connectivity tests between VMs.

Save sanitized captures under [`../evidence/`](../evidence/README.md).
