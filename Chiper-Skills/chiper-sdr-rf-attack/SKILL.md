---
name: chiper-sdr-rf-attack
description: "Use when Software Defined Radio and RF signal attacks encompass a broad range of offensive techniques targeting wireless communication systems."
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, sdr, attack]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/sdr-rf-attack/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/sdr-rf-attack/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/sdr-rf-attack/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/sdr-rf-attack/guides
---

# Sdr Rf Attack

## Prerequisites

> 💡 Missing tools? This skill will auto-check before execution.

**Required tools:**

- `gnuradio` — install: `sudo apt install -y gnuradio`
- `gqrx` — install: `sudo apt install -y gqrx-sdr`
- `hackrf` — install: `sudo apt install -y hackrf`
- `urh` — install: `sudo apt install -y urh`

**Quick check (run before using this skill):**

```bash
# Check which tools are missing
MISSING=""
for cmd in gnuradio gqrx hackrf urh; do
  command -v "$cmd" >/dev/null 2>&1 || MISSING="$MISSING $cmd"
done
if [ -n "$MISSING" ]; then
  echo "⚠️  Missing tools:$MISSING"
  echo "Install with:"
  command -v gnuradio >/dev/null 2>&1 || echo "  sudo apt install -y gnuradio"
  command -v gqrx >/dev/null 2>&1 || echo "  sudo apt install -y gqrx-sdr"
  command -v hackrf >/dev/null 2>&1 || echo "  sudo apt install -y hackrf"
  command -v urh >/dev/null 2>&1 || echo "  sudo apt install -y urh"
else
  echo "✅ All tools installed"
fi
```

## When to Use

Sdr Rf Attack skill domain covering security operations.

**Tools**: gnuradio, gr-gsm, hackrf, rtl-sdr, urh, gqrx, inspectrum

**Domain**: security

## Core Tools

| Tool | Purpose | Command Example |
|------|---------|-----------------|
| **gnuradio** | Graphical signal processing flowgraph design and execution for custom SDR applications | `gnuradio-companion` -> Drag Osmocom Source -> Demod -> File Sink -> Execute |
| **gr-gsm** | GSM network interception, 

## Methodology Overview

### Phase 1: Reconnaissance -- Spectrum Survey

1. Identify target frequency band using gqrx for real-time monitoring
2. Perform wideband spectrum scan with rtl_power to map active frequencies
3. Record signal activity patterns and timing characteristics
4. Identify modulation type and bandwidth of target signals
5. Document frequency allocations and correlate with known services

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/sdr-rf-attack/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
