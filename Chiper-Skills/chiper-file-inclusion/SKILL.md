---
name: chiper-file-inclusion
description: "Use when Local File Inclusion (LFI) and Remote File Inclusion (RFI) attack techniques covering path traversal, PHP wrapper abuse, log poisoning, session file inclusion, and"
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, file, inclusion]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/file-inclusion/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/file-inclusion/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/file-inclusion/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/file-inclusion/guides
---

# File Inclusion

## Prerequisites

> 💡 Missing tools? This skill will auto-check before execution.

**Required tools:**

- `ffuf` — install: `go install github.com/ffuf/ffuf/v2@latest`

**Quick check (run before using this skill):**

```bash
# Check which tools are missing
MISSING=""
for cmd in ffuf; do
  command -v "$cmd" >/dev/null 2>&1 || MISSING="$MISSING $cmd"
done
if [ -n "$MISSING" ]; then
  echo "⚠️  Missing tools:$MISSING"
  echo "Install with:"
  command -v ffuf >/dev/null 2>&1 || echo "  go install github.com/ffuf/ffuf/v2@latest"
else
  echo "✅ All tools installed"
fi
```

## When to Use

File Inclusion skill domain covering web attack operations.

**Tools**: dotdotpwn, kadimus, fimap, Burp Suite, php_filter_chain_generator, SecLists, ffuf + SecLists

**Domain**: web-attack

**OWASP**: A01:2021-Broken Access Control

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/file-inclusion/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
