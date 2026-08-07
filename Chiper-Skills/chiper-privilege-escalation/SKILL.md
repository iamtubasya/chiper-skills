---
name: chiper-privilege-escalation
description: "Use when Privilege escalation is the process of elevating access from a low-privileged user context (standard user, service account, or limited shell) to root on Linux"
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, privilege, escalation]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/privilege-escalation/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/privilege-escalation/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/privilege-escalation/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/privilege-escalation/guides
---

# Privilege Escalation

## When to Use

Privilege Escalation skill domain covering post exploitation operations.

**Tools**: linpeas, winpeas, linux-exploit-suggester, pspy, GTFOBins, lolbas, sudo, capsh

**Domain**: post-exploitation

**MITRE ATT&CK**: TA0004-Privilege Escalation

## Core Tools

| Tool | Purpose | Command Example |
|------|---------|-----------------|
| **linpeas** | Automated Linux privilege escalation enumeration; checks SUID, sudo, capabilities, cron, NFS, kernel, and hundreds of misconfiguration vectors | `./linpeas.sh -a 2>/dev/null \| tee linpeas.out` |
| **winpeas** 

## Methodology Overview

### Attack Chain

```
Enumeration                    Identification                 Exploitation
(linpeas, winpeas,           (sudo -l, SUID find,           (GTFOBins, kernel exploit,
 manual checks)               getcap, pspy)                  token impersonation)
      |                              |                              |
      v                              v                          

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/privilege-escalation/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
