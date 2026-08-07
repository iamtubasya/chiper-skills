---
name: chiper-cyber
description: >
  Use when installing, placing, or managing chiper-* skills in Hermes Agent.
  Covers skill placement to ~/.hermes/skills/, environment bootstrap,
  tool verification, and cross-skill dependency resolution.
tags: [setup, skills, installation, placement, management]
---

# Chiper-Cyber Skill Ecosystem

## Overview

**146 skills** across offensive security, covering:

- Web Exploitation (SQLi, XSS, SSRF, XXE, RCE, SSTI)
- Network Pentest (recon, scanning, exploitation, pivoting)
- Active Directory (Kerberos, LDAP, Certificate abuse)
- Cloud Security (AWS, Azure, GCP, Kubernetes)
- Wireless (WiFi, Bluetooth, RFID, NFC, SDR)
- Reverse Engineering (binary, firmware, malware)
- Blockchain / Web3 (Solidity, DeFi, bridge attacks)
- AI/LLM Red Team (prompt injection, jailbreak, agent attack)
- SCADA/ICS (Modbus, DNP3, PROFINET, OPC UA)
- 5G/6G Telecom (5G Core, RAN, O-RAN, signaling)
- And 120+ more domains...

---

## Skill Placement

### Target Directory

```
~/.hermes/skills/chiper-*/SKILL.md
```

### Quick Install (All Skills)

```bash
# Clone this repo
git clone https://github.com/iamtubasya/chiper-skills.git /tmp/chiper-skills

# Copy all skills to Hermes
cp -r /tmp/chiper-skills/Chiper-Skills/chiper-* ~/.hermes/skills/

# Verify
ls ~/.hermes/skills/chiper-* | wc -l
# Expected: 146
```

### Selective Install (One Skill)

```bash
# Copy only what you need
cp -r /tmp/chiper-skills/Chiper-Skills/chiper-web-sqli ~/.hermes/skills/
cp -r /tmp/chiper-skills/Chiper-Skills/chiper-network-pentest ~/.hermes/skills/
```

### From GitHub (Raw)

```bash
# Download single skill
mkdir -p ~/.hermes/skills/chiper-web-sqli
curl -sL https://raw.githubusercontent.com/iamtubasya/chiper-skills/main/Chiper-Skills/chiper-web-sqli/SKILL.md \
  -o ~/.hermes/skills/chiper-web-sqli/SKILL.md
```

---

## Environment Bootstrap

**Run `chiper-bootstrap` FIRST on any new environment:**

```bash
# Install all 302 tools referenced across 146 skills
bash ~/.hermes/skills/chiper-bootstrap/scripts/install.sh

# Verify installation
bash ~/.hermes/skills/chiper-bootstrap/scripts/verify.sh
```

### What Gets Installed

| Phase | Tools | Method |
|-------|-------|--------|
| System | 223 packages | `apt install` |
| Python | 59 libraries | `pip install` |
| Go | 12 binaries | `go install` |
| Manual | 8 tools | Download |

---

## Per-Skill Tool Check

Every skill with CLI tools has a `## Prerequisites` section:

```bash
# Example: chiper-web-sqli checks before running
MISSING=""
for cmd in curl sqlmap; do
  command -v "$cmd" >/dev/null 2>&1 || MISSING="$MISSING $cmd"
done
[ -z "$MISSING" ] && echo "✅ All tools ready" && exit 0
echo "⚠️  Missing:$MISSING"
# → Install only what's missing
```

**Logic:** Check → Missing? → Install ONLY that tool → Execute

---

## Directory Structure

```
Chiper-Cyber/
├── SKILL.md                      ← This file (placement guide)
├── Chiper-Skills/
│   ├── chiper-bootstrap/         ← RUN FIRST (tool installer)
│   │   ├── SKILL.md
│   │   ├── scripts/install.sh
│   │   ├── scripts/verify.sh
│   │   └── references/tool-inventory.md
│   ├── chiper-web-sqli/
│   │   └── SKILL.md              ← Has ## Prerequisites
│   ├── chiper-exploit-development/
│   │   └── SKILL.md
│   ├── chiper-network-pentest/
│   │   └── SKILL.md
│   └── ... (146 skills total)
├── README.md
└── .gitignore
```

---

## OS Support

| OS | Bootstrap | Skills |
|----|-----------|--------|
| Kali Linux (headless) | ✅ Full | ✅ |
| Kali Linux (default/large) | ✅ Full | ✅ |
| Ubuntu 22.04/24.04 | ✅ (adds Kali repo) | ✅ |
| Debian 12+ | ✅ (adds Kali repo) | ✅ |
| Parrot OS | ✅ Full | ✅ |
| Arch Linux | ⚠️ Partial | ✅ |

---

## Priority Order

```
1. chiper-bootstrap    ← Install tools first
2. chiper-kali-tools   ← Tool selection reference
3. chiper-kali-identity ← 12 Hacker Laws, skill matrix
4. chiper-*            ← All other skills (pick what you need)
```

---

## Updating

```bash
# Pull latest skills
cd /tmp/chiper-skills && git pull
cp -r /tmp/chiper-skills/Chiper-Skills/chiper-* ~/.hermes/skills/

# Re-verify tools
bash ~/.hermes/skills/chiper-bootstrap/scripts/verify.sh
```

---

## License

For authorized security testing only. Use responsibly.
