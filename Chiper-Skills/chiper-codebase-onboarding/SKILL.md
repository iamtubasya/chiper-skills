---
name: chiper-codebase-onboarding
description: "Use when Rapidly acquire a mental model of any unfamiliar codebase — from a 500-line script to a 100M+ line monorepo. This skill transforms raw code into structured int"
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, codebase, onboarding]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/codebase-onboarding/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/codebase-onboarding/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/codebase-onboarding/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/codebase-onboarding/guides
---

# Codebase Onboarding

## When to Use

This skill transforms raw code into structured intelligence: architecture maps, entry points, data flows, security surfaces, and onboarding confidence scores.

**Domain**: knowledge

## Methodology Overview

### Phase 1: Orientation

- Count files, LOC, and language distribution
- Identify primary language(s) and detect framework
- Map top-level directory structure to functional areas
- Find entry points and main execution paths

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/codebase-onboarding/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
