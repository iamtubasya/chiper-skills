---
name: chiper-physical-security-testing
description: "Use when Physical penetration testing covering mechanical lock bypass (pin-tubular/wafer), RFID/NFC badge cloning (Proxmark3/ESP-RFID-Tool/Walrus), HID iCLASS/Mif"
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, physical, testing]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/physical-security-testing/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/physical-security-testing/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/physical-security-testing/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/physical-security-testing/guides
---

# Physical Security Testing

## When to Use

Physical security testing covers the on-site operations that gain physical access to a target facility — lock picking, badge cloning, drop-box deployment, USB-weapon delivery, hidden-camera placement, and the social engineering that gets a human through the door. This skill is the physical-access complement to radio and firmware skills: where `bluetooth-rfid-nfc` analyzes the wireless protocol and `hardware-security` analyzes chips and firmware, this skill asks "how do I get *through the door*?"

**Tools**: Proxmark3, ESP-RFID-Tool, Walrus, Hak5 LAN Turtle, Hak5 Packet Squirrel, USB Rubber Duc

## Core Tools

### Lock Bypass & Mechanical

| Tool | Purpose | Notes |
|------|---------|-------|
| **Lock pick set** (Peterson, SouthOrd, Sparrows) | Pin-tumbler picking with hooks, rakes, and tension wrenches | Standard 0.025" or 0.018" thickness; transparent practice locks first, then progressively harder belt

## Methodology Overview

### On-Site Engagement Six-Phase Process

```
Phase 1            Phase 2          Phase 3              Phase 4          Phase 5            Phase 6
Scope & Legal  →   Pre-Engagement →  Entry Vector      →  Execution &   →  On-Site Ops &   →  Exit &
                   Recon            Selection              Access           Persistence          Evidence
   │                  │                  │    

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/physical-security-testing/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
