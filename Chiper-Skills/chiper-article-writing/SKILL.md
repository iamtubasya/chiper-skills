---
name: chiper-article-writing
description: "Use when Transform technical findings into clear, structured written content: penetration test reports, vulnerability disclosures, security blog posts, and technical docume"
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, article, writing]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/article-writing/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/article-writing/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/article-writing/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/article-writing/guides
---

# Article Writing

## When to Use

Article Writing skill domain covering knowledge operations.

**Domain**: knowledge

## Methodology Overview

### Phase 1: Gather Intelligence

```bash
# Aggregate all findings from knowledge-ops
grep -rn "type: finding" memory/*target*.md | wc -l

# Extract high-confidence findings (>= 75)
grep -rn "confidence: [789][0-9]\|confidence: 100" memory/*target*.md -l | \
  xargs grep -h "## Summary"

# Group by severity
grep -rn "tags:.*critical\|tags:.*high" memory/*target*.md
```

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/article-writing/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
