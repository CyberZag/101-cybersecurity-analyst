# 10 Incident Response

A portfolio-ready study module based on the Incident Response section of *The Complete Hands-On Cybersecurity Analyst Course*. This module ties together everything from earlier modules — networking, Linux, EDR/SIEM telemetry, threat intel — into the structured lifecycle used to handle a real security incident.

## Learning objectives

By the end of this module, I can:

- Explain the IR lifecycle: Preparation → Detection → Containment → Investigation → Mitigation/Eradication → Recovery → Lessons Learned.
- Scope an incident: what's affected, what evidence exists, what containment actions are appropriate.
- Build an incident timeline from multiple log sources (EDR, SIEM, auth logs).
- Recommend and justify containment/mitigation actions given a stated scenario.
- Write a final incident report suitable for both technical and management audiences.

## Concept map

| Topic | What it does | Analyst relevance |
|---|---|---|
| IR lifecycle | Structured phases from preparation through lessons learned | Keeps a chaotic incident response organized and auditable |
| Scoping | Determines what's actually affected | Prevents both under- and over-reacting to an incident |
| Timeline reconstruction | Orders events chronologically across sources | The backbone of any incident report |
| Containment | Short-term action to stop the spread | Must balance speed against evidence preservation |
| Incident reporting | Documents what happened, what was done, and lessons learned | The final deliverable stakeholders actually read |

## Key notes

### The IR lifecycle
A widely used model (NIST SP 800-61) frames IR as Preparation, Detection & Analysis, Containment/Eradication/Recovery, and Post-Incident Activity. Every later step depends on solid scoping and evidence handling from the earlier ones.

### Scoping and evidence handling
Before containing anything, an analyst should establish what hosts/accounts/data are actually affected, based on the available telemetry (this is where Modules 04, 05, 09, and 11 all feed in). Evidence (logs, memory captures, disk images) should be preserved before containment actions might alter or destroy it.

### Building a timeline
A timeline that merges EDR process events, SIEM alerts, and authentication logs into one chronological view is often the single most useful artifact in an investigation — it turns scattered data points into a coherent story.

### Containment vs. investigation trade-offs
Isolating a host stops further spread but can also tip off an attacker or destroy volatile evidence (e.g., an active network connection) if done carelessly. IR plans should document the reasoning behind each containment decision.

### Reporting for two audiences
A good incident report includes both a technical narrative (for other analysts) and an executive summary (for leadership) — what happened, impact, and what's being done to prevent recurrence.

## Labs

See [`labs/`](./labs) for hands-on exercises:
- [`lab-01-simulated-incident-scoping.md`](./labs/lab-01-simulated-incident-scoping.md)
- [`lab-02-timeline-and-final-report.md`](./labs/lab-02-timeline-and-final-report.md)

## Portfolio project

See [`project/`](./project) — **Incident Response Case Study**, an end-to-end simulated IR case with a scoping note, timeline, containment plan, and final report.

## Resources

See [`resources.md`](./resources.md) for tools and reference links.
