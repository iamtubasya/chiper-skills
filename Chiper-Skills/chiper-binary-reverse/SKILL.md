---
name: chiper-binary-reverse
description: "Use when Binary reverse engineering covers the complete chain from static analysis, dynamic debugging, to vulnerability discovery, exploit development, and malware analysis."
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, binary, reverse]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/binary-reverse/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/binary-reverse/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/binary-reverse/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/binary-reverse/guides
---

# Binary Reverse

## Prerequisites

> 💡 Missing tools? This skill will auto-check before execution.

**Required tools:**

- `binwalk` — install: `sudo apt install -y binwalk`
- `checksec` — install: `sudo apt install -y checksec`
- `gdb` — install: `sudo apt install -y gdb`
- `ghidra` — install: `sudo apt install -y ghidra`
- `objdump` — install: `sudo apt install -y binutils`
- `radare2` — install: `sudo apt install -y radare2`

**Quick check (run before using this skill):**

```bash
# Check which tools are missing
MISSING=""
for cmd in binwalk checksec gdb ghidra objdump radare2; do
  command -v "$cmd" >/dev/null 2>&1 || MISSING="$MISSING $cmd"
done
if [ -n "$MISSING" ]; then
  echo "⚠️  Missing tools:$MISSING"
  echo "Install with:"
  command -v binwalk >/dev/null 2>&1 || echo "  sudo apt install -y binwalk"
  command -v checksec >/dev/null 2>&1 || echo "  sudo apt install -y checksec"
  command -v gdb >/dev/null 2>&1 || echo "  sudo apt install -y gdb"
  command -v ghidra >/dev/null 2>&1 || echo "  sudo apt install -y ghidra"
  command -v objdump >/dev/null 2>&1 || echo "  sudo apt install -y binutils"
  command -v radare2 >/dev/null 2>&1 || echo "  sudo apt install -y radare2"
else
  echo "✅ All tools installed"
fi
```

## When to Use

Binary Reverse skill domain covering binary analysis operations.

**Tools**: radare2, ghidra, objdump, gdb, checksec, ROPgadget, binwalk, readelf (+2 more)

**Domain**: binary-analysis

## Core Tools

| Tool | Purpose | Command Example |
|------|---------|-----------------|
| **radare2** | Full-featured reverse engineering framework, static/dynamic analysis, script automation | `r2 -A binary && afl \|\| pdf @ main` |
| **ghidra** | NSA open-source reverse engineering platform, decompiler, GUI, he

## Methodology Overview

### Attack Chain

```
Binary ID           Static Analysis       Dynamic Analysis     Vulnerability Discovery
(file, checksec)  (r2 -A, objdump)     (gdb, r2 -d)        (pattern, fuzz)
     |                 |                 |               |
     v                 v                 v               v
Security Assessment  Exploit Dev         Shellcode          Report & Fix
(ASLR, Canary,     (ROP c

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/binary-reverse/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
