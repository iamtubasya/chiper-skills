# chiper-skills

Skill ecosystem untuk **Hermes Agent** — security, automation, dan utilities.

## Struktur

```
chiper-skills/
├── chiper-cyber/       ← 144 security skill domains (302 tools)
├── 9router/            ← Router automation
├── interlink/          ← Interlink utilities
└── README.md           ← This file
```

## Skill Packs

| Pack | Description | Skills |
|------|-------------|--------|
| [chiper-cyber](chiper-cyber/) | Security pentest, exploit dev, OSINT, forensics | 144 |
| 9router | Router automation | - |
| interlink | Interlink utilities | - |

## Quick Start — chiper-cyber

```bash
git clone https://github.com/iamtubasya/chiper-skills.git /tmp/chiper-skills
cp -r /tmp/chiper-skills/chiper-cyber ~/.hermes/skills/
bash ~/.hermes/skills/chiper-cyber/chiper-bootstrap/scripts/install.sh
```

Lihat [chiper-cyber/SKILL.md](chiper-cyber/SKILL.md) untuk dokumentasi lengkap.

## License

Unauthorized access to computer systems is illegal.
Use these skills only on systems you own or have explicit written permission to test.
