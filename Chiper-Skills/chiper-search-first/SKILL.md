---
name: chiper-search-first
description: "Use when Systematizes the \"search for existing tools, exploits, and techniques before writing custom ones\" workflow."
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, search, first]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/search-first/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/search-first/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/search-first/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/search-first/guides
---

# Search First

## When to Use

Search First skill domain covering workflow operations.

**Domain**: workflow

## Methodology Overview

### Search-First Decision Flow

```
┌─────────────────────────────────────────────┐
│  1. NEED ANALYSIS                           │
│     Define what capability is needed         │
│     Identify target technology/constraints   │
├─────────────────────────────────────────────┤
│  2. PARALLEL SEARCH                         │
│     ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│     │ ExploitDB│ │  GitH

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/search-first/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
