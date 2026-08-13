# 09 SIEM Tools

A portfolio-ready study module based on the SIEM Tools section of *The Complete Hands-On Cybersecurity Analyst Course*, covering Splunk, Elastic, and Wazuh — the platforms that turn raw logs into searchable, alertable, dashboard-visible data.

## Learning objectives

By the end of this module, I can:

- Explain the role of a SIEM in a SOC: log ingestion, normalization, correlation, alerting, dashboards.
- Deploy Wazuh (or Splunk Free/Elastic) in the home lab from Module 03 and forward logs from the victim VM.
- Write basic search queries (SPL for Splunk, Wazuh rule/query syntax) to find specific events.
- Build a simple dashboard or saved search summarizing a security-relevant metric (e.g., failed logins over time).
- Create a basic custom alert rule and test that it fires correctly.

## Concept map

| Topic | What it does | Analyst relevance |
|---|---|---|
| Log ingestion & forwarding | Agents/forwarders send logs from endpoints to the SIEM | The data pipeline every later detection depends on |
| Normalization | Standardizes fields across different log sources | Makes cross-source correlation possible |
| Search query language (SPL / Wazuh rules) | Lets an analyst query and filter ingested data | The primary day-to-day interaction with a SIEM |
| Dashboards | Visual summaries of query results over time | Fast situational awareness for a SOC shift |
| Alerting | Runs a saved search/rule on a schedule and notifies on match | Turns a query into an automated detection |

## Key notes

### Why Wazuh for a home lab
Wazuh is free/open-source and combines a SIEM-like dashboard (built on the Elastic stack) with host-based agent monitoring (file integrity, log collection, basic EDR-style telemetry) — a practical, no-cost way to get real SIEM experience in a home lab.

### Ingestion pipeline
An agent (or forwarder) on each monitored host sends logs to the SIEM; the SIEM parses/normalizes them into structured fields, making later queries far more reliable than raw-text grepping.

### Query language basics
Even a simple query — filter by host, time range, and event type — is the foundation of both alert triage (Module 04) and threat hunting (Module 05). Splunk's SPL and Wazuh's rule-based queries differ in syntax but serve the same purpose.

### Dashboards and alerts
A dashboard panel (e.g., failed logins per hour) turns a one-off query into an always-on visual. Saving that same query as a scheduled alert turns it into an automated detection — connecting directly back to Module 04's detection-engineering skills.

## Labs

See [`labs/`](./labs) for hands-on exercises:
- [`lab-01-deploy-wazuh-and-forward-logs.md`](./labs/lab-01-deploy-wazuh-and-forward-logs.md)
- [`lab-02-build-a-dashboard-and-alert.md`](./labs/lab-02-build-a-dashboard-and-alert.md)

## Portfolio project

See [`project/`](./project) — **Splunk/Wazuh Detection Lab**, a documented SIEM deployment with sample queries, a dashboard, and an alert rule tied back to Module 04's detection content.

## Resources

See [`resources.md`](./resources.md) for tools and reference links.
