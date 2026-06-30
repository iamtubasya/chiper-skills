# ⚡ Chiper Skills

Custom automation skills for [ChiperRouter / 9Router](https://github.com/iamtubasya) — Google OAuth stealth, provider auto-setup, and batch account provisioning.

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

---

## 🛠 Requirements

```bash
# Python 3.10+
pip3 install playwright
playwright install chromium
```

---

## 🚀 Quick Start

1. **Clone**
   ```bash
   git clone https://github.com/iamtubasya/chiper-skill.git
   cd chiper-skill
   ```

2. **Pick a skill** → read the `SKILL.md` inside each folder for triggers, config, and usage.

3. **Run scripts** → each skill has a `scripts/` folder with ready-to-run automation.

---

## 📁 Structure

```
chiper-skill/
└── 9router/
    ├── add-antigravity/     # Google OAuth stealth (v3)
    │   ├── SKILL.md
    │   ├── README.md
    │   ├── config.env.example
    │   └── scripts/
    │       ├── google_oauth_stealth.py
    │       └── batch_run.sh
    ├── add-cline/           # Cline provider setup
    │   ├── SKILL.md
    │   ├── README.md
    │   └── scripts/
    │       └── add_cline_provider.py
    ├── add-kiro/            # Kiro via AWS Builder ID
    │   ├── SKILL.md
    │   └── scripts/
    │       └── signup_kiro.py
    └── Add-kiro-v1/         # Kiro ultra-stealth variant
        ├── SKILL.md
        └── scripts/
            └── signup_kiro_ultra_stealth.py
```

---

## ⚠️ Disclaimer

These skills are designed for personal automation on your own infrastructure. Use responsibly and in accordance with each service's terms.

---

## 📜 License

MIT
