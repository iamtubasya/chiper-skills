# Chiper-Cyber Skills

**146 security skill domains** for Hermes Agent — 302 tools, cross-platform support.

## Quick Start

```bash
# Clone
git clone https://github.com/iamtubasya/chiper-skills.git
cd chiper-skills

# Copy skills to Hermes
cp -r Chiper-Skills/chiper-* ~/.hermes/skills/

# Install all tools
bash ~/.hermes/skills/chiper-bootstrap/scripts/install.sh

# Verify
bash ~/.hermes/skills/chiper-bootstrap/scripts/verify.sh
```

## Skills

| Category | Count | Examples |
|----------|-------|---------|
| Web Exploitation | 15 | sqli, xss, ssrf, xxe, auth-bypass |
| Network | 8 | pentest, sniffing-mitm, tunneling, dns |
| AD/Identity | 5 | ad-ldap, ad-cs, identity-provider, cloud-identity |
| Cloud/Container | 6 | cloud-security, kubernetes, container, gitops |
| Wireless/RF | 6 | wifi, bluetooth-rfid-nfc, sdr-rf, hf-vhf |
| Reverse Engineering | 4 | binary, firmware, reverse-adv, malware-adv |
| Blockchain/Web3 | 2 | blockchain-web3, blockchain-l2 |
| AI/LLM | 7 | ai-security, llm-red-team, ai-fuzzing, ai-agent |
| SCADA/ICS | 3 | scada-ics, ics-fieldbus, cps |
| 5G/6G Telecom | 2 | 5g-telecom, 5g-6g-advanced |
| IoT/Embedded | 3 | iot-pentest, embedded-rtos, hardware |
| Forensics | 3 | digital-forensics, anti-forensics, steganography |
| OSINT/Social | 5 | osint, recon-osint, social-engineering, darkweb |
| Post-Exploit | 4 | post-exploitation, privilege-esc, av-edr-evasion |
| And more... | 67 | crypto, payment, voip, automotive, satellite, etc. |

## Bootstrap (Must Run First)

```bash
# Install 302 tools across all skills
bash ~/.hermes/skills/chiper-bootstrap/scripts/install.sh

# Phase options:
#   --phase 1  → System detection
#   --phase 2  → apt packages (223)
#   --phase 3  → pip packages (59)
#   --phase 4  → Go binaries (12)
#   --phase 5  → Manual downloads (8)
#   --phase all → Everything (default)
```

## Per-Skill Tool Check

Each skill auto-checks tools when invoked:
- ✅ Tools installed → Execute immediately
- ⚠️ Missing tools → Show install command → Install → Execute

## OS Support

| OS | Status |
|----|--------|
| Kali Linux | ✅ Full |
| Ubuntu 22.04/24.04 | ✅ (auto-adds Kali repo) |
| Debian 12+ | ✅ (auto-adds Kali repo) |
| Parrot OS | ✅ Full |

## Links

- **Bootstrap skill**: [`Chiper-Skills/chiper-bootstrap/`](Chiper-Skills/chiper-bootstrap/)
- **Tool inventory**: [`Chiper-Skills/chiper-bootstrap/references/tool-inventory.md`](Chiper-Skills/chiper-bootstrap/references/tool-inventory.md)
- **Full skill list**: See [`SKILL.md`](SKILL.md) for complete directory structure

## License

For authorized security testing only.
