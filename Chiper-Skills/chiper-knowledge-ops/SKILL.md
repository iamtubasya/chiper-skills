---
name: chiper-knowledge-ops
description: "Use when Build and maintain structured, persistent knowledge graphs across sessions. Knowledge-ops transforms ephemeral session findings into reusable intelligence — connecti"
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, knowledge, ops]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/knowledge-ops/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/knowledge-ops/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/knowledge-ops/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/knowledge-ops/guides
---

# Knowledge Ops

## When to Use

Knowledge-ops transforms ephemeral session findings into reusable intelligence — connecting entities, tracking confidence over time, and enabling recall across engagements.

**Domain**: knowledge

## Methodology Overview

### Phase 1: Capture

Extract knowledge units from session outputs:

- After codebase-onboarding: capture architecture map, security surfaces, confidence scores
- After deep-research: capture key findings, IOCs, CVEs, linked entities
- After social-intelligence: capture sentiment, key actors, timeline events
- After an exploitation attempt: capture what worked, what failed, and why

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/knowledge-ops/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
