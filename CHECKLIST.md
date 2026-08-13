# GitHub Portfolio — Project Readiness Checklist

Use this checklist before adding any project to your portfolio or sharing a repo link with a recruiter. A project is "recruiter-ready" only when every box below is checked.

---

## 1. Documentation (mandatory)

- [ ] **Problem Statement** section exists and answers: What real problem does this solve? Who is it for? Why does it matter (e.g., a SOC pain point, a detection gap, a trading inefficiency)?
- [ ] **Technical Implementation** section exists and covers: architecture/data flow diagram or description, tech stack and why it was chosen, key algorithms or detection logic, notable design decisions and trade-offs.
- [ ] **Demo Instructions** section exists and covers: exact setup steps from a clean machine, sample input/data (or how to generate it), expected output/screenshot/GIF, a live demo link or short video if applicable.
- [ ] README follows the standardized template (see `README_TEMPLATE.md`).
- [ ] All documentation is free of spelling/grammar errors and broken links.
- [ ] Screenshots, diagrams, or terminal recordings are included where relevant (network diagrams, dashboard views, packet captures, backtest equity curves, etc.).

## 2. Code Quality

- [ ] Code passes linting with zero errors (flake8/pylint for Python, ESLint for JS, etc.).
- [ ] Consistent formatting applied (black/autopep8, or Prettier).
- [ ] No hardcoded secrets, API keys, credentials, or internal hostnames — checked with a secret scanner (e.g., `gitleaks`, `truffleHog`) before every push.
- [ ] `.gitignore` excludes venvs, `__pycache__`, `.env`, IDE config, captured pcap/log samples with sensitive data.
- [ ] Functions and modules have docstrings/comments explaining non-obvious logic (e.g., detection heuristics, trading signal math).
- [ ] No dead code, commented-out blocks, or leftover debug prints.

## 3. Testing & CI/CD (mandatory)

- [ ] Automated tests exist for core logic (unit tests minimum; integration tests where feasible — e.g., mock EDR/Splunk API responses, mock market data feeds).
- [ ] Test coverage is measured and reported (target: 70%+ for core logic).
- [ ] GitHub Actions workflow runs lint + tests + coverage on every push/PR (see `.github/workflows/ci.yml`).
- [ ] CI badge is added to the top of the README and shows passing status.
- [ ] Coverage badge/report is visible (Codecov, Coveralls, or workflow-generated summary).
- [ ] Build/CI is green on the default branch before sharing the link.

## 4. Repository Hygiene

- [ ] Descriptive repo name (avoid `test-repo`, `project1`, `misc-scripts`).
- [ ] One-line repo description + topics/tags set on GitHub (e.g., `cybersecurity`, `soc`, `siem`, `python`, `algo-trading`).
- [ ] License file present (MIT/Apache-2.0 unless there's a reason otherwise).
- [ ] `requirements.txt` / `pyproject.toml` / `package.json` pinned and installable from a clean environment.
- [ ] No large binary artifacts committed (pcaps, datasets, model weights) — use Git LFS or link externally instead.
- [ ] Commit history is reasonably clean (no `wip`, `asdf`, `fix fix fix` spam on main) — squash if needed before showcasing.
- [ ] Default branch is `main`, protected if collaborators exist.

## 5. Security-Specific Checks (given the domain)

- [ ] Any included packet captures, logs, or datasets are sanitized/synthetic — no real IPs, credentials, or PII from actual employer systems.
- [ ] If the tool interacts with live systems (scanners, EDR APIs, trading APIs), README clearly states it's for lab/sandbox use and includes a safety/ethics disclaimer.
- [ ] Dependencies are checked for known CVEs (`pip-audit`, `npm audit`, or Dependabot enabled on the repo).
- [ ] If simulating attacks/exploits (HackTheBox/TryHackMe-style tooling), README states the tool is for authorized testing only.

## 6. Recruiter-Facing Polish

- [ ] Pinned on your GitHub profile if it's a top-3 project.
- [ ] Linked from your resume/LinkedIn with a one-line impact statement (e.g., "Reduced false-positive alert triage time by X% using...").
- [ ] Demo video or GIF under ~60 seconds embedded near the top of the README — recruiters skim, they rarely clone and run code.
- [ ] Quantified results where possible (detection accuracy, backtest Sharpe ratio, alerts processed/sec, false-positive rate reduction).

---

### How to use this checklist

1. Copy this file into each portfolio repo as `CHECKLIST.md`, or keep a master copy and re-run it before every "share with recruiter" moment.
2. Pair it with `README_TEMPLATE.md` for the documentation structure and `.github/workflows/ci.yml` for automated linting + coverage enforcement.
3. Treat unchecked boxes as blockers — do not link the repo on your resume until the checklist is fully green.
