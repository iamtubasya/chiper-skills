---
name: chiper-docker-patterns
description: "Use when Setting up a practice lab for penetration testing techniques - Creating isolated environments for exploit development and testing - Building vulnerable application"
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, docker, patterns]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/docker-patterns/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/docker-patterns/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/docker-patterns/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/docker-patterns/guides
---

# Docker Patterns

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

Docker Patterns skill domain covering infrastructure operations.

**Domain**: infrastructure

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/docker-patterns/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
