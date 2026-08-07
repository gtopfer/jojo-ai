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
│     ★  init  →  features  →  run  ★              │
│        agentes com régua · você no controle      │
│                                                  │
└──────────────────────────────────────────────────┘
```

# jojo-ai

SPECKIT minimalista para agentes de IA.

## Dois comandos

```bash
# 1) Instala OU atualiza o kit no projeto (detecta versão antiga sozinho)
./jojo init /caminho/do/seu-projeto
#    se já tiver jojo: remove kit/CLI gerenciados e reinstala; preserva agents.md

# 2) Lê agents.md → ### Features e mostra a próxima a implementar
cd /caminho/do/seu-projeto
./jojo run

# extra
./jojo detect .    # jojo já instalado? qual versão?
```

No chat do Grok (skills do projeto):

- **`/jojo-init`** — instala dependências/kit no repo  
- **`/jojo-run`** — mapeia features pendentes e começa o loop  

## Você edita na raiz

| arquivo | pra quê |
| --- | --- |
| [`agents.md`](./agents.md) | projeto + **`### Features`** (backlog) |
| [`system-design.md`](./system-design.md) | arquitetura + design system |
| [`CHANGELOG.md`](./CHANGELOG.md) | histórico (agentes atualizam) |

Fluxo: escreve feature em `agents.md` → `./jojo run` → IA pede OK → implementa.

Kit interno: [`kit/`](./kit/). CLI: [`jojo`](./jojo).

**Licença:** [GPL-3.0](./LICENSE)
