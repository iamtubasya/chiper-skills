---
name: chiper-logging-monitoring
description: "Use when Security logging and monitoring deficiencies (OWASP A09:2021) refer to applications failing to properly record security events or lacking effective monitoring,"
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, logging, monitoring]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/logging-monitoring/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/logging-monitoring/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/logging-monitoring/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/logging-monitoring/guides
---

# Logging Monitoring

## When to Use

Logging Monitoring skill domain covering defense operations.

**Tools**: ELK Stack, Splunk, Wazuh, OSSEC, auditd, Zeek

**Domain**: defense

**OWASP**: A09:2021-Logging Failures

## Core Tools

| Tool | Purpose | Command/Usage Example |
|------|---------|----------------------|
| **ELK Stack** (Elasticsearch + Logstash + Kibana) | Centralized log collection, full-text search, visual analysis | Logstash pipeline parses logs -> Elasticsearch indexes -> Kibana Dashboard displays |
| **Splunk*

## Methodology Overview

### Attack Chain

```
[1] Log Discovery           [2] Log Injection           [3] Log Evasion
  - Log storage location      - CRLF / newline injection  - Clear/modify log files
    probing                    - Forge log levels/         - Log rotation exploitation
  - Log format reversing       timestamps                - Noise injection to
  - Collection path            - Control character        

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/logging-monitoring/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
