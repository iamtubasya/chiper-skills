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

---

## 🛠 Requirements

```bash
# Python 3.10+
pip3 install playwright requests
playwright install chromium
```

---

## 🚀 Quick Start

1. **Clone**
   ```bash
   git clone https://github.com/iamtubasya/chiper-skills.git
   cd chiper-skills
   ```

2. **Pick a skill** → read the `SKILL.md` inside each folder for triggers, config, and usage.

3. **Run scripts** → each skill has a `scripts/` folder with ready-to-run automation.

---

## 📁 Structure

```
chiper-skills/
├── 9router/
│   ├── add-antigravity/     # Google OAuth stealth (v3)
│   │   ├── SKILL.md
│   │   ├── README.md
│   │   ├── config.env.example
│   │   └── scripts/
│   ├── add-cline/           # Cline provider setup
│   │   ├── SKILL.md
│   │   ├── README.md
│   │   └── scripts/
│   ├── add-kiro/            # Kiro via AWS Builder ID
│   │   ├── SKILL.md
│   │   └── scripts/
│   └── Add-kiro-v1/         # Kiro ultra-stealth variant
│       ├── SKILL.md
│       └── scripts/
└── interlink/
    ├── SKILL.md             # Full documentation
    └── scripts/
        ├── claim.py         # Main auto-claim script
        └── config.json.example
```

---

## ⚠️ Disclaimer

These skills are designed for personal automation on your own infrastructure. Use responsibly and in accordance with each service's terms.

---

## 📜 License

MIT
