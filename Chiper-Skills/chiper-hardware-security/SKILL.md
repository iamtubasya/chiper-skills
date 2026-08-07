---
name: chiper-hardware-security
description: "Use when Hardware and embedded system security testing covering physical interface exploitation, firmware extraction and analysis, side-channel attacks, RFID/NFC cloning,"
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, hardware]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/hardware-security/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/hardware-security/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/hardware-security/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/hardware-security/guides
---

# Hardware Security

## When to Use

Hardware Security skill domain covering hardware operations.

**Domain**: hardware

## Methodology Overview

### Phase 1: Physical Reconnaissance

**Goal**: Identify all external interfaces and collect device intelligence before applying probes.

- Photograph all PCB surfaces; annotate visible chip markings
- Look up FCC ID on fcc.gov to obtain internal photos, test reports, and sometimes full schematics
- Identify chip families from markings: SoC, flash chip, EEPROM, RF modules
- Map all exposed connect

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/hardware-security/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
