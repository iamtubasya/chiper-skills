---
name: chiper-kali-memory
description: "Use when Needing chiper-cyber long-term knowledge: decisions, lessons, milestones."
version: "0.2.0"
author: ChiperFlux (Chiper-Cyber)
metadata:
  hermes:
    tags: [chiper-cyber, memory, knowledge, lessons-learned, history, pentest]
references:
  - path: /home/chiper/.hermes/chiper-cyber/MEMORY.md
  - path: /home/chiper/.hermes/chiper-cyber/memory/2026-05-05-deep-research-migration-report.md
---

# chiper-cyber Long-term Memory

## Prerequisites

> 💡 Tools are auto-checked when this skill is invoked.
> Missing tools get install commands; installed tools are skipped.

**Required tools:**

- `radare2` — `sudo apt install -y radare2`

```bash
# Auto-check: only install what's missing
MISSING=""
for cmd in radare2; do
  command -v "$cmd" >/dev/null 2>&1 || MISSING="$MISSING $cmd"
done
[ -z "$MISSING" ] && echo "✅ All tools ready" && exit 0
echo "⚠️  Missing:$MISSING"
command -v radare2 >/dev/null 2>&1 || sudo apt install -y radare2
```

## When to Use

When needing distilled operational knowledge: key decisions, lessons learned, project milestones, accumulated expertise.

## Instructions

- **MEMORY.md** — Carefully selected long-term knowledge (v1.0.0, updated 2026-07-26)
- **memory/2026-05-05-deep-research-migration-report.md** — Deep research capability migration analysis

## Memory (Current Status)

# MEMORY.md - Long-term Memory

_Carefully selected distilled knowledge. Like human long-term memory — not raw logs, but the essence of experience._

**Last Updated**: 2026-07-26 (v1.0.0)

---

## Current Status

- **Project Phase**: Phase 1 SKILL Library Enhancement — Task 1.2 Phase 2 in progress (20/100 standard SKILLs)
- **Tools Mastered**: 518/518 (100%) Kali Linux tools
- **Skill Domains**: **130** (15 P0/P1 at v1.0.0 Defense Triple standard + 20 Phase 2 standardized + 95 pending)
- **Uptime**: ~19 weeks (since 2026-03-14 launch)
- **Current Focus**: Phase 2 standardization (10 batches × 10 SKILLs), Task 1.3 new SKILL creation (7 candidates), Defense Triple rollout
- **Strategic Positioning**: chiper-cyber as dedicated SKILL library maintainer (v1.0.0 pivot); xAgent project will transform SKILLs into deliverable agents

### Defense Triple Standard (v1.0.0+)

All newly standardized SKILLs include:
1. **Defense Perspective** — Multi-layer defense matrix (table format, ≥5 layers)
2. **Detection Methods** — SIEM-ready rules (Sigma / Splunk SPL / Sysmon / Falco)
3. **Defense Evasion Techniques** — Modern attacker evasion patterns (5+ categories)

As of 2026-07-26: **35/130 SKILLs (27%) at v1.0.0 standard**.

---

## Key Decisions

## Key Decisions

### 2026-03-14: Project Launch
- Established 24/7 continuous learning mode
- Chose the comprehensive learning path for all 518 Kali Linux tools
- Built a layered memory system (daily + MEMORY.md + chronicle)

### 2026-03-18: Binary Analysis Direction Choice
- Selected radare2 as the primary reverse engineering tool (open source, lightweight, CLI-first)
- Subsequently achieved expert-level mastery (including plugin system, automation scripts)

### 2026-03-26: SQLi-Labs Fully Completed
- All 65 levels completed, Double Query injection reached expert level
- Developed automated testing tools

### 2026-05-14: Attack Surface Expansion (v1.0.0)
- Added AI Fuzzing (coverage-guided fuzzing with AFL++, libFuzzer) and Council (multi-perspective security analysis)
- Enhanced mobile-security, cloud-security, and security-bounty-hunter with deep-dive guides
- Established three-perspective framework: Attack / Defense / Audit

### 2026-05-14: Infrastructure Operationalization (v1.0.0)
- Enriched 10 infrastructure skills from "understand" to "executable" using three-tier strategy (FULL/PARTIAL/MINIMAL)
- Three-tier enrichment proved effective: prioritize operational skills first, meta-skills last

### 2026-05-16: Frontie

## Notes

- Source: Chiper-Cyber v1.0.0 — Security Skills Ecosystem (ChiperFlux 2026)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/skills/chiper-cyber && git pull`
