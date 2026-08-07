---
name: chiper-security-misconfiguration
description: "Use when Security misconfiguration detection (OWASP A02:2025) covering default credentials, unnecessary services, verbose errors, missing security headers, and di"
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, misconfiguration]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/security-misconfiguration/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/security-misconfiguration/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/security-misconfiguration/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/security-misconfiguration/guides
---

# Security Misconfiguration

## Prerequisites

> 💡 Missing tools? This skill will auto-check before execution.

**Required tools:**

- `nikto` — install: `sudo apt install -y nikto`
- `nmap` — install: `sudo apt install -y nmap`
- `whatweb` — install: `sudo apt install -y whatweb`

**Quick check (run before using this skill):**

```bash
# Check which tools are missing
MISSING=""
for cmd in nikto nmap whatweb; do
  command -v "$cmd" >/dev/null 2>&1 || MISSING="$MISSING $cmd"
done
if [ -n "$MISSING" ]; then
  echo "⚠️  Missing tools:$MISSING"
  echo "Install with:"
  command -v nikto >/dev/null 2>&1 || echo "  sudo apt install -y nikto"
  command -v nmap >/dev/null 2>&1 || echo "  sudo apt install -y nmap"
  command -v whatweb >/dev/null 2>&1 || echo "  sudo apt install -y whatweb"
else
  echo "✅ All tools installed"
fi
```

## When to Use

Security Misconfiguration skill domain covering defense operations.

**Tools**: Nmap, Nikto, testssl.sh, Burp Suite, WhatWeb

**Domain**: defense

**OWASP**: A02:2025-Misconfiguration

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/security-misconfiguration/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
