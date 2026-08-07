---
name: chiper-database-attack
description: "Use when Direct attacks against database servers at the protocol level — distinct from web-based SQL injection (covered by web-sqli). This skill targets database listeners,"
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, database, attack]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/database-attack/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/database-attack/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/database-attack/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/database-attack/guides
---

# Database Attack

## Prerequisites

> 💡 Missing tools? This skill will auto-check before execution.

**Required tools:**

- `hydra` — install: `sudo apt install -y hydra`
- `ncrack` — install: `sudo apt install -y ncrack`
- `patator` — install: `sudo apt install -y patator`

**Quick check (run before using this skill):**

```bash
# Check which tools are missing
MISSING=""
for cmd in hydra ncrack patator; do
  command -v "$cmd" >/dev/null 2>&1 || MISSING="$MISSING $cmd"
done
if [ -n "$MISSING" ]; then
  echo "⚠️  Missing tools:$MISSING"
  echo "Install with:"
  command -v hydra >/dev/null 2>&1 || echo "  sudo apt install -y hydra"
  command -v ncrack >/dev/null 2>&1 || echo "  sudo apt install -y ncrack"
  command -v patator >/dev/null 2>&1 || echo "  sudo apt install -y patator"
else
  echo "✅ All tools installed"
fi
```

## When to Use

This skill targets database listeners, authentication mechanisms, stored procedures, and protocol-level misconfigurations.

**Tools**: odat, oscanner, sqsh, redis-tools, mongoaudit, patator, ncrack, hydra

**Domain**: database

**MITRE ATT&CK**: TA0006-Credential Access

## Core Tools

| Tool | Purpose | Command Example |
|------|---------|-----------------|
| **odat** | Oracle database attack toolkit — SID guessing, credential brute-force, file read/write, OS command exec | `odat all -s 192.168.1.100 -d ORCL` |
| **oscanner** | Oracle TNS listener scanning and enumeration | `osca

## Methodology Overview

### Attack Chain

```
Recon & Discovery → Service Enumeration → Authentication Testing → Exploitation → Post-Exploitation
   (nmap/oscanner)    (odat/SID guess)     (hydra/ncrack/patator)   (odat/sqsh)     (xp_cmdshell/file ops)
```

**Phase 1: Recon and Discovery**

- Port scan common database ports: Oracle (1521), MySQL (3306), PostgreSQL (5432), MSSQL (1433), Redis (6379), MongoDB (27017)
- Ide

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/database-attack/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
