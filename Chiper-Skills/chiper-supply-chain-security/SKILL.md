---
name: chiper-supply-chain-security
description: "Use when Software supply chain security covering the entire lifecycle from code development to deployment: dependency vulnerabilities (known-vulnerable third-party pa"
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, supply, chain]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/supply-chain-security/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/supply-chain-security/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/supply-chain-security/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/supply-chain-security/guides
---

# Supply Chain Security

## Prerequisites

> 💡 Missing tools? This skill will auto-check before execution.

**Required tools:**

- `trivy` — install: `sudo apt install -y trivy`

**Quick check (run before using this skill):**

```bash
# Check which tools are missing
MISSING=""
for cmd in trivy; do
  command -v "$cmd" >/dev/null 2>&1 || MISSING="$MISSING $cmd"
done
if [ -n "$MISSING" ]; then
  echo "⚠️  Missing tools:$MISSING"
  echo "Install with:"
  command -v trivy >/dev/null 2>&1 || echo "  sudo apt install -y trivy"
else
  echo "✅ All tools installed"
fi
```

## When to Use

Supply Chain Security skill domain covering supply chain operations.

**Tools**: Trivy, Snyk, Dependabot, OWASP Dependency-Check, npm audit, Safety / pip-audit

**Domain**: supply-chain

**OWASP**: A08:2021-Software Integrity

## Core Tools

| Tool | Purpose | Command Example |
|------|---------|-----------------|
| **Trivy** | Comprehensive container/filesystem/Git repository vulnerability scanning with SBOM generation | `trivy fs --severity HIGH,CRITICAL ./project` |
| **Snyk** | SaaS dependency vulnerability scanning with remediation

## Methodology Overview

### Attack Chain

```
[1] Dependency Analysis   [2] Vulnerability Mapping  [3] Malicious Package Detection
  - Direct/transitive       - CVE database matching     - Typosquatting identification
    dependency enumeration  - CVSS score assessment     - post-install script auditing
  - Version range           - Exploit feasibility       - Anomalous network request
    identification            analy

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/supply-chain-security/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
