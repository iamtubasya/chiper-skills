# Airdrop

Auto-claim & automation skills untuk crypto airdrops.

Default: scripts run on local machine, cron-ready.

## Skills

| Skill | Description | Stack |
|---|---|---|
| **[interlink](interlink/)** | Auto-claim $ITLG (Interlink Gold Token). OTP login → refresh token → auto-claim every 4 hours. Android-mimic headers, human-like jitter. | Python · IMAP |

## Install

```bash
cp -r airdrop ~/.hermes/skills/
```

## Add New Airdrop Skill

```bash
mkdir airdrop/new-airdrop-name
# Add SKILL.md + scripts/
```

## Author

**ChiperFlux** (Chiper-Cyber)
