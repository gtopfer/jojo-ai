```
┌──────────────────────────────────────────────────┐
│                                                  │
│      ██╗ ██████╗      ██╗ ██████╗                │
│      ██║██╔═══██╗     ██║██╔═══██╗               │
│      ██║██║   ██║     ██║██║   ██║               │
│ ██   ██║██║   ██║██   ██║██║   ██║               │
│ ╚█████╔╝╚██████╔╝╚█████╔╝╚██████╔╝               │
│  ╚════╝  ╚═════╝  ╚════╝  ╚═════╝                │
│                    · a i ·                       │
│                                                  │
│     ★  spec  →  design  →  ship  ★               │
│        agentes com régua · você no controle      │
│                                                  │
└──────────────────────────────────────────────────┘
```

# jojo-ai

SPECKIT minimalista para agentes de IA.

**Você edita só isto na raiz:**

| arquivo | pra quê |
| --- | --- |
| [`agents.md`](./agents.md) | produto + processo |
| [`system-design.md`](./system-design.md) | arquitetura + design system |
| [`CHANGELOG.md`](./CHANGELOG.md) | feito vs. falta |

O resto mora em [`kit/`](./kit/) (agents, skills, scripts). Detalhes do kit: [`kit/README.md`](./kit/README.md).

```bash
# 1) preencha agents.md + system-design.md
# 2) abra seu agente de IA e diga: "siga agents.md"
# (opcional, agentes/CI)
cd kit && npm run sync
```

**Licença:** [GPL-3.0](./LICENSE)
