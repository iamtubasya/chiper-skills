---
name: chiper-crypto-attacks
description: "Use when Cryptographic Attacks target implementation flaws and algorithm weaknesses in encryption systems, covering OWASP A04: Cryptographic Failures."
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, crypto, attacks]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/crypto-attacks/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/crypto-attacks/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/crypto-attacks/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/crypto-attacks/guides
---

# Crypto Attacks

## Prerequisites

> 💡 Missing tools? This skill will auto-check before execution.

**Required tools:**

- `hashcat` — install: `sudo apt install -y hashcat`
- `sslscan` — install: `sudo apt install -y sslscan`

**Quick check (run before using this skill):**

```bash
# Check which tools are missing
MISSING=""
for cmd in hashcat sslscan; do
  command -v "$cmd" >/dev/null 2>&1 || MISSING="$MISSING $cmd"
done
if [ -n "$MISSING" ]; then
  echo "⚠️  Missing tools:$MISSING"
  echo "Install with:"
  command -v hashcat >/dev/null 2>&1 || echo "  sudo apt install -y hashcat"
  command -v sslscan >/dev/null 2>&1 || echo "  sudo apt install -y sslscan"
else
  echo "✅ All tools installed"
fi
```

## When to Use

Crypto Attacks skill domain covering cryptography operations.

**Tools**: openssl, sslscan, testssl.sh, hashcat, CyberChef, padbuster, RsaCtfTool

**Domain**: cryptography

**OWASP**: A04:2021-Cryptographic Failures

## Core Tools

| Tool | Purpose | Command Example |
|------|---------|-----------------|
| **openssl** | Certificate analysis, protocol testing, encryption/decryption operations | `openssl s_client -connect target:443 -tls1` |
| **sslscan** | Quick TLS configuration scan, detect supported protocols and cipher suit

## Methodology Overview

### Attack Chain

```
[1] Crypto ID            [2] Algorithm Analysis    [3] Key/IV Attacks
  - Protocol version       - Weak algorithm detect   - Hardcoded key search
  - Cipher suite enum      - Block size/mode detect  - IV predictability
  - Hash type ID           - Key length assessment   - Key reuse detection
  - Token format parse     - Padding mode analysis   - ECB mode detection
       |  

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/crypto-attacks/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
