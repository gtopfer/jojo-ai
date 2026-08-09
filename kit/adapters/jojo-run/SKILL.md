---
name: jojo-run
description: >
  Read agents.md ### Features, pick the next pending feature, start SPECKIT loop.
  Use when the user runs jojo run or asks for the next backlog feature.
---

# jojo run (adapter)

Lê o backlog em **`agents.md` → `### Features`** e inicia a **primeira** `- [ ]`.  
**LLM-agnóstico:** este adapter só descreve o protocolo; qualquer agent executa.

## Passos

### 1. CLI

```bash
./jojo run
# opcional: ./jojo run --json
# opcional: ./jojo sync
```

Atualiza `.ai/jojo-run.json` e resumo em `.ai/state.md`.  
A CLI **não** implementa sozinha.

### 2. Contexto

1. `agents.md` (Seção 1 + Features)  
2. `system-design.md`  
3. `.ai/jojo-run.json`  
4. `kit/docs/agents/squad-lead.agent.md`  

### 3. OK humano → loop

8 fases (ou hotfix-path).  
Review = suíte do **app** + skill `code-review`.  
Done = `- [x]` em Features + CHANGELOG + `./jojo run`.

## Regras

- Backlog = só `### Features`  
- Sem arquivos de config extras  
- Sem assumir um fornecedor de LLM  
