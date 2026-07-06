---
name: interlink-claim
description: "Interlink ITLG Auto Claim — single script, OTP-free after first login, cron-ready"
version: "2.0.1"
tags: [crypto, airdrop, auto-claim, interlink, itlg, automation, claim]
related_skills: []
---

# Interlink ITLG Auto Claim (claim.py)

## Overview

Single-script auto-claim untuk token $ITLG dari Interlink Labs. Login sekali via OTP, token tersimpan, claim berulang tanpa login lagi (pakai refresh token).

**Source:** https://github.com/feb-frmn/itlg-claim (modified)

## Skill Directory

```
SKILL_DIR/scripts/
├── claim.py              # Main script (604 baris)
├── config.json           # Kredensial (manual edit, gitignored)
├── config.json.example   # Contoh config (aman di-share)
├── token.json            # JWT token (auto-created)
├── token-backup.json     # Backup token (auto-created)
└── claim_state.json      # History claim (auto-created)
```

**Semua path relatif terhadap SKILL_DIR** — gunakan `SKILL_DIR/scripts/` bukan hardcode path absolut.

## Config Format

Copy `config.json.example` ke `config.json`, edit manual:

```json
{
  "loginId": "0000000000",
  "passcode": "000000",
  "email": "your_gmail@gmail.com",
  "imapPassword": "xxxx xxxx xxxx xxxx",
  "deviceId": "",
  "deviceModel": "",
  "deviceBrand": ""
}
```

**Yang wajib:**
- loginId — angka dari app Interlink (Profile → Login ID)
- passcode — 6 digit
- email — Gmail terdaftar di Interlink
- imapPassword — Gmail App Password (16 char, BUKAN password Gmail)

**Yang opsional (auto-generate kalau kosong):**
- deviceId — md5(loginId)[:16]
- deviceModel — random dari 10 device list
- deviceBrand — sesuai deviceModel

## Gmail App Password Setup

1. Buka https://myaccount.google.com/apppasswords
2. Login dengan Gmail yang terdaftar di Interlink
3. Pilih app "Mail", device "Other" → ketik "Interlink Bot"
4. Generate → copy 16 karakter (format: xxxx xxxx xxxx xxxx)

**Syarat:** Gmail harus punya 2FA aktif.

## Usage

```bash
cd SKILL_DIR/scripts

# Normal run: auto session → claim → dashboard
python3 claim.py

# Cek status saja, gak claim
python3 claim.py --status

# Force login ulang (OTP baru)
python3 claim.py --login
```

## Alur Kerja Script

```
1. Load config.json
2. Cek token.json
   ├── Token valid → pakai langsung
   ├── Token expired → refresh via /auth/token
   └── Refresh gagal → login OTP (auto: IMAP Gmail)
3. Tampilkan dashboard (balance, rates, dll)
4. Cek claimable
   ├── Ya → trigger ads → tunggu → claim → simpan state
   └── Tidak → info next claim time
5. Exit (one-shot, gak loop)
```

## Login Flow (hanya kalau session invalid)

```
1. GET /auth/loginId-exist-check/{id}     → cek ID ada
2. POST /auth/check-passcode?v=2          → verifikasi passcode
3. POST /auth/send-otp-email-verify-login → kirim OTP ke email
4. IMAP poll Gmail inbox                  → baca OTP dari email
5. POST /auth/check-otp-email-verify-login?v=2 → verifikasi OTP
6. Simpan accessToken + refreshToken ke token.json
```

## Claim Flow

```
1. GET /token/check-is-claimable → cek bisa claim
2. [JITTER] tunggu 30-120 detik (human-like)
3. GET /auth/current-user-full → catat balance sebelum
4. GET /token/get-random-ads-mining-new → trigger ads
5. Tunggu timeRetry + 5 detik
6. POST /token/claim-airdrop → claim ITLG
7. Hitung selisih balance → simpan ke claim_state.json
8. Tampilkan dashboard
```

## API Endpoints

| Endpoint | Method | Fungsi |
|----------|--------|--------|
| /auth/loginId-exist-check/{id} | GET | Cek login ID |
| /auth/check-passcode?v=2 | POST | Verifikasi passcode |
| /auth/send-otp-email-verify-login | POST | Kirim OTP |
| /auth/check-otp-email-verify-login?v=2 | POST | Verifikasi OTP |
| /auth/token | POST | Refresh token |
| /auth/current-user-full?include=userInfo,token,isClaimable | GET | User info |
| /token/check-is-claimable | GET | Cek claimable |
| /token/get-random-ads-mining-new | GET | Trigger ads |
| /token/claim-airdrop | POST | Claim ITLG |

## HTTP Headers (Android Mimic)

```
User-Agent: okhttp/4.12.0
Content-Type: application/json
version: 5.0.0
x-platform: android
x-model: [random device]
x-brand: [random brand]
x-system-name: Android
x-bundle-id: org.ai.interlinklabs.interlinkId
x-unique-id: [deviceId]
x-device-id: [deviceId]
x-date: [timestamp ms]
x-content-hash: [SHA256 body, base64]
Authorization: Bearer [token]
```

## Cron Setup (Hermes Agent)

```
Schedule: 5 0,4,8,12,16,20 * * *  (UTC) = 07:05, 11:05, 15:05, 19:05, 23:05, 03:05 WIB

Prompt: Run ITLG auto-claim. Go to SKILL_DIR/scripts, run python3 claim.py, and report results (ITLG claimed, current balance, next claim time). DO NOT run --login unless token expired and refresh failed.

Deliver: telegram
```

## Prerequisites

```bash
# Python 3 + requests (biasanya udah ada)
python3 -c "import requests" || pip3 install requests
```

## Step-by-Step Setup (Untuk Agent Lain)

### Step 1: Temukan Skill Directory

```bash
SKILL_DIR=$(find ~/.hermes/skills -name "claim.py" -path "*/interlink/*" -exec dirname {} \; | head -1)
echo "Skill dir: $SKILL_DIR"
```

### Step 2: Buat config.json

Collect dari user:
- Login ID (angka)
- Passcode (6 digit)
- Email Gmail terdaftar
- Gmail App Password (16 char)

Buat config:

```bash
cd "$SKILL_DIR/scripts"
cp config.json.example config.json
# Edit config.json dengan credentials user
```

Atau generate via Python:

```python
import json, hashlib
loginId = "USER_LOGIN_ID"  # dari user
config = {
    "loginId": loginId,
    "passcode": "USER_PASSCODE",
    "email": "user@gmail.com",
    "imapPassword": "xxxx xxxx xxxx xxxx",
    "deviceId": hashlib.md5(loginId.encode()).hexdigest()[:16]
}
with open("config.json", "w") as f:
    json.dump(config, f, indent=2)
```

### Step 3: Login (First Time Only)

```bash
cd "$SKILL_DIR/scripts"
python3 claim.py --login
```

Ini akan:
1. Kirim OTP ke email
2. Baca OTP dari Gmail via IMAP
3. Verifikasi OTP
4. Simpan token ke token.json

### Step 4: Verify

```bash
cd "$SKILL_DIR/scripts"
python3 claim.py --status
```

Harusnya tampilkan dashboard dengan balance.

### Step 5: Test Claim

```bash
cd "$SKILL_DIR/scripts"
python3 claim.py
```

Kalau belum waktunya claim, akan tampilkan next claim time.

### Step 6: Setup Cron (Opsional)

Pakai Hermes cron tool:
- Schedule: `5 0,4,8,12,16,20 * * *`
- Deliver: telegram
- Prompt: self-contained, gak butuh context

## Pitfalls

### Email OTP Gak Masuk

- Interlink email service kadang down
- Cek: kirim OTP manual, cek inbox Gmail
- Kalau gak masuk = server down, tunggu

### Token Expired Tapi Refresh Gagal

- Refresh token juga bisa expired (biasanya 30 hari)
- Kalau refresh gagal, script auto-login OTP
- Kalau OTP juga gagal = email service down

### Rate Limit EMAIL_SEND

- API return 400 "EMAIL_SEND" kalau OTP dikirim terlalu cepat
- Tunggu 60 detik antara percobaan
- Script auto-retry 3x dengan delay

### IMAP Error

- Pastikan IMAP enabled di Gmail Settings
- Pastikan App Password bener (16 char, BUKAN password Gmail)
- Gak bisa pakai password Gmail biasa

### Claim TOO_EARLY

- Udah claim cycle ini, tunggu 4 jam berikutnya
- Normal behavior, bukan error

## Security Notes

- config.json chmod 600 (owner only)
- token.json chmod 600 (owner only)
- JANGAN commit config.json ke git
- config.json.example aman di-share (data dummy)
- Gak ada data dikirim ke server lain selain Interlink API
- Gmail App Password = limited scope, bukan full access

## Disclaimer

- Bot ini untuk educational purposes
- Interlink bisa ganti API kapan saja
- Pakai resiko sendiri
