---
name: chiper-digital-forensics
description: "Use when Digital forensics covers the complete workflow of disk forensics, memory forensics, network forensics, file recovery/carving, and chain of custody."
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, digital, forensics]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/digital-forensics/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/digital-forensics/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/digital-forensics/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/digital-forensics/guides
---

# Digital Forensics

## Prerequisites

> 💡 Missing tools? This skill will auto-check before execution.

**Required tools:**

- `autopsy` — install: `sudo apt install -y autopsy`
- `binwalk` — install: `sudo apt install -y binwalk`
- `foremost` — install: `sudo apt install -y foremost`
- `volatility` — install: `pip install volatility3`

**Quick check (run before using this skill):**

```bash
# Check which tools are missing
MISSING=""
for cmd in autopsy binwalk foremost volatility; do
  command -v "$cmd" >/dev/null 2>&1 || MISSING="$MISSING $cmd"
done
if [ -n "$MISSING" ]; then
  echo "⚠️  Missing tools:$MISSING"
  echo "Install with:"
  command -v autopsy >/dev/null 2>&1 || echo "  sudo apt install -y autopsy"
  command -v binwalk >/dev/null 2>&1 || echo "  sudo apt install -y binwalk"
  command -v foremost >/dev/null 2>&1 || echo "  sudo apt install -y foremost"
  command -v volatility >/dev/null 2>&1 || echo "  pip install volatility3"
else
  echo "✅ All tools installed"
fi
```

## When to Use

Digital Forensics skill domain covering forensics operations.

**Tools**: autopsy, sleuth kit, volatility, wireshark/tshark, binwalk, foremost, Autopsy, SleuthKit (+2 more)

**Domain**: forensics

## Core Tools

| Tool | Purpose | Command Example |
|------|---------|-----------------|
| **autopsy** | Web-based forensics platform built on SleuthKit | `autopsy -p 8080 -d /case/evidence` |
| **sleuth kit** | Command-line filesystem forensics toolset | `mmls image.dd && fls -r -o 2048 image.dd` |
| **volatility

## Methodology Overview

### Attack Chain

```
Evidence Collection    Disk Analysis        Memory Analysis      Network Reconstruction
(Imaging/Hash/         (Partition/          (Process/Injection/  (PCAP/C2/Data
 Write-Blocking)        Filesystem/Deleted)  Rootkit)             Exfiltration)
       |                    |                     |                      |
       v                    v                     v     

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/digital-forensics/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
