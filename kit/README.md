# jojo-ai — kit interno

Máquina do SPECKIT. **Humanos não abrem isto no dia a dia.**

Operação: **`./jojo`** + agent de código. Raiz: `agents.md`, `system-design.md`, `CHANGELOG.md`.

## Layout

```
kit/
├── docs/agents/           # runbooks de fase
├── docs/skills/<id>/SKILL.md
├── docs/recommendations.json
├── scripts/               # generate + validate
├── templates/
├── generated/             # registry + context
└── package.json
```

## Comandos

```bash
./jojo sync          # na raiz do app ou fonte
# ou
cd kit && npm run sync
```

## Progressive disclosure

| L1 | registry (name + description) |
| L2 | SKILL.md body |
| L3 | references/ etc. |
