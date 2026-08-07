---
name: chiper-security-review
description: "Use when Comprehensive security checklist and review patterns for analyzing applications, configurations, and infrastructure. This skill provides structured review methodol"
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, review]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/security-review/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/security-review/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/security-review/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/security-review/guides
---

# Security Review

## When to Use

This skill provides structured review methodology to identify vulnerabilities across OWASP Top 10 categories during penetration testing.

**Domain**: assessment

## Methodology Overview

### Security Review Checklist

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/security-review/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
