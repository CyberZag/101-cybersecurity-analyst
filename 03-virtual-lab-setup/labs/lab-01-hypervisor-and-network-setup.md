# Lab 01 — Hypervisor & Network Setup

**Type:** Lab Guide (personal/home-lab hardware only)

## Objective
Install a hypervisor and configure an isolated virtual network that the rest of the course labs will run on.

## Prerequisites
- A host machine with virtualization support enabled in BIOS/UEFI and enough RAM/disk for multiple VMs (8GB+ RAM recommended for 2-3 lightweight VMs).
- Installer for VMware Workstation/Player or VirtualBox.

## Steps
1. Install your chosen hypervisor.
2. Create a new isolated/host-only (or "internal") virtual network — do not use bridged mode for this lab network.
3. Document the network's subnet (e.g., 192.168.56.0/24) and confirm it has no route to your home network or the internet unless you intentionally add one.
4. Create one throwaway test VM, attach it to the isolated network, and confirm it can reach other VMs on the same network but not your home LAN.
5. Take a clean snapshot of the test VM once configured.

## Expected outcome
A working hypervisor with one isolated internal network defined, verified to be cut off from your home network, plus a documented subnet.

## Evidence to capture (sanitized)
- Screenshot of the virtual network configuration (subnet, mode).
- Screenshot confirming isolation (e.g., a failed ping to your home router's IP from the lab VM).

Save sanitized captures under [`../evidence/`](../evidence/README.md).
