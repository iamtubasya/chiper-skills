---
name: chiper-patch-to-poc-pipeline
description: "Use when The end-to-end patch-diff vulnerability reproduction workflow — patch analysis (read diff, identify protective pattern, hypothesize bug class), source or bin"
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, patch, poc, pipeline]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/patch-to-poc-pipeline/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/patch-to-poc-pipeline/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/patch-to-poc-pipeline/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/patch-to-poc-pipeline/guides
---

# Patch To Poc Pipeline

## When to Use

The **patch-to-poc-pipeline** is kali-claw's workflow skill for turning a published patch diff into a working PoC plus detection coverage. It is the **pipeline itself**: the discipline of reading a diff, forming a bug-class hypothesis, walking the code path from attacker-controlled input to the patched sink, generating a trigger input (manually or via fuzzer harness), **differentially verifying** the input crashes the pre-patch binary and leaves the post-patch binary clean, and finally shipping YARA + Sigma rules that fire on the vulnerable pattern and the exploitation telemetry respectively. 

## Core Tools

### Patch Acquisition & Forensics

| Tool | Vendor / Project | Role |
|------|------------------|------|
| **git** | git project | `git diff`, `git log -p`, `git format-patch` for diff acquisition |
| **patch / git apply** | GNU / git | Apply/reverse patches during reproduction |
| **diffstat** | di

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/patch-to-poc-pipeline/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
