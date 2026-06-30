---
name: chiperrouter-add-kiro
description: Add new Kiro provider account via AWS Builder ID with Google OAuth to ChiperRouter Proxy dashboard
tags: [automation, kiro, aws, oauth, google, playwright, stealth]
version: 1.0.0
---

# ChiperRouter Add Kiro Provider

Automate adding new Kiro AI provider accounts to ChiperRouter Proxy dashboard via AWS Builder ID signup using Google OAuth.

## Trigger Conditions
- User asks to add new Kiro provider connection
- User says "add kiro" or similar
- Need to increase Kiro connections count on dashboard

## Prerequisites
- ChiperRouter or 9router Proxy dashboard access (http://localhost:xxxx or https://domain.com)
- Google Workspace account
- Playwright installed with chromium
- Python 3.10+

## Configuration

User must provide their own credentials. Example:

```python
DASHBOARD_URL = "http://localhost:xxxx/dashboard/providers/kiro"
Or "https://domain.com/dashboard/providers/kiro"
LOGIN_URL = "http://localhost:xxxx/login" or "https://domain.com/login"
DASHBOARD_PASS = "your-dashbord-password" 
GOOGLE_EMAIL = "your-email@domain.com"      # Replace with Google account
GOOGLE_PASS = "your_google_password"        # Replace with Google password
```

## Key Settings
- Dashboard password: User's Router dashboard password
- Google OAuth credentials: User's Google Workspace or Gmail account
- Script location: Can be anywhere (e.g., ~/scripts/, /tmp/, project directory)
- Always use ULTRA STEALTH mode to bypass Google detection

## Step-by-Step Flow

### Step 1: Login to Dashboard
- Navigate to http://localhost:xxxx/login or https://domain.com
- Fill password: user's password,
- Click Login button

### Step 2: Check Current Connections
- Navigate to http://localhost:****/dashboard/providers/kiro or https://domain.com/dashboard/providers/kiro
- Note current connection count (e.g., "9 connections")
- This is the BEFORE count

### Step 3: Open Add Modal
- Click "Add" button
- Modal appears with connection options

### Step 4: Select AWS Builder ID
- Click "AWS Builder ID" option
- Wait for device authorization modal
- Extract device code and URL (format: https://view.awsapps.com/start/#/device?user_code=XXXX-XXXX)

### Step 5: Open Auth Page
- Open device authorization URL in NEW CONTEXT (separate browser profile)
- This prevents cookie/session conflicts

### Step 6: Google OAuth Login
- Click "Sign up with Google" button (test-signup-with-button-Google)
- Fill email: user's Google email (e.g., yourname@gmail.com)
- Click Next
- Fill password: user's Google password
- Click Next

### Step 7: Handle Consent Screens

**Google Workspace Consent (not always shown):**
- If "I understand" button appears, click it
- This only appears for Google Workspace accounts, NOT for regular Gmail
- Regular Gmail accounts skip this step

**Google OAuth Consent:**
- If "Continue" button with "Sign in with Google" appears, click it
- This authorizes AWS to access Google profile

**AWS Device Authorization:**
- If "Confirm and continue" button appears, click it
- This confirms the device code matches

**Kiro Access Consent:**
- If "Allow access" button appears, click it
- This allows kiro-oauth-client to access data

### Step 8: Wait for Authorization
- Wait for "Authorized" or "Success" message
- Timeout after 100 seconds if not detected

### Step 9: Verify Success
- Return to dashboard
- Refresh page
- Check connection count increased
- Verify new account exists (e.g., "Account 10")

## Ultra Stealth Configuration

CRITICAL: Google blocks headless browsers. Use maximum anti-detection:

```python
browser = await p.chromium.launch(
    headless=True,
    args=[
        "--no-sandbox",
        "--disable-gpu",
        "--disable-dev-shm-usage",
        "--disable-blink-features=AutomationControlled",
        "--disable-features=IsolateOrigins,site-per-process",
        "--disable-web-security",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-popup-blocking",
        "--window-size=1920,1080",
    ],
)

# Real Chrome user agent
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

# Anti-detection init scripts
await context.add_init_script("""
    Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
    delete navigator.__proto__.webdriver;
    window.chrome = {runtime: {}, loadTimes: function() {}, csi: function() {}, app: {}};
    Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]});
    Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
""")
```

## Pitfalls

### Google "Browser Not Secure" Error
- This happens with basic headless mode
- MUST use ultra stealth configuration with all flags
- MUST use real Chrome user agent
- MUST inject anti-detection init scripts

### ERR-837 on Manual AWS Signup
- AWS detects automation on manual email/name signup
- Google OAuth bypasses this detection
- Always use Google OAuth, never manual signup

### Device Authorization Timeout
- Device codes expire after 15 minutes
- Complete all steps within this window
- If timeout, click Add again to get new code

### Consent Screens Not Detected
- Add proper waits (3-5 seconds) between steps
- Check page text before clicking
- Use try/except to handle missing elements

### Connections Count Unchanged
- Verify by refreshing dashboard page
- Check if Account N exists in the list
- May need to scroll to see new account

## Verification Steps
1. After script completes, check log for "SUCCESS! X → Y"
2. Refresh dashboard page
3. Count total connections
4. Verify new account number exists

## Files
- Main script: Place anywhere (e.g., ~/signup_kiro_ultra_stealth.py, /tmp/kiro_signup.py)
- Screenshots: Same directory as script (ultra_*.png)
- Logs: stdout

## Success Example
```
STEP 1: Login to dashboard
Logged in: http://localhost:****/dashboard or https://domain.com/dashboard
STEP 2: Navigate to Kiro providers
Current connections: 9
STEP 3: Click Add button
STEP 4: Select AWS Builder ID
Device URL: https://view.awsapps.com/start/#/device?user_code=XXXX-XXXX
STEP 5: Open auth page in separate context
STEP 6: Click Google OAuth
Google login page loaded
STEP 7: Fill Google email: yourname@gmail.com
Email filled
STEP 8: Fill Google password
STEP 8.5: Click 'I understand' on Google Workspace consent (if applicable)
STEP 8.6: Click 'Continue' on Google OAuth consent (if applicable)
STEP 8.7: Click 'Confirm and continue' on AWS authorization
AWS device authorization confirmed
STEP 8.8: Click 'Allow access' for kiro-oauth-client
Kiro access allowed!
STEP 9: Wait for authorization...
Waiting... 0s
...
STEP 10: Verify new connection
After: 10 connections
SUCCESS! 9 → 10
```

## Usage

Edit the CONFIG section at the top of the script with your credentials, then run:

```bash
python3 signup_kiro.py
```

## Important Notes

- The script screenshot paths default to the current working directory
- Google Workspace accounts may see extra consent screens that regular Gmail does not
- Each run creates one new AWS Builder ID linked to your Google account
- If Google account already has an AWS Builder ID, the flow may differ
- Device authorization codes expire in ~15 minutes
- Dashboard URL may differ per deployment, always check with user
