#!/usr/bin/env python3
"""
Kiro Signup with ULTRA STEALTH - Maximum anti-detection
"""
import asyncio
import logging
import os
import random
import re
from pathlib import Path
from playwright.async_api import async_playwright

# Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("ultra_stealth")

# Config
DASHBOARD_URL = "http://localhost:20128/dashboard/providers/kiro"
LOGIN_URL = "http://localhost:20128/login"
DASHBOARD_PASS = os.environ.get("DASHBOARD_PASS", "YOUR_DASHBOARD_PASSWORD")
GOOGLE_EMAIL = os.environ.get("GOOGLE_EMAIL", "your-email@domain.com")
GOOGLE_PASS = os.environ.get("GOOGLE_PASS", "YOUR_GOOGLE_PASSWORD")

async def main():
    log.info("="*60)
    log.info("ULTRA STEALTH MODE - Maximum Anti-Detection")
    log.info("="*60)

    async with async_playwright() as p:
        # ULTRA STEALTH BROWSER CONFIG
        browser = await p.chromium.launch(
            headless=True,
            args=[
                # Basic
                "--no-sandbox",
                "--disable-gpu",
                "--disable-dev-shm-usage",
                
                # Anti-detection MAXED OUT
                "--disable-blink-features=AutomationControlled",
                "--disable-features=IsolateOrigins,site-per-process",
                "--disable-web-security",
                "--disable-features=VizDisplayCompositor",
                
                # Fingerprint spoofing
                "--disable-features=site-per-process",
                "--disable-site-isolation-trials",
                
                # Stealth flags
                "--no-first-run",
                "--no-default-browser-check",
                "--disable-popup-blocking",
                "--disable-prompt-on-repost",
                "--disable-hang-monitor",
                "--disable-sync",
                "--disable-background-networking",
                "--disable-background-timer-throttling",
                "--disable-backgrounding-occluded-windows",
                "--disable-breakpad",
                "--disable-client-side-phishing-detection",
                "--disable-component-update",
                "--disable-default-apps",
                "--disable-domain-reliability",
                "--disable-extensions",
                "--disable-features=TranslateUI",
                "--disable-ipc-flooding-protection",
                "--metrics-recording-only",
                "--mute-audio",
                "--no-pings",
                "--password-store=basic",
                "--use-mock-keychain",
                
                # Window size
                "--window-size=1920,1080",
            ],
        )

        # ULTRA STEALTH CONTEXT
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True,
            
            # Real Chrome user agent (current version)
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            
            locale="en-US",
            timezone_id="America/New_York",
            
            # Extra headers
            extra_http_headers={
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Sec-Ch-Ua": '"Chromium";v="131", "Not_A Brand";v="24"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"Windows"',
                "Upgrade-Insecure-Requests": "1",
            },
            
            # Permissions
            permissions=["geolocation", "notifications"],
            geolocation={"latitude": 40.7128, "longitude": -74.0060},  # NYC
        )

        # INJECT ANTI-DETECTION SCRIPTS
        await context.add_init_script("""
            // Remove webdriver property
            Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
            
            // Remove automation flags
            delete navigator.__proto__.webdriver;
            
            // Spoof Chrome runtime
            window.chrome = {
                runtime: {},
                loadTimes: function() {},
                csi: function() {},
                app: {}
            };
            
            // Spoof plugins
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5]
            });
            
            // Spoof languages
            Object.defineProperty(navigator, 'languages', {
                get: () => ['en-US', 'en']
            });
            
            // Spoof platform
            Object.defineProperty(navigator, 'platform', {
                get: () => 'Win32'
            });
            
            // Spoof vendor
            Object.defineProperty(navigator, 'vendor', {
                get: () => 'Google Inc.'
            });
            
            // Spoof hardware concurrency
            Object.defineProperty(navigator, 'hardwareConcurrency', {
                get: () => 8
            });
            
            // Spoof deviceMemory
            Object.defineProperty(navigator, 'deviceMemory', {
                get: () => 8
            });
            
            // Spoof permissions
            const originalQuery = window.navigator.permissions.query;
            window.navigator.permissions.query = (parameters) => (
                parameters.name === 'notifications' ?
                    Promise.resolve({state: Notification.permission}) :
                    originalQuery(parameters)
            );
        """)

        page = await context.new_page()
        page.set_default_timeout(60000)

        try:
            # Step 1: Login
            log.info("STEP 1: Login to dashboard")
            await page.goto(LOGIN_URL, wait_until="networkidle")
            await asyncio.sleep(random.uniform(1, 2))
            await page.locator('input[type="password"]').fill(DASHBOARD_PASS)
            await asyncio.sleep(random.uniform(0.5, 1))
            await page.locator('button:has-text("Login")').click()
            await page.wait_for_load_state("networkidle")
            await asyncio.sleep(2)
            log.info(f"Logged in: {page.url}")

            # Step 2: Check current connections
            log.info("STEP 2: Navigate to Kiro providers")
            await page.goto(DASHBOARD_URL, wait_until="networkidle")
            await asyncio.sleep(3)
            txt = await page.inner_text("body")
            current = re.search(r"(\d+) connections", txt)
            current_count = int(current.group(1)) if current else 0
            log.info(f"Current connections: {current_count}")

            # Step 3: Click Add
            log.info("STEP 3: Click Add button")
            await page.get_by_role("button", name="Add").first.click()
            await asyncio.sleep(3)

            # Step 4: Select AWS Builder ID
            log.info("STEP 4: Select AWS Builder ID")
            await page.get_by_text("AWS Builder ID", exact=True).click()
            await asyncio.sleep(5)

            # Extract device URL
            txt = await page.inner_text("body")
            url_match = re.search(r"(https://view\.awsapps\.com/start/#/device\?user_code=[A-Z0-9-]+)", txt)
            if not url_match:
                log.error("Device URL not found!")
                await page.screenshot(path="/home/paws/error_no_device_url.png")
                return
            
            device_url = url_match.group(1)
            log.info(f"Device URL: {device_url}")

            # Step 5: Open auth page in NEW CONTEXT (separate browser profile)
            log.info("STEP 5: Open auth page in separate context")
            
            # Create ANOTHER ultra-stealth context for Google
            auth_context = await browser.new_context(
                viewport={"width": 1920, "height": 1080},
                ignore_https_errors=True,
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
                locale="en-US",
                timezone_id="America/New_York",
                extra_http_headers={
                    "Accept-Language": "en-US,en;q=0.9",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                },
            )
            
            await auth_context.add_init_script("""
                Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
                delete navigator.__proto__.webdriver;
                window.chrome = {runtime: {}, loadTimes: function() {}, csi: function() {}, app: {}};
            """)
            
            ap = await auth_context.new_page()
            ap.set_default_timeout(60000)
            
            await ap.goto(device_url, wait_until="networkidle")
            await asyncio.sleep(5)
            await ap.screenshot(path="/home/paws/ultra_01_auth_page.png")

            # Step 6: Click Google OAuth
            log.info("STEP 6: Click Google OAuth")
            google_btn = ap.get_by_test_id("test-signup-with-button-Google")
            if await google_btn.is_visible():
                await asyncio.sleep(random.uniform(1, 2))
                await google_btn.click()
                await asyncio.sleep(5)
                await ap.screenshot(path="/home/paws/ultra_02_google_redirect.png")
                
                # Wait for Google page
                try:
                    await ap.wait_for_url("**/accounts.google.com/**", timeout=15000)
                    log.info("Google login page loaded")
                except:
                    log.warning("Did not redirect to Google, checking current page...")
                
                await asyncio.sleep(3)
                await ap.screenshot(path="/home/paws/ultra_03_google_page.png")
                
                # Step 7: Fill Google email
                log.info(f"STEP 7: Fill Google email: {GOOGLE_EMAIL}")
                email_input = ap.locator('#identifierId, input[name="identifier"], input[type="email"]').first
                try:
                    await email_input.wait_for(state="visible", timeout=10000)
                    await asyncio.sleep(random.uniform(1, 2))
                    await email_input.fill(GOOGLE_EMAIL)
                    await asyncio.sleep(random.uniform(1, 2))
                    log.info("Email filled")
                    await ap.screenshot(path="/home/paws/ultra_04_email_filled.png")
                    
                    # Click Next
                    next_btn = ap.locator('button:has-text("Next"), #identifierNext').first
                    await asyncio.sleep(random.uniform(0.5, 1))
                    await next_btn.click()
                    await asyncio.sleep(5)
                    await ap.screenshot(path="/home/paws/ultra_05_after_email.png")
                    
                    # Check for error
                    txt = await ap.inner_text("body")
                    if "not be secure" in txt or "Couldn't sign you in" in txt:
                        log.error("Google blocked the login - detected automation")
                        await ap.screenshot(path="/home/paws/ultra_ERROR_google_blocked.png")
                        log.info("Page content:")
                        log.info(txt[:500])
                    else:
                        # Step 8: Fill password
                        log.info("STEP 8: Fill Google password")
                        pw_input = ap.locator('input[type="password"]').first
                        if await pw_input.is_visible(timeout=10000):
                            await asyncio.sleep(random.uniform(1, 2))
                            await pw_input.fill(GOOGLE_PASS)
                            await asyncio.sleep(random.uniform(1, 2))
                            
                            # Click Next/Sign in
                            signin_btn = ap.locator('button:has-text("Next"), #passwordNext, button:has-text("Sign in")').first
                            await asyncio.sleep(random.uniform(0.5, 1))
                            await signin_btn.click()
                            await asyncio.sleep(10)
                            await ap.screenshot(path="/home/paws/ultra_06_after_password.png")
                            
                            # Check for Google Workspace consent screen
                            txt = await ap.inner_text("body")
                            if "I understand" in txt or "Welcome" in txt:
                                log.info("STEP 8.5: Click 'I understand' on Google Workspace consent")
                                understand_btn = ap.locator('button:has-text("I understand")').first
                                try:
                                    if await understand_btn.is_visible(timeout=5000):
                                        await asyncio.sleep(random.uniform(1, 2))
                                        await understand_btn.click()
                                        await asyncio.sleep(5)
                                        await ap.screenshot(path="/home/paws/ultra_07_after_consent.png")
                                        log.info("Consent accepted")
                                except Exception as e:
                                    log.warning(f"Consent button not found: {e}")
                            
                            # Check for Google OAuth consent (Continue button)
                            await asyncio.sleep(3)
                            txt = await ap.inner_text("body")
                            if "Continue" in txt and "Sign in with Google" in txt:
                                log.info("STEP 8.6: Click 'Continue' on Google OAuth consent")
                                continue_btn = ap.locator('button:has-text("Continue")').first
                                try:
                                    if await continue_btn.is_visible(timeout=5000):
                                        await asyncio.sleep(random.uniform(1, 2))
                                        await continue_btn.click()
                                        await asyncio.sleep(5)
                                        await ap.screenshot(path="/home/paws/ultra_08_after_oauth_consent.png")
                                        log.info("OAuth consent accepted")
                                except Exception as e:
                                    log.warning(f"Continue button not found: {e}")
                            
                            # Check for AWS device authorization confirmation
                            await asyncio.sleep(5)
                            txt = await ap.inner_text("body")
                            if "Confirm and continue" in txt or "Authorization requested" in txt:
                                log.info("STEP 8.7: Click 'Confirm and continue' on AWS authorization")
                                confirm_btn = ap.locator('button:has-text("Confirm and continue")').first
                                try:
                                    if await confirm_btn.is_visible(timeout=5000):
                                        await asyncio.sleep(random.uniform(1, 2))
                                        await confirm_btn.click()
                                        await asyncio.sleep(5)
                                        await ap.screenshot(path="/home/paws/ultra_09_after_aws_confirm.png")
                                        log.info("AWS device authorization confirmed")
                                except Exception as e:
                                    log.warning(f"Confirm button not found: {e}")
                            
                            # Check for kiro-oauth-client access consent
                            await asyncio.sleep(5)
                            txt = await ap.inner_text("body")
                            if "Allow access" in txt or "kiro-oauth-client" in txt:
                                log.info("STEP 8.8: Click 'Allow access' for kiro-oauth-client")
                                allow_btn = ap.locator('button:has-text("Allow access")').first
                                try:
                                    if await allow_btn.is_visible(timeout=5000):
                                        await asyncio.sleep(random.uniform(1, 2))
                                        await allow_btn.click()
                                        await asyncio.sleep(5)
                                        await ap.screenshot(path="/home/paws/ultra_10_after_allow_access.png")
                                        log.info("Kiro access allowed!")
                                except Exception as e:
                                    log.warning(f"Allow access button not found: {e}")
                            
                            # Wait for authorization
                            log.info("STEP 9: Wait for authorization...")
                            for i in range(20):
                                txt = await ap.inner_text("body")
                                if any(k in txt.lower() for k in ["authorized", "success", "complete"]):
                                    log.info("Authorization successful!")
                                    await ap.screenshot(path="/home/paws/ultra_SUCCESS_authorized.png")
                                    break
                                await asyncio.sleep(5)
                                log.info(f"Waiting... {i*5}s")
                        else:
                            log.warning("Password field not found")
                            
                except Exception as e:
                    log.error(f"Google login failed: {e}")
                    await ap.screenshot(path="/home/paws/ultra_ERROR_exception.png")
            
            else:
                log.error("Google button not found!")

            # Step 10: Verify
            log.info("STEP 10: Verify new connection")
            await page.goto(DASHBOARD_URL, wait_until="networkidle")
            await asyncio.sleep(5)
            txt = await page.inner_text("body")
            new = re.search(r"(\d+) connections", txt)
            new_count = int(new.group(1)) if new else 0
            log.info(f"After: {new_count} connections")
            
            if new_count > current_count:
                log.info(f"✓ SUCCESS! {current_count} → {new_count}")
                await page.screenshot(path="/home/paws/ultra_FINAL_success.png")
            else:
                log.warning(f"✗ FAILED: Still {current_count} connections")
                await page.screenshot(path="/home/paws/ultra_FINAL_failed.png")

        except Exception as e:
            log.error(f"Fatal: {e}", exc_info=True)
            await page.screenshot(path="/home/paws/ultra_ERROR_fatal.png")
        
        finally:
            await browser.close()
            log.info("Done")


if __name__ == "__main__":
    asyncio.run(main())
