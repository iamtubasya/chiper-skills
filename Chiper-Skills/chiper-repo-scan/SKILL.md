---
name: chiper-repo-scan
description: "Use when Cross-stack source code asset audit that classifies every file, detects embedded third-party libraries, and delivers actionable verdicts per module."
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, repo, scan]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/repo-scan/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/repo-scan/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/repo-scan/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/repo-scan/guides
---

# Repo Scan

## Prerequisites

> 💡 Tools are auto-checked when this skill is invoked.
> Missing tools get install commands; installed tools are skipped.

**Required tools:**

- `file` — `sudo apt install -y file`
- `trivy` — `sudo apt install -y trivy`

```bash
# Auto-check: only install what's missing
MISSING=""
for cmd in file trivy; do
  command -v "$cmd" >/dev/null 2>&1 || MISSING="$MISSING $cmd"
done
[ -z "$MISSING" ] && echo "✅ All tools ready" && exit 0
echo "⚠️  Missing:$MISSING"
command -v file >/dev/null 2>&1 || sudo apt install -y file
command -v trivy >/dev/null 2>&1 || sudo apt install -y trivy
```

## When to Use

Repo Scan skill domain covering assessment operations.

**Domain**: assessment

## Core Tools

| Tool | Purpose | Command Example |
|------|---------|-----------------|
| semgrep | Pattern-based static analysis | `semgrep --config=auto --json .` |
| trivy | Dependency and container scanning | `trivy fs .` |
| grype | Vulnerability matching for packages | `grype dir:.` |
| trufflehog | Secret 

## Methodology Overview

### Repo Scan Four-Phase Process

**Phase 1: Surface Classification**

Enumerate and tag every file:

```bash
# Count lines of code by language
cloc --by-file . --json

# Identify file types and structure
find . -type f | sed 's/.*\.//' | sort | uniq -c | sort -rn

# Detect third-party directories
find . -type d \( -name "vendor" -o -name "node_modules" -o -name "third_party" -o -name "external" -

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/repo-scan/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
