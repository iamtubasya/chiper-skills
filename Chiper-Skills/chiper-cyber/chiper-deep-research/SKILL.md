---
name: chiper-deep-research
description: "Use when Multi-source intelligence gathering through systematic web research — producing thorough, cited reports from diverse sources."
version: "0.2.0"
author: ChiperFlux (Chiper-Cyber)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, chiper-cyber, deep, research]
references:
  - path: ~/.hermes/skills/chiper-cyber/chiper-deep-research/SKILL.md
  - path: ~/.hermes/skills/chiper-cyber/chiper-deep-research/payloads.md
  - path: ~/.hermes/skills/chiper-cyber/chiper-deep-research/test-cases.md
  - path: ~/.hermes/skills/chiper-cyber/chiper-deep-research/guides
---

# Deep Research

## Prerequisites

> 💡 Tools are auto-checked when this skill is invoked.
> Missing tools get install commands; installed tools are skipped.

**Required tools:**

- `shodan` — `pip install shodan`

```bash
# Auto-check: only install what's missing
MISSING=""
for cmd in shodan; do
  command -v "$cmd" >/dev/null 2>&1 || MISSING="$MISSING $cmd"
done
[ -z "$MISSING" ] && echo "✅ All tools ready" && exit 0
echo "⚠️  Missing:$MISSING"
command -v shodan >/dev/null 2>&1 || pip install shodan
```

## When to Use

Deep Research skill domain covering research operations.

**Domain**: research

## Core Tools

### Search Engines & Aggregators

| Tool | Purpose | Command Example |
|------|---------|-----------------|
| Google Dorking | Precision search with operators | `site:github.com "password" filetype:env` |
| Shodan | Internet-facing device search | `shodan search "apache 2.4.49"` |
| Censys | Host an

## Methodology Overview

### Deep Research Six-Phase Process

**Phase 1: Define Research Scope**

Clarify the research goal and decompose into 3-5 specific sub-questions.

```
Topic: "Security of Kubernetes ingress controllers"
Sub-questions:
  1. What CVEs have been disclosed for popular ingress controllers?
  2. What misconfiguration patterns lead to compromise?
  3. What are the current best practices for hardening?
  

## Instructions

Read the referenced chiper-cyber files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `~/.hermes/skills/chiper-cyber/chiper-deep-research/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: chiper-cyber v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/chiper-cyber && git pull`
