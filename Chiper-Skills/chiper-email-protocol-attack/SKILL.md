---
name: chiper-email-protocol-attack
description: "Use when Email protocol attacks targeting mail infrastructure at the protocol level."
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, email, protocol, attack]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/email-protocol-attack/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/email-protocol-attack/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/email-protocol-attack/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/email-protocol-attack/guides
---

# Email Protocol Attack

## Prerequisites

> 💡 Tools are auto-checked when this skill is invoked.
> Missing tools get install commands; installed tools are skipped.

**Required tools:**

- `dig` — `sudo apt install -y dnsutils`

```bash
# Auto-check: only install what's missing
MISSING=""
for cmd in dig; do
  command -v "$cmd" >/dev/null 2>&1 || MISSING="$MISSING $cmd"
done
[ -z "$MISSING" ] && echo "✅ All tools ready" && exit 0
echo "⚠️  Missing:$MISSING"
command -v dig >/dev/null 2>&1 || sudo apt install -y dnsutils
```

## When to Use

Email Protocol Attack skill domain covering network attack operations.

**Tools**: smtp-user-enum, swaks, sendemail, nailgun, smtpmap, mutt, openssl

**Domain**: network-attack

**MITRE ATT&CK**: T1114-Email Collection

## Core Tools

| Tool | Purpose | Command Example |
|------|---------|-----------------|
| **smtp-user-enum** | SMTP user enumeration via VRFY/EXPN/RCPT | `smtp-user-enum -M VRFY -U users.txt -t 10.0.0.1` |
| **swaks** | Swiss Army Knife for SMTP testing, email forgery | `swaks --to victim@target.com --from spoofe

## Methodology Overview

### Attack Chain

```
Reconnaissance → Enumeration → Authentication Testing → Forgery/Phishing → Mailbox Access → Data Exfiltration
```

**1. Reconnaissance (Information Gathering)**
- Identify mail server via DNS MX records: `dig MX target.com`
- Banner grabbing: `nc mail.target.com 25`
- Software fingerprinting with smtpmap
- TLS configuration assessment

**2. Enumeration (User Discovery)**
- SM

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/email-protocol-attack/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
