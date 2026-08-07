# ⚡ Chiper Skills

Custom automation skills for [ChiperRouter / 9Router](https://github.com/iamtubasya) — Google OAuth stealth, provider auto-setup, batch account provisioning, and crypto airdrop automation.

Built for [Chiper Agent](https://chiper-agent.nousresearch.com) runtime.

---

## 📂 Skills

### `9router/`

Automation skills for ChiperRouter proxy dashboard — adding AI provider connections via stealth OAuth flows.

| Skill | Description | Stack |
|---|---|---|
| **[add-antigravity](9router/add-antigravity/)** | Google OAuth stealth automation with anti-detection. Mobile Chromium emulation, auto-ToS, auto-consent, token exchange. 15+ bypass strategies. | Playwright · Python |
| **[add-cline](9router/add-cline/)** | Add Cline provider via Google OAuth. Pixel 5 mobile emulation to bypass reCAPTCHA. Handles popup, login, authorize, callback. | Playwright · Python |
| **[add-kiro](9router/add-kiro/)** | Add Kiro provider via AWS Builder ID + Google OAuth. Stealth signup flow. | Playwright · Python |
| **[Add-kiro-v1](9router/Add-kiro-v1/)** | Kiro provider v1 — ultra-stealth variant with enhanced anti-detection. | Playwright · Python |

### `interlink/`

Auto-claim $ITLG (Interlink Gold Token) from Interlink Labs. Single script, login once via OTP, claim every 4 hours without re-login.

| Skill | Description | Stack |
|---|---|---|
| **[interlink-claim](interlink/)** | Auto-claim ITLG token. OTP login → refresh token → auto-claim. Cron-ready, Android-mimic headers, human-like jitter. | Python · IMAP |

### `chiper-cyber/`

144 security skill domains for Hermes Agent — pentest, exploit dev, OSINT, forensics, cloud, AI red team, blockchain, 5G/6G, SCADA, wireless, dan 120+ domain lainnya.

| Skill Pack | Description | Tools |
|---|---|---|
| **[chiper-cyber](chiper-cyber/)** | 144 security skill domains | 302 tools |

Lihat [chiper-cyber/SKILL.md](chiper-cyber/SKILL.md) untuk dokumentasi lengkap dan [chiper-cyber/README.md](chiper-cyber/README.md) untuk daftar semua 144 skills.

**Quick Start:**
```bash
git clone https://github.com/iamtubasya/chiper-skills.git /tmp/chiper-skills
cp -r /tmp/chiper-skills/chiper-cyber ~/.hermes/skills/
bash ~/.hermes/skills/chiper-cyber/chiper-bootstrap/scripts/install.sh
```

---

## 📦 Install

```bash
git clone https://github.com/iamtubasya/chiper-skills.git /tmp/chiper-skills
cd /tmp/chiper-skills

# 9router skills
cp -r 9router ~/.hermes/skills/

# chiper-cyber skills
cp -r chiper-cyber ~/.hermes/skills/
bash ~/.hermes/skills/chiper-cyber/chiper-bootstrap/scripts/install.sh
```

---

## ⚠️ Disclaimer

These skills are for authorized security testing and research only.
Unauthorized access to computer systems is illegal.
Use only on systems you own or have explicit written permission to test.
