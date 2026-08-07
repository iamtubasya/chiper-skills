---
name: chiper-chronicle
description: "Use when A system for recording, indexing, and distilling knowledge from agent lifecycle events. Through a three-layer document system (overview -> detailed records -> knowledge"
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, chronicle]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/chronicle/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/chronicle/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/chronicle/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/chronicle/guides
---

# Chronicle

## When to Use

Through a three-layer document system (overview -> detailed records -> knowledge distillation), raw conversation events are transformed into reusable experience.

**Tools**: MEMORY.md, HEARTBEAT.md, TOOLS.md, skills/

**Domain**: knowledge

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/chronicle/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
