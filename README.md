# ⚡ Chiper Skills

Custom automation & security skills for [Hermes Agent](https://hermes-agent.nousresearch.com).

Built by [ChiperFlux](https://github.com/iamtubasya).

---

## 📂 Skill Packs

### [`9router/`](9router/)

Automation skills untuk **9Router** proxy dashboard — OAuth provider setup via stealth browser automation. Default: `http://localhost:20128`

| Skill | Description | Stack |
|---|---|---|
| **[add-antigravity](9router/add-antigravity/)** | Google OAuth stealth with anti-detection. Mobile Chromium emulation, auto-ToS, auto-consent, token exchange. | Playwright · Python |
| **[add-cline](9router/add-cline/)** | Add Cline provider via Google OAuth. Pixel 5 mobile emulation. | Playwright · Python |
| **[add-kiro](9router/add-kiro/)** | Add Kiro provider via AWS Builder ID + Google OAuth. | Playwright · Python |
| **[Add-kiro-v1](9router/Add-kiro-v1/)** | Kiro ultra-stealth variant. | Playwright · Python |

### [`airdrop/`](airdrop/)

Auto-claim & automation skills untuk crypto airdrops.

| Skill | Description | Stack |
|---|---|---|
| **[interlink](airdrop/interlink/)** | Auto-claim $ITLG. OTP login → refresh token → auto-claim every 4h. | Python · IMAP |

### [`chiper-cyber/`](chiper-cyber/)

144 security skill domains — pentest, exploit dev, OSINT, forensics, cloud, AI red team, blockchain, 5G/6G, SCADA, wireless, dan 120+ domain lainnya. 302 tools.

| Skill Pack | Description | Tools |
|---|---|---|
| **[chiper-cyber](chiper-cyber/)** | 144 security skill domains | 302 tools |

Lihat [chiper-cyber/SKILL.md](chiper-cyber/SKILL.md) dan [chiper-cyber/README.md](chiper-cyber/README.md).

---

## 📦 Quick Start

```bash
git clone https://github.com/iamtubasya/chiper-skills.git /tmp/chiper-skills
cd /tmp/chiper-skills

# 9router
cp -r 9router ~/.hermes/skills/

# airdrop
cp -r airdrop ~/.hermes/skills/

# chiper-cyber
cp -r chiper-cyber ~/.hermes/skills/
bash ~/.hermes/skills/chiper-cyber/chiper-bootstrap/scripts/install.sh
```

---

## ⚠️ Disclaimer

These skills are for authorized security testing and research only.
Unauthorized access to computer systems is illegal.
Use only on systems you own or have explicit written permission to test.
