---
name: chiper-ai-security
description: "Use when Semantic-layer attack testing against AI systems and LLM-integrated applications."
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/ai-security/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/ai-security/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/ai-security/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/ai-security/guides
---

# Ai Security

## Prerequisites

> 💡 Missing tools? This skill will auto-check before execution.

**Required tools:**

- `burpsuite` — install: `echo "Download: https://portswigger.net/burp/communitydownload"`
- `ffuf` — install: `go install github.com/ffuf/ffuf/v2@latest`
- `garak` — install: `pip install garak`

**Quick check (run before using this skill):**

```bash
# Check which tools are missing
MISSING=""
for cmd in burpsuite ffuf garak; do
  command -v "$cmd" >/dev/null 2>&1 || MISSING="$MISSING $cmd"
done
if [ -n "$MISSING" ]; then
  echo "⚠️  Missing tools:$MISSING"
  echo "Install with:"
  command -v burpsuite >/dev/null 2>&1 || echo "  echo "Download: https://portswigger.net/burp/communitydownload""
  command -v ffuf >/dev/null 2>&1 || echo "  go install github.com/ffuf/ffuf/v2@latest"
  command -v garak >/dev/null 2>&1 || echo "  pip install garak"
else
  echo "✅ All tools installed"
fi
```

## When to Use

Ai Security skill domain covering ai operations.

**Tools**: garak, promptfoo, llm-guard, picklescan, ffuf, burpsuite, Custom Python, Burp Suite

**Domain**: ai

## Methodology Overview

### Attack Surface Mapping

Before testing, enumerate all AI integration points in the target:

| Surface | Examples | Injection Vector |
|---------|---------|-----------------|
| API Endpoints | `/v1/chat/completions`, `/api/ask` | `messages[].content`, `system` parameter |
| Chat Interfaces | Web chatbots, Slack bots, embedded widgets | User message field |
| Document Processors | PDF summarizer

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/ai-security/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
