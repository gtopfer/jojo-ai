---
name: jojo-run
description: >
  Read agents.md ### Features, pick the next pending feature, and start
  the SPECKIT implementation loop. Use when the user runs /jojo-run,
  says "jojo run", "próxima feature", "implementar backlog", or
  "tem feature nova no agents.md".
---

# /jojo-run

Lê o backlog em **`agents.md` → Seção 1 → `### Features`** e inicia o trabalho na **primeira** feature `- [ ]`.

## Passos obrigatórios

### 1. CLI (fonte da verdade da fila)

Na raiz do projeto:

```bash
./jojo run
# opcional: ./jojo run --json
```

Isso atualiza:
- `.ai/jojo-run.json` — `next_feature`, pending, done
- `.ai/state.md` — resumo legível

Se não houver `./jojo`, instale com `/jojo-init` primeiro.

### 2. Ler contexto

Sempre leia **antes** de codar:

1. `agents.md` (Seção 1 + ### Features)
2. `system-design.md`
3. `.ai/jojo-run.json` (próxima feature)

### 3. Apresentar e pedir OK

Mostre ao humano:

```text
Próxima feature (agents.md):
  <título da feature>

Plano resumido:
  - ...
OK para eu implementar o ciclo completo?
```

**Não comece a codar sem OK explícito** (a menos que o humano já tenha pedido “pode implementar”).

### 4. Executar o loop (8 fases)

Siga `agents.md` Seção 2 e os runbooks em `kit/docs/agents/`:

`draft → spec_approved → ux_approved → tech_approved → test_red → code_review → tested → done`

- PM: requisitos testáveis  
- UX: se houver UI (senão N/A em system-design / spec)  
- Architect: alinhar a `system-design.md`  
- QA: TDD RED  
- Dev: GREEN + `kit/docs/skills/*`  
- QA validação → PM DoD  

### 5. Ao concluir

1. Em `agents.md` → `### Features`, troque `- [ ]` por `- [x]` nessa feature  
2. Atualize `CHANGELOG.md`  
3. Rode `./jojo run` de novo (próxima pendente ou “nenhuma”)

## Regras

- **Fonte do backlog = só `### Features` no agents.md** — não peça outro arquivo ao humano.
- Specs detalhadas em `.ai/specs/` são opcionais/internas.
- Respeite Ducks Pattern e `system-design.md`.
