# Lab 01 — Deploy Wazuh and Forward Logs

**Type:** Lab Guide (home-lab VMs only)

## Objective
Deploy Wazuh on the monitoring VM (from Module 03) and start forwarding logs from the victim VM.

## Prerequisites
- The three-VM lab topology from Module 03 (victim, attacker/tools, monitoring).
- Enough RAM/disk on the monitoring VM for the Wazuh stack (check current official sizing recommendations before installing).

## Steps
1. Install Wazuh server (and its bundled Elastic/OpenSearch + dashboard components) on the monitoring VM per the official install guide.
2. Install the Wazuh agent on the victim VM and register it with the manager.
3. Confirm the agent shows "Active" in the Wazuh dashboard.
4. Generate a simple event on the victim VM (e.g., a failed login) and confirm it appears in the Wazuh dashboard within a few minutes.

## Expected outcome
A working Wazuh deployment with at least one active agent and confirmed log flow from victim VM to dashboard.

## Evidence to capture (sanitized)
- Screenshot of the Wazuh dashboard showing the active agent.
- Screenshot of the test event appearing in the dashboard.

Save sanitized captures under [`../evidence/`](../evidence/README.md).
