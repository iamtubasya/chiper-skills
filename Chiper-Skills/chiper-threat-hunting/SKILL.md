---
name: chiper-threat-hunting
description: "Use when Proactive threat hunting — MITRE ATT&CK-mapped hunt hypotheses, Sigma detection engineering, SIEM query authoring (Splunk SPL, KQL, Lucene), and SOC workflow integr"
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, threat, hunting]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/threat-hunting/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/threat-hunting/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/threat-hunting/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/threat-hunting/guides
---

# Threat Hunting

## When to Use

Threat Hunting skill domain covering defense operations.

**Tools**: MITRE ATT&CK Navigator, MITRE CAR, Sigma, YARA, OSSEM, Sysmon, Zeek, Splunk SPL, Microsoft Sentinel KQL, Elastic Stack, MISP, OpenCTI

**Domain**: defense

**MITRE ATT&CK**: TA0040-Detection

## Core Tools

### Frameworks & Methodologies

| Framework | Purpose | Command / Usage |
|-----------|---------|-----------------|
| **MITRE ATT&CK Enterprise** | Canonical TTP taxonomy — 14 tactics, ~200 techniques, ~400 sub-techniques | Reference `T<id>` (e.g., `T1003.001`) on every hunt hypothesis |
| **MITRE A

## Methodology Overview

### Threat-Hunting Five-Phase Process

```
Phase 1            Phase 2            Phase 3            Phase 4            Phase 5
Hypothesis      →  Telemetry       →  Query           →  Triage &        →  Document &
Formation          Inventory           Authoring          Investigate         Detect
   │                  │                  │                  │                  │
   ▼                

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/threat-hunting/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
