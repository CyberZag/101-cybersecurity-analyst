# 101 Cybersecurity Analyst

A defensive cybersecurity learning portfolio. Projects use authorized lab material and clearly distinguish implementation, test evidence and personal learning progress.

## Working starter project

### [SOC Authentication Triage Lab](./01-soc-alert-triage-lab/)

Offline Python investigation of synthetic authentication telemetry: non-MFA failures before success, MFA-denial sequences and suspicious geo-velocity. Includes a command-line interface, schema validation, UTC normalization, JSON findings, 30 unit tests, an analyst report, draft Sentinel hunting queries and an interview learning guide.

**Validation:** the assistant ran the revised Python project on September 6, 2026: 16 synthetic rows, three findings, 30 passing tests. **AI-assisted implementation; learner reproduction pending. KQL has not been executed in a tenant.** These artifacts do not establish production incident-response experience or real-world detection accuracy.

Start with the lab README, reproduce the tests, then add your own changes and learning notes before presenting the work as personal experience.

## New investigation project

### [Phishing Evidence Lab](./02-phishing-evidence-lab/)

Offline EML parsing, source and attachment SHA-256, defanged URL extraction, explainable review rules, and an escaped HTML analyst report. Six original inert email cases include a benign partner control and an untrusted authentication-pass trap. **22 assistant-run tests passed on September 6, 2026; six cases, five requiring review, zero errors.** AI-assisted; learner reproduction pending. No real mail, network lookups, or attachment execution.

[Start the lab](./02-phishing-evidence-lab/README.md) · [Case investigation](./02-phishing-evidence-lab/docs/case-investigation.md) · [Interview exercises](./02-phishing-evidence-lab/docs/learning-guide.md)

Profile: [Zagros Saeedi on LinkedIn](https://www.linkedin.com/in/zagros-saeedi-263638257/)

## Planned study areas

Networking and Linux fundamentals; email/phishing analysis; incident response and forensics; SIEM detection tuning; vulnerability management; authorized security labs.

## Publishing standard

Every addition should include an objective, authorized scope, reproducible input, actual observed result, limitations and a reflection. Do not publish credentials, personal data, invented evidence, copyrighted course content or claims of unperformed work.

## Related work

- [Trading Account Security Monitor](https://github.com/CyberZag/trading-account-security-monitor)
- [Azure Security Labs](https://github.com/CyberZag/azure-security-labs)
- [Azure Sentinel, SOAR & Identity Defense](https://github.com/CyberZag/azure-sentinel-soar-identity-defense)
