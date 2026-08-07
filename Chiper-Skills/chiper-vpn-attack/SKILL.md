---
name: chiper-vpn-attack
description: "Use when Virtual Private Networks (VPNs) are a critical component of enterprise network security, providing encrypted tunnels for remote access and site-to-site connectivity."
version: "0.2.0"
author: kali-claw (OpenClaw Security Research Project)
metadata:
  hermes:
    tags: [pentest, security, kali-linux, kali-claw, vpn, attack]
references:
  - path: /home/chiper/.hermes/kali-claw/skills/vpn-attack/SKILL.md
  - path: /home/chiper/.hermes/kali-claw/skills/vpn-attack/payloads.md
  - path: /home/chiper/.hermes/kali-claw/skills/vpn-attack/test-cases.md
  - path: /home/chiper/.hermes/kali-claw/skills/vpn-attack/guides
---

# Vpn Attack

## When to Use

Vpn Attack skill domain covering security operations.

**Tools**: ike-scan, ikeforce, ikecrack, vpnc, strongswan

**Domain**: security

## Core Tools

| Tool | Purpose | Command Example |
|------|---------|-----------------|
| **ike-scan** | IKE enumeration, fingerprinting, and transform set discovery | `ike-scan -M -A --id=vpn --pskcrack target` |
| **ikeforce** | Aggressive mode PSK brute force and VPN enumeration | `ikeforce.py target -e -i vpn

## Methodology Overview

### Attack Chain

```
Discovery → Enumeration → Authentication Attack → Tunnel Exploitation → Post-VPN Access
```

**1. Discovery (Identify VPN gateways)**
- Port scan for IKE (UDP 500, 4500), SSL VPN (TCP 443, 8443, 10443)
- Identify VPN vendors via banner grabbing, certificate analysis, and web interface fingerprinting
- Detect supported protocols: IPSec/IKEv1, IKEv2, SSL/TLS, PPTP, L2TP

**2. E

## Instructions

Read the referenced kali-claw files for full methodology:
- **SKILL.md** — Step-by-step methodology, attack chain, tools, and defense perspective
- **payloads.md** — Ready-to-use attack payloads organized by type and technique
- **test-cases.md** — Structured test procedures with prerequisites and expected results
- **guides/** — Deep-dive learning materials and scripts

Full skill content at: `/home/chiper/.hermes/kali-claw/skills/vpn-attack/`

## Examples

See `payloads.md` in the referenced directory for ready-to-use attack payloads.

## Test Cases

See `test-cases.md` in the referenced directory for structured test procedures.

## Notes

- Source: kali-claw v0.2.0.4 — Agent Skills Open Standard (Anthropic 2025)
- Defense Triple: Defense Perspective + Detection Methods + Evasion Techniques
- Update: `cd ~/.hermes/kali-claw && git pull`
