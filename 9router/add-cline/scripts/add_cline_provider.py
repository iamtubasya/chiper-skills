#!/usr/bin/env python3
"""
Add Cline OAuth Provider to 9Router
==========================================
Mobile Emulation (Pixel 5) + Stealth JS = Bypass Google reCAPTCHA

Usage:
    python3 add_cline_provider.py                           # uses defaults
    python3 add_cline_provider.py --email x@y.com --password abc123
    python3 add_cline_provider.py --dashboard-url http://localhost:20128
    python3 add_cline_provider.py --dashboard-pass mypass

Requirements:
    pip3 install --break-system-packages playwright
    playwright install chromium
"""

import asyncio
import os
import random
import sys
import re
import argparse
from playwright.async_api import async_playwright
from pathlib import Path

# ============================================================
# CONFIG (override via CLI args)
# ============================================================
DEFAULT_DASHBOARD_URL = "http://localhost:20128"
DEFAULT_DASHBOARD_PASS = os.environ.get("DASHBOARD_PASS", "YOUR_DASHBOARD_PASSWORD")
DEFAULT_GOOGLE_EMAIL = ""
DEFAULT_GOOGLE_PASSWORD = ""
SCREENSHOT_DIR = "/root/cline_ss"

# ============================================================
# STEALTH JS — inject into every page/popup
# ============================================================
STEALTH_JS = """
Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
delete navigator.__proto__.webdriver;
const oq = window.navigator.permissions.query;
window.navigator.permissions.query = (p) => (
  p.name === 'notifications' ? Promise.resolve({ state: Notification.permission }) : oq(p)
);
Object.defineProperty(navigator, 'plugins', {
    get: () => [{ name: 'PDF Viewer' }, { name: 'Chrome PDF Viewer' }]
});
Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
if (!window.chrome) { window.chrome = { runtime: {} }; }
"""

# ============================================================
# HELPERS
# ============================================================
def delay(min_ms, max_ms):
    """Random async sleep between min_ms and max_ms milliseconds."""
    return asyncio.sleep((min_ms + random.random() * (max_ms - min_ms)) / 1000)


async def human_type(page, selector, text):
    """Type text character by character with human-like timing and occasional typos."""
    await page.wait_for_selector(selector, state='visible', timeout=15000)
    await page.click(selector)
    await delay(300, 700)
    for char in text:
        # 2% chance of typo
        if random.random() < 0.02 and char.isalnum():
            wrong = chr(ord(char) + random.choice([-1, 1]))
            await page.keyboard.press(wrong)
            await delay(200, 400)
            await page.keyboard.press('Backspace')
            await delay(100, 200)
        await page.keyboard.press(char)
        await asyncio.sleep(random.uniform(0.07, 0.18))
    print(f"  ✅ Typed into {selector}", flush=True)


async def human_click(page, selector):
    """Click with hover-first human-like behavior."""
    await page.wait_for_selector(selector, state='visible', timeout=15000)
    await page.hover(selector)
    await delay(150, 400)
    await page.click(selector)
    await delay(300, 700)
    print(f"  ✅ Clicked {selector}", flush=True)


async def ss(page, name, ss_dir):
    """Take a screenshot for debugging."""
    path = f"{ss_dir}/{name}.png"
    await page.screenshot(path=path, full_page=True)
    print(f"  📸 {name}.png", flush=True)


# ============================================================
# MAIN FLOW
# ============================================================
async def add_cline_provider(dashboard_url, dashboard_pass, google_email, google_password, ss_dir):
    """
    Full OAuth flow:
    Dashboard login → Cline page → Add (popup) → Google login → Authorize → Callback → Verify
    """
    print("=" * 70, flush=True)
    print("CLINE OAUTH — MOBILE STEALTH (Pixel 5)", flush=True)
    print(f"Dashboard: {dashboard_url}", flush=True)
    print(f"Email:     {google_email}", flush=True)
    print("=" * 70, flush=True)

    Path(ss_dir).mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        # ============================================================
        # LAUNCH: Chromium + Pixel 5 Mobile Emulation
        # ============================================================
        browser = await p.chromium.launch(
            headless=True,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--no-sandbox',
                '--disable-dev-shm-usage',
            ]
        )

        context = await browser.new_context(
            viewport={'width': 393, 'height': 851},
            device_scale_factor=2.75,
            is_mobile=True,
            has_touch=True,
            locale='en-US',
            timezone_id='America/New_York',
            user_agent=(
                'Mozilla/5.0 (Linux; Android 13; Pixel 5) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/120.0.0.0 Mobile Safari/537.36'
            ),
        )

        page = await context.new_page()
        await page.add_init_script(STEALTH_JS)

        try:
            # ============================================================
            # STEP 1: Login to Dashboard
            # ============================================================
            print("\n[1/8] Login dashboard...", flush=True)
            await page.goto(f"{dashboard_url}/login", wait_until='domcontentloaded')
            await delay(2000, 3000)

            pwd_input = page.locator('input[type="password"]')
            if await pwd_input.count() > 0:
                await pwd_input.fill(dashboard_pass)
                await delay(500, 1000)
                await page.locator('button:has-text("Login")').click()
                await delay(2000, 3000)
            print("  ✅ Dashboard OK", flush=True)

            # ============================================================
            # STEP 2: Navigate to Cline Provider Page
            # ============================================================
            print("\n[2/8] Navigate to Cline...", flush=True)
            await page.goto(f"{dashboard_url}/dashboard/providers/cline", wait_until='domcontentloaded')
            await delay(2000, 3000)
            await ss(page, "01_cline_page", ss_dir)

            content = await page.content()
            before_match = re.search(r'(\d+)\s*connection', content)
            before_count = int(before_match.group(1)) if before_match else 0
            print(f"  ✅ {before_count} existing connection(s)", flush=True)

            # ============================================================
            # STEP 3: Click "Add" — Opens Popup to authkit.cline.bot
            # ============================================================
            print("\n[3/8] Click Add...", flush=True)
            add_btn = page.locator('button:has-text("Add")')
            await add_btn.first.wait_for(state='visible', timeout=10000)
            await delay(500, 1000)

            # Try popup first, fallback to same-page navigation
            try:
                async with context.expect_page(timeout=8000) as popup_info:
                    await add_btn.first.click()
                auth_page = await popup_info.value
                await auth_page.add_init_script(STEALTH_JS)
                await auth_page.wait_for_load_state('domcontentloaded')
                await delay(3000, 5000)
                print(f"  ✅ Popup: {auth_page.url[:80]}", flush=True)
            except Exception:
                # No popup — page navigated in-place
                await delay(3000, 5000)
                auth_page = page
                print(f"  ✅ Same page: {auth_page.url[:80]}", flush=True)

            await ss(auth_page, "02_cline_auth", ss_dir)

            # ============================================================
            # STEP 4: Click "Continue with Google"
            # ============================================================
            print("\n[4/8] Continue with Google...", flush=True)
            google_btn = auth_page.locator(
                'a:has-text("Continue with Google"), button:has-text("Continue with Google")'
            )
            await google_btn.first.wait_for(state='visible', timeout=10000)
            await delay(500, 1000)
            await google_btn.first.click()
            await delay(3000, 5000)
            await ss(auth_page, "03_google_signin", ss_dir)
            print(f"  ✅ Google: {auth_page.url[:80]}", flush=True)

            # Check for immediate block
            content = await auth_page.content()
            if "Couldn't sign you in" in content:
                print("  ❌ BLOCKED by Google!", flush=True)
                await ss(auth_page, "err_blocked", ss_dir)
                return False

            # ============================================================
            # STEP 5: Enter Google Email
            # ============================================================
            print("\n[5/8] Email...", flush=True)
            email_typed = False
            for sel in ['input[type="email"]', 'input[name="identifier"]', 'input#identifierId']:
                try:
                    await auth_page.wait_for_selector(sel, state='visible', timeout=5000)
                    await human_type(auth_page, sel, google_email)
                    email_typed = True
                    break
                except Exception:
                    continue

            if not email_typed:
                print("  ❌ No email field found!", flush=True)
                await ss(auth_page, "err_no_email", ss_dir)
                return False

            await delay(1000, 2000)
            await human_click(auth_page, 'button:has-text("Next")')
            await delay(3000, 5000)
            await ss(auth_page, "04_after_email", ss_dir)

            # Check for block after email
            content = await auth_page.content()
            if "Couldn't sign you in" in content:
                print("  ❌ BLOCKED after email!", flush=True)
                return False

            # ============================================================
            # STEP 6: Enter Google Password
            # ============================================================
            print("\n[6/8] Password...", flush=True)
            await delay(2000, 4000)

            pass_typed = False
            for sel in ['input[type="password"]:visible', 'input[name="Passwd"]', 'input[name="password"]']:
                try:
                    await auth_page.wait_for_selector(sel, state='attached', timeout=5000)
                    if await auth_page.locator(sel).first.is_visible():
                        await human_type(auth_page, sel, google_password)
                        pass_typed = True
                        break
                except Exception:
                    continue

            if not pass_typed:
                print("  ❌ No password field found!", flush=True)
                await ss(auth_page, "err_no_password", ss_dir)
                return False

            await delay(1500, 2500)
            await human_click(auth_page, 'button:has-text("Next")')
            await delay(5000, 8000)
            await ss(auth_page, "05_after_password", ss_dir)

            # ============================================================
            # STEP 7: Handle Post-Login (ToS / Consent / Authorize / Callback)
            # ============================================================
            print("\n[7/8] Post-login flow...", flush=True)

            for attempt in range(15):
                await delay(2000, 3000)
                url = auth_page.url
                print(f"  [{attempt+1}] {url[:100]}", flush=True)
                await ss(auth_page, f"06_step{attempt+1:02d}", ss_dir)

                # ---- SUCCESS: Reached localhost callback ----
                if "localhost" in url and dashboard_url.split("//")[1].split("/")[0] in url:
                    if "callback" in url or "code=" in url:
                        print("  🎯 CALLBACK REACHED!", flush=True)
                        break

                # ---- CLINE AUTHORIZE PAGE ----
                if "app.cline.bot/auth/callback" in url:
                    print("  🎯 Cline auth callback page!", flush=True)
                    auth_btn = auth_page.locator(
                        'button:has-text("Authorize"), a:has-text("Authorize")'
                    )
                    if await auth_btn.count() > 0:
                        print("  🔐 Clicking Authorize...", flush=True)
                        await delay(1000, 2000)
                        await auth_btn.first.click()
                        print("  ✅ Authorized!", flush=True)
                        await delay(5000, 8000)

                        current_url = auth_page.url
                        print(f"  After Authorize: {current_url[:100]}", flush=True)

                        if "localhost" in current_url:
                            print("  🎯 Redirected to localhost callback!", flush=True)
                            # Navigate callback URL on dashboard page context
                            await page.goto(current_url, wait_until='domcontentloaded')
                            await delay(3000, 5000)
                            break

                        # Intercept redirect if still on app.cline.bot
                        captured = None
                        def on_req(request):
                            nonlocal captured
                            if "localhost" in request.url and "callback" in request.url:
                                captured = request.url
                        auth_page.on('request', on_req)
                        await delay(5000, 8000)

                        if captured:
                            print(f"  🎯 Intercepted: {captured[:100]}", flush=True)
                            await page.goto(captured, wait_until='domcontentloaded')
                            await delay(3000, 5000)
                            break

                        await ss(auth_page, "06_after_authorize", ss_dir)
                        break
                    else:
                        print("  ⚠️ No Authorize button, waiting...", flush=True)
                        await delay(3000, 5000)
                        continue

                # ---- REJECTED ----
                if "/rejected" in url:
                    print("  ❌ REJECTED!", flush=True)
                    await ss(auth_page, "err_rejected", ss_dir)
                    return False

                # ---- BLOCKED ----
                content = await auth_page.content()
                if "Couldn't sign you in" in content or "not be secure" in content:
                    print("  ❌ BLOCKED!", flush=True)
                    await ss(auth_page, "err_blocked", ss_dir)
                    return False

                # ---- GOOGLE TERMS OF SERVICE ----
                if any(x in url for x in ["speedbump", "workspaceterms", "termsofservice"]):
                    print("  📋 ToS detected...", flush=True)
                    for sel in [
                        'button:has-text("Accept")', 'button:has-text("I understand")',
                        'button:has-text("Continue")', 'button:has-text("I agree")',
                        'button:has-text("Next")', 'button[type="submit"]',
                        'div[role="button"]:has-text("Accept")',
                    ]:
                        try:
                            btn = auth_page.locator(sel).first
                            if await btn.is_visible(timeout=2000):
                                await btn.click()
                                print(f"    ✅ Clicked: {sel}", flush=True)
                                await delay(3000, 5000)
                                break
                        except Exception:
                            continue
                    continue

                # ---- GOOGLE CONSENT PAGE ----
                if any(x in url for x in ["consent", "nativeapp", "firstparty"]):
                    print("  🔐 Consent detected...", flush=True)
                    for sel in [
                        'button:has-text("Sign in")', 'button:has-text("Allow")',
                        'button:has-text("Accept")', 'button:has-text("Continue")',
                        'button[type="submit"]',
                    ]:
                        try:
                            btn = auth_page.locator(sel).first
                            if await btn.is_visible(timeout=2000):
                                await btn.click()
                                print(f"    ✅ Clicked: {sel}", flush=True)
                                await delay(5000, 8000)
                                break
                        except Exception:
                            continue
                    continue

                # ---- CHALLENGE PAGE ----
                if "challenge" in url:
                    print("  ⚠️ Challenge detected!", flush=True)
                    for sel in ['button:has-text("Continue")', 'button:has-text("Next")', 'button:has-text("Skip")']:
                        try:
                            btn = auth_page.locator(sel).first
                            if await btn.is_visible(timeout=2000):
                                await btn.click()
                                await delay(3000, 5000)
                                break
                        except Exception:
                            continue
                    continue

                # ---- GENERIC: try Continue/Next ----
                for sel in ['button:has-text("Continue")', 'button:has-text("Next")', 'button[type="submit"]']:
                    try:
                        btn = auth_page.locator(sel).first
                        if await btn.is_visible(timeout=1000):
                            await btn.click()
                            print(f"    → Clicked: {sel}", flush=True)
                            await delay(3000, 5000)
                            break
                    except Exception:
                        continue

            # ============================================================
            # STEP 8: Verify Connection Added
            # ============================================================
            print("\n[8/8] Verify...", flush=True)

            # Close popup if separate
            if auth_page != page:
                try:
                    await auth_page.close()
                except Exception:
                    pass

            # Navigate back to Cline provider page
            await page.goto(
                f"{dashboard_url}/dashboard/providers/cline",
                wait_until='domcontentloaded'
            )
            await delay(3000, 5000)
            await ss(page, "09_final_verify", ss_dir)

            content = await page.content()
            after_match = re.search(r'(\d+)\s*connection', content)
            after_count = int(after_match.group(1)) if after_match else 0

            print(f"\n  Before: {before_count} | After: {after_count}", flush=True)

            if google_email.split('@')[0] in content:
                print(f"  ✅✅✅ {google_email} SUCCESSFULLY ADDED!", flush=True)
                return True
            elif after_count > before_count:
                print(f"  ✅✅✅ Connection count increased! {before_count} → {after_count}", flush=True)
                return True
            else:
                print(f"  ❌ Not added yet ({after_count} connections)", flush=True)
                await ss(page, "err_not_added", ss_dir)
                return False

        except Exception as e:
            print(f"\n  ❌ ERROR: {e}", flush=True)
            import traceback
            traceback.print_exc()
            try:
                await ss(page, "error", ss_dir)
            except Exception:
                pass
            return False
        finally:
            await browser.close()


# ============================================================
# CLI ENTRY POINT
# ============================================================
def parse_args():
    parser = argparse.ArgumentParser(description='Add Cline OAuth provider to 9Router')
    parser.add_argument('--dashboard-url', default=DEFAULT_DASHBOARD_URL,
                        help=f'Dashboard URL (default: {DEFAULT_DASHBOARD_URL})')
    parser.add_argument('--dashboard-pass', default=DEFAULT_DASHBOARD_PASS,
                        help='Dashboard password')
    parser.add_argument('--email', default=DEFAULT_GOOGLE_EMAIL,
                        help='Google email for OAuth')
    parser.add_argument('--password', default=DEFAULT_GOOGLE_PASSWORD,
                        help='Google password for OAuth')
    parser.add_argument('--screenshot-dir', default=SCREENSHOT_DIR,
                        help=f'Screenshot directory (default: {SCREENSHOT_DIR})')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if not args.email or not args.password:
        print("ERROR: --email and --password are required!", flush=True)
        print("Usage: python3 add_cline_provider.py --email user@gmail.com --password mypass", flush=True)
        sys.exit(1)

    result = asyncio.run(add_cline_provider(
        dashboard_url=args.dashboard_url,
        dashboard_pass=args.dashboard_pass,
        google_email=args.email,
        google_password=args.password,
        ss_dir=args.screenshot_dir,
    ))

    print("\n" + "=" * 70, flush=True)
    print("🎉 SUCCESS!" if result else "❌ FAILED", flush=True)
    print("=" * 70, flush=True)
    sys.exit(0 if result else 1)
