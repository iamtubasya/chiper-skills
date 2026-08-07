---
name: chiper-api-security
description: "Use when API Security Testing covers security assessment across three major API architectures: REST, GraphQL, and gRPC, focusing on the OWASP API Security Top 10 core risks: B"
version: "0.2.0"
author: ChiperFlux (Chiper-Cyber)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, chiper-cyber, api]
references:
  - path: ~/.hermes/skills/chiper-cyber/chiper-api-security/SKILL.md
  - path: ~/.hermes/skills/chiper-cyber/chiper-api-security/payloads.md
  - path: ~/.hermes/skills/chiper-cyber/chiper-api-security/test-cases.md
  - path: ~/.hermes/skills/chiper-cyber/chiper-api-security/guides
---

# Api Security

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

Api Security skill domain covering web attack operations.

**Tools**: Burp Suite, Postman, ffuf, GraphQLMap, kiterunner

**Domain**: web-attack

**OWASP**: API Security Top 10

## Core Tools

| Tool | Purpose | Command Example |
|------|---------|-----------------|
| **Burp Suite** | API proxy interception, authorization testing, Intruder brute force enumeration, response comparison analysis | Proxy intercept API request -> Autorize plugin test BOLA -> Comparer compare responses for diff

## Methodology Overview

### Attack Chain

```
[1] API Discovery        [2] Authentication     [3] Authorization
  - Endpoint enumeration   - JWT security analysis      - BOLA testing (IDOR)
    (kiterunner)            - API key leakage detection  - BPLA property tampering
  - Swagger/OpenAPI leak   - OAuth flow audit           - Permission matrix verification
  - GraphQL Introspection  - Authentication bypass      - Hori

## Instructions

Read the referenced chiper-cyber files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `~/.hermes/skills/chiper-cyber/chiper-api-security/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: chiper-cyber v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/chiper-cyber && git pull`
