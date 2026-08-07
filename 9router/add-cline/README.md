# Cline Add Provider — Skill Package

## What Is This?

A complete automation skill to **add Cline OAuth provider accounts** to 9Router dashboard via Google OAuth login. Uses Playwright with **Pixel 5 mobile emulation** to bypass Google's reCAPTCHA bot detection.

## For AI Agents (Claude, GPT, Hermes, etc.)

### Quick Install

1. Copy the `cline-add-provider/` folder to your skills directory
2. Install dependencies:
   ```bash
   pip3 install --break-system-packages playwright
   playwright install chromium
   ```

### Quick Use (Run the Script Directly)

```bash
python3 scripts/add_cline_provider.py \
  --email user@gmail.com \
  --password yourpassword \
  --dashboard-url http://localhost:20128 \
  --dashboard-pass YOUR_DASHBOARD_PASSWORD
```

### As a Hermes Agent Skill

Copy the entire `cline-add-provider/` directory to `~/.hermes/skills/system-admin/`:

```bash
cp -r cline-add-provider/ ~/.hermes/skills/system-admin/cline-add-provider/
```

Then the agent can load it with:
```
skill_view(name='cline-add-provider')
```

## File Structure

```
cline-add-provider/
├── README.md                          ← This file (quick start guide)
├── SKILL.md                           ← Full skill documentation
│                                        (architecture, anti-detection, pitfalls, etc.)
└── scripts/
    └── add_cline_provider.py          ← Ready-to-run Python script (CLI)
```

## How It Works (Summary)

```
1. Login to 9Router dashboard (localhost:20128)
2. Navigate to Providers → Cline
3. Click "Add" → popup opens to authkit.cline.bot
4. Click "Continue with Google" → Google Sign-in page
5. Enter email → Enter password (with human-like typing)
6. Handle ToS/Consent pages automatically
7. Click "Authorize" on Cline consent page (app.cline.bot)
8. Callback redirects to localhost → connection saved
9. Verify connection count increased
```

## Key Technology

| Component | Purpose |
|-----------|---------|
| Playwright (async) | Browser automation engine |
| Chromium (headless) | Browser |
| Pixel 5 Mobile Emulation | **Bypass Google reCAPTCHA** |
| Stealth JS Injection | Hide `navigator.webdriver` flag |
| Human-like Typing | Random delay 70-180ms per character |
| Human-like Clicking | Hover before click with delays |

## Critical Notes for Other Agents

1. **MUST use mobile emulation** — without it, Google shows CAPTCHA 100% of the time
2. **MUST inject Stealth JS into popup pages** — not just the main page
3. **MUST click "Authorize" button** on `app.cline.bot/auth/callback` — this is NOT automatic
4. **DO NOT use Browserbase/cloud browsers** — Google blocks their IPs
5. **DO NOT use desktop user-agent** — triggers reCAPTCHA
6. **DO NOT use `playwright-stealth` package alone** — not enough without mobile emulation

## Requirements

- Python 3.10+
- Playwright (`pip3 install playwright`)
- Chromium (`playwright install chromium`)
- 9Router running on localhost:20128
- Valid Google account credentials

## Tested & Verified

- ✅ chiper2@jujusa.my.id — June 2026
- Environment: Debian/Ubuntu, Python 3.12, Playwright 1.61.0
