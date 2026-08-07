---
name: chiper-ad-ldap-attack
description: "Use when Active Directory is the backbone of enterprise identity and access management, making it a primary target during internal network penetration tests."
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, ldap, attack]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/ad-ldap-attack/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/ad-ldap-attack/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/ad-ldap-attack/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/ad-ldap-attack/guides
---

# Ad Ldap Attack

## Prerequisites

> 💡 Tools are auto-checked when this skill is invoked.
> Missing tools get install commands; installed tools are skipped.

**Required tools:**

- `impacket` — `pip install impacket`
- `nbtscan` — `sudo apt install -y nbtscan`
- `secretsdump` — `pip install impacket`

```bash
# Auto-check: only install what's missing
MISSING=""
for cmd in impacket nbtscan secretsdump; do
  command -v "$cmd" >/dev/null 2>&1 || MISSING="$MISSING $cmd"
done
[ -z "$MISSING" ] && echo "✅ All tools ready" && exit 0
echo "⚠️  Missing:$MISSING"
command -v impacket >/dev/null 2>&1 || pip install impacket
command -v nbtscan >/dev/null 2>&1 || sudo apt install -y nbtscan
command -v secretsdump >/dev/null 2>&1 || pip install impacket
```

## When to Use

Ad Ldap Attack skill domain covering enterprise operations.

**Domain**: enterprise

**MITRE ATT&CK**: TA0006-Credential Access

## Core Tools

| Tool | Category | Purpose |
|------|----------|---------|
| impacket-secretsdump.py | Credential Harvesting | Extract hashes from NTDS.dit, perform DCSync attacks, dump SAM/SYSTEM |
| impacket-psexec.py | Lateral Movement | Execute commands via SMB using Pass-the-Hash or credential authentication 

## Methodology Overview

### Phase 1: Reconnaissance

Discover live hosts, identify domain controllers, map network topology, and gather NetBIOS/DNS information about the target domain.

1. Scan the target network for live hosts and open ports (88/Kerberos, 389/LDAP, 445/SMB, 636/LDAPS, 135/RPC)
2. Use `nbtscan` for NetBIOS discovery to identify domain names and machine roles
3. Perform DNS enumeration to locate domain co

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/ad-ldap-attack/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
