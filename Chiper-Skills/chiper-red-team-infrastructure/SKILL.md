---
name: chiper-red-team-infrastructure
description: "Use when Building, deploying, and operating stealthy C2 infrastructure for red team engagements. Covers Mythic, Havoc, Sliver, Covenant, PoshC2, Brute Ratel, and Co"
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, red, team, infrastructure]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/red-team-infrastructure/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/red-team-infrastructure/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/red-team-infrastructure/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/red-team-infrastructure/guides
---

# Red Team Infrastructure

## Prerequisites

> 💡 Tools are auto-checked when this skill is invoked.
> Missing tools get install commands; installed tools are skipped.

**Required tools:**

- `docker` — `sudo apt install -y docker.io`

```bash
# Auto-check: only install what's missing
MISSING=""
for cmd in docker; do
  command -v "$cmd" >/dev/null 2>&1 || MISSING="$MISSING $cmd"
done
[ -z "$MISSING" ] && echo "✅ All tools ready" && exit 0
echo "⚠️  Missing:$MISSING"
command -v docker >/dev/null 2>&1 || sudo apt install -y docker.io
```

## When to Use

Red team infrastructure is the offensive platform on which adversary emulation runs: C2 frameworks, redirectors, domains, certificates, listeners, listeners, listeners — every component that lets operators control implants while evading defenders. This domain covers modern C2 platform selection (Mythic modular, Havoc C++, Sliver Go, Covenant .NET, PoshC2 PowerShell, Brute Ratel, Cobalt Strike), redirector architecture (Nginx mTLS reverse proxy, Cloudflare Workers, CDN domain fronting, AzDoors), dead-drop resolvers (GitHub gist, Telegram channels, Reddit posts), and infrastructure OPSEC (compar

## Core Tools

| Tool | Purpose |
|------|---------|
| `Mythic` | Modular C2 framework (Docker-based, agent-agnostic) |
| `Sliver` | Go-based HTTPS/DNS C2 (modern, free) |
| `Havoc` | C++ implant + Python C2 (stealthy) |
| `Covenant` | .NET C2 (Windows focus) |
| `PoshC2` | PowerShell C2 (Windows agents) |
| `Brut

## Methodology Overview

### Phase 1 — Engagement scoping

Match infrastructure complexity to target + objectives:

| Engagement type | Infrastructure | Domains | Hosting |
|-----------------|----------------|---------|---------|
| Single host test | 1 Sliver C2 + 1 redirector | 1 | 1 VPS |
| Adversary emulation (1 day) | Mythic + 2 redirectors | 2 | 2 VPS |
| Long-term red team (months) | Sliver + Mythic + 4 redirectors 

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/red-team-infrastructure/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
