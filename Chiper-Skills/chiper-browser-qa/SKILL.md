---
name: chiper-browser-qa
description: "Use when Automated browser-based security testing using Playwright and browser devtools. Interact with web applications as a user would — click, type, navigate — while monitorin"
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, browser]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/browser-qa/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/browser-qa/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/browser-qa/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/browser-qa/guides
---

# Browser Qa

## When to Use

Interact with web applications as a user would — click, type, navigate — while monitoring network traffic, JavaScript execution, and DOM changes for security issues.

**Domain**: testing

## Methodology Overview

1. **Baseline capture** — record clean network traffic and console logs before injecting payloads.
2. **Stateful navigation** — drive multi-step flows (login → dashboard → settings) so client-side state mirrors real users.
3. **Differential observation** — diff request/response pairs across attacker vs. victim contexts to surface authorization gaps.
4. **Evidence-first** — capture screenshots, HAR

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/browser-qa/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
