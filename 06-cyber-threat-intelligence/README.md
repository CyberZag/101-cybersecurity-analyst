# 06 Cyber Threat Intelligence

A portfolio-ready study module based on the Cyber Threat Intelligence (CTI) section of *The Complete Hands-On Cybersecurity Analyst Course*. CTI turns raw indicators into context — who's likely behind an attack, what they typically do, and how confident we are in that assessment.

## Learning objectives

By the end of this module, I can:

- Explain the difference between strategic, operational, and tactical threat intelligence.
- Use the MITRE ATT&CK framework and the Diamond Model to structure an analysis.
- Enrich a raw indicator (IP, domain, hash) with open-source threat intel sources.
- Build a basic threat-actor profile from public reporting.
- Score confidence/reliability of intelligence sources and indicators.

## Concept map

| Topic | What it does | Analyst relevance |
|---|---|---|
| CTI tiers (strategic/operational/tactical) | Different audiences/timeframes for intel | Match the intel product to the consumer (executive vs. SOC analyst) |
| MITRE ATT&CK | Catalog of adversary TTPs | Common vocabulary for describing and comparing adversary behavior |
| Diamond Model | Adversary–Capability–Infrastructure–Victim framework | Structures an intrusion analysis around four core elements |
| IOC enrichment | Adding context (geolocation, reputation, history) to a raw indicator | Turns "this IP appeared in a log" into "this IP is tied to known malicious infrastructure" |
| Source reliability/confidence scoring | Rates how trustworthy an intel source or indicator is | Prevents over-reacting to low-confidence intel |

## Key notes

### CTI tiers
Strategic intel informs executive risk decisions (long time horizon, broad trends). Operational intel supports campaign-level understanding (a specific threat actor's current activity). Tactical intel is the day-to-day IOCs and TTPs analysts use directly in detection and hunting.

### ATT&CK and the Diamond Model
ATT&CK catalogs what adversaries do (techniques); the Diamond Model frames a specific intrusion event around four connected elements — the adversary, their capability (tools/malware), the infrastructure they used, and the victim. Using both together gives a structured way to write up an incident or a threat-actor profile.

### Enrichment workflow
A raw indicator (an IP address in a log) becomes useful intel once enriched: WHOIS/geolocation, reputation score, known campaign associations, and first/last-seen dates. This is the bridge between "detection fired" and "here's what we think this actually is."

### Confidence and source reliability
Not all intel is equally trustworthy. Applying a simple reliability scale (e.g., admiralty code — source reliability A–F, information credibility 1–6) to sources and indicators keeps a CTI product honest about how confident its conclusions really are.

## Labs

See [`labs/`](./labs) for hands-on exercises:
- [`lab-01-ioc-enrichment-workflow.md`](./labs/lab-01-ioc-enrichment-workflow.md)
- [`lab-02-build-a-threat-actor-profile.md`](./labs/lab-02-build-a-threat-actor-profile.md)

## Portfolio project

See [`project/`](./project) — **Threat Intel Enrichment Workflow**, a documented process (plus optional script) for enriching a raw indicator and producing a mini threat-actor profile from public sources.

## Resources

See [`resources.md`](./resources.md) for tools and reference links.
