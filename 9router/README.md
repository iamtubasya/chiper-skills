# 9router

Automation skills untuk **9Router** proxy dashboard — OAuth provider setup via stealth browser automation.

Default dashboard: `http://localhost:20128`

## Skills

| Skill | Description | Stack |
|---|---|---|
| **[add-antigravity](add-antigravity/)** | Google OAuth stealth automation with anti-detection. Mobile Chromium emulation, auto-ToS, auto-consent, token exchange. 15+ bypass strategies. | Playwright · Python |
| **[add-cline](add-cline/)** | Add Cline provider via Google OAuth. Pixel 5 mobile emulation to bypass reCAPTCHA. Handles popup, login, authorize, callback. | Playwright · Python |
| **[add-kiro](add-kiro/)** | Add Kiro provider via AWS Builder ID + Google OAuth. Device authorization flow. | Playwright · Python |
| **[Add-kiro-v1](Add-kiro-v1/)** | Kiro provider v1 — ultra-stealth variant with enhanced anti-detection. | Playwright · Python |

## Install

```bash
cp -r 9router ~/.hermes/skills/
```

## Usage

Each skill uses `--dashboard-url` flag (default: `http://localhost:20128`):

```bash
python3 add-cline/scripts/add_cline_provider.py \
  --dashboard-url http://localhost:20128 \
  --dashboard-pass YOUR_PASSWORD
```

For remote tunnel:
```bash
python3 add-cline/scripts/add_cline_provider.py \
  --dashboard-url https://your-domain.com \
  --dashboard-pass YOUR_PASSWORD
```

## Author

**ChiperFlux** (9Router)
