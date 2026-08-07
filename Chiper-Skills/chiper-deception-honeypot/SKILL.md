---
name: chiper-deception-honeypot
description: "Use when Defensive deception and honeypot deployment covering SSH/Telnet (Cowrie), web (OpenCanary), enterprise (HFish), ICS/SCADA (Conpot), all-in-one (T-Pot), AI-drive"
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, deception, honeypot]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/deception-honeypot/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/deception-honeypot/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/deception-honeypot/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/deception-honeypot/guides
---

# Deception Honeypot

## When to Use

Deception & Honeypot skill domain covering defensive deception operations.

**Tools**: Cowrie, OpenCanary, HFish, Conpot, T-Pot, Beelzebub, Canarytokens (Thinkst), Honeyport, Glastopf, HoneyDB, Cowrie-Analyzer, MISP (for IOC sharing)

**Domain**: defense

**MITRE ATT&CK / MITRE Engage**: TA0040-Detection (deception); aligned to the MITRE Engage framework's *Prepare* (lure deployment), *Expose* (attacker interaction), *Affect* (resource burn), and *Collect* (IOC and TTP harvesting) goals.

## Core Tools

### Multi-Purpose & All-in-One

| Tool | Purpose | Deployment |
|------|---------|------------|
| **T-Pot** | All-in-one honeypot platform — bundles 20+ honeypots (Cowrie, Dionaea, Heralding, Conpot, Honeytrap, Glutton, etc.) with ElasticStack, Attack Map, and the Pottee management UI on a single ho

## Methodology Overview

### Deception Six-Phase Process

```
Phase 1              Phase 2              Phase 3              Phase 4              Phase 5              Phase 6
Architecture      →  Lure Design       →  Deployment OPSEC  →  Monitoring &       →  IOC Extraction   →  Attribution &
& Scoping            & Realism             (within scope)        Alerting             & TTP Harvesting      Sharing
   │           

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/deception-honeypot/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
