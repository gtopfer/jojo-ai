# jojo-ai

Framework agnóstico para agentes de IA colaborarem em desenvolvimento.

**Produto:** `jojo-ai` · **CLI:** `./jojo`

## Componentes

- **agents.md** — Régua universal (8 fases, 6 agentes, 5 princípios)
- **docs/agents/** — Runbooks especializados por papel
- **docs/skills/** — Competências reutilizáveis (TDD, code-review, ui-ux)
- **templates/** — Scaffolding para specs e arquitetura
- **CLI `./jojo`** — status, sync, approve, reject, review, propose, init

## Como Usar

1. Copie `agents.md` (e o kit) para seu projeto
2. Leia seu papel em `docs/agents/<papel>.md`
3. Use templates de `templates/` conforme necessário
4. Customize `docs/` com seu stack
5. Use `./jojo <comando>` para governar fases e review

## Integração Mínima

```bash
cp agents.md seu-app/
mkdir -p seu-app/.ai/specs seu-app/.ai/guidelines
cp -r templates/* seu-app/.ai/
```

## Status

✅ Production-ready | Agnóstico | Minimalista
