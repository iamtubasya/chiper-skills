---
name: chiper-anti-forensics
description: "Use when Anti-forensics is the offensive counterpart to digital forensics."
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, anti, forensics]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/anti-forensics/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/anti-forensics/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/anti-forensics/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/anti-forensics/guides
---

# Anti Forensics

## Prerequisites

> 💡 Missing tools? This skill will auto-check before execution.

**Required tools:**

- `bulk_extractor` — install: `sudo apt install -y bulk-extractor`
- `steghide` — install: `sudo apt install -y steghide`

**Quick check (run before using this skill):**

```bash
# Check which tools are missing
MISSING=""
for cmd in bulk_extractor steghide; do
  command -v "$cmd" >/dev/null 2>&1 || MISSING="$MISSING $cmd"
done
if [ -n "$MISSING" ]; then
  echo "⚠️  Missing tools:$MISSING"
  echo "Install with:"
  command -v bulk_extractor >/dev/null 2>&1 || echo "  sudo apt install -y bulk-extractor"
  command -v steghide >/dev/null 2>&1 || echo "  sudo apt install -y steghide"
else
  echo "✅ All tools installed"
fi
```

## When to Use

Anti Forensics skill domain covering forensics operations.

**Tools**: shred, wipe, tcplay, logtamper, timestomp, bulk_extractor, steghide, Real-Time Logging (+6 more)

**Domain**: forensics

**MITRE ATT&CK**: TA0005-Defense Evasion

## Core Tools

| Tool | Purpose | Command Example |
|------|---------|-----------------|
| **shred** | Secure file overwrite and deletion | `shred -vfz -n 5 secret.txt` |
| **wipe** | Secure directory and file wiping | `wipe -rfci /tmp/sensitive/` |
| **tcplay** | TrueCrypt/VeraCrypt compatible encrypted volumes |

## Methodology Overview

### Attack Chain

```
Pre-Operation               Active Operations              Post-Operation
(Encrypted Volume           (Log Manipulation,             (Secure Deletion,
 Setup, Stego Prep)         Timestamp Forging)              Stego Extraction)
       |                          |                              |
       v                          v                              v
               

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/anti-forensics/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
