# 05 Threat Hunting

A portfolio-ready study module based on the Threat Hunting section of *The Complete Hands-On Cybersecurity Analyst Course*. Threat hunting is proactive: instead of waiting for an alert, the analyst forms a hypothesis and goes looking for evidence that it's true.

## Learning objectives

By the end of this module, I can:

- Explain the difference between reactive alert triage and proactive threat hunting.
- Form a testable hypothesis based on a known TTP (e.g., from MITRE ATT&CK) or threat-intel report.
- Use SIEM-style queries to search for evidence supporting or refuting a hypothesis.
- Identify and document IOCs (Indicators of Compromise) and TTPs (Tactics, Techniques, Procedures) found during a hunt.
- Write a hunt report that documents hypothesis, method, findings, and next steps — even when the finding is "no evidence found."

## Concept map

| Topic | What it does | Analyst relevance |
|---|---|---|
| Hypothesis-driven hunting | Starts from "if attacker technique X was used, what evidence would exist?" | Structures a hunt so it's falsifiable and reproducible |
| MITRE ATT&CK | Catalog of adversary tactics/techniques/procedures | Common vocabulary for choosing what to hunt for |
| IOCs vs. TTPs | IOC = specific artifact (hash, IP, domain); TTP = behavior pattern | TTP-based hunts survive IOC rotation and generalize better |
| SIEM search/pivoting | Querying and pivoting across log sources | The mechanical "how" of a hunt |
| Hunt reporting | Documents hypothesis, method, findings, recommendation | Makes hunts auditable and repeatable, even negative results |

## Key notes

### Reactive vs. proactive
Alert triage (Module 04) responds to what a detection rule already caught. Threat hunting assumes some techniques evade existing detections and searches for evidence directly — closing detection gaps rather than waiting for them to fire.

### Building a hypothesis
A good hunt hypothesis references a specific ATT&CK technique (e.g., T1059 — Command and Scripting Interpreter) and predicts what telemetry would exist if that technique were used in this environment, then searches for exactly that.

### IOCs vs. TTPs
An IOC (a specific hash, IP, or domain) is brittle — attackers rotate infrastructure constantly. A TTP (a behavior pattern, like "encoded PowerShell spawned from an Office process") is far more durable and is the preferred basis for a repeatable hunt.

### Documenting negative results
A hunt that finds no evidence of the hypothesized technique is still valuable — it demonstrates coverage and can be repeated on a schedule. Hunt reports should always be written, not just for confirmed findings.

## Labs

See [`labs/`](./labs) for hands-on exercises:
- [`lab-01-build-a-hunt-hypothesis.md`](./labs/lab-01-build-a-hunt-hypothesis.md)
- [`lab-02-execute-and-document-the-hunt.md`](./labs/lab-02-execute-and-document-the-hunt.md)

## Portfolio project

See [`project/`](./project) — **Threat Hunting Playbooks**, a small set of ATT&CK-mapped hunt playbooks with hypotheses, queries, and a sample findings write-up.

## Resources

See [`resources.md`](./resources.md) for tools and reference links.
