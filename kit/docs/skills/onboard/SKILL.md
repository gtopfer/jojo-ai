---
name: onboard
type: process
category: process
description: Interview and fill agents.md Seção 1 + system-design.md once. Use on first setup or when placeholders remain.
usedFor: [bootstrap, setup, interview]
appliesTo: [all]
requiredKnowledge: [product-context]
conflicts: []
---

# Skill: Onboard

> **Quando:** placeholders em Seção 1 / system-design.  
> **Grava só:** `agents.md` (Seção 1) e `system-design.md`.  
> **Depois:** humano roda `./jojo run` com o agent de código no app.

## Quando usar

- Projeto recém-`init`  
- Placeholders (`[tecnologia]`, `[Nome do Projeto]`, …)  
- Antes da primeira feature se o contexto estiver vazio  

## Quando NÃO usar

- Produto/design já estáveis  
- Só para implementar item do backlog (use `./jojo run`)  

## Fluxo

1. Detectar buracos em Seção 1 e `system-design.md`  
2. Entrevistar (5–10 perguntas por rodada): produto, usuários, stack, UI, guardrails  
3. Gravar nos 2 arquivos  
4. Pedir OK humano  
5. `cd kit && npm run sync` (ou `./jojo sync` se disponível)  
6. Garantir backlog em `### Features` e orientar `./jojo run`  

## Anti-padrões

| Evite | Faça |
|-------|------|
| Criar stack.md / profile.json | Só 3 MDs raiz |
| Inventar design system no vácuo | Gravar em system-design com OK |

## Critérios de saída

- [ ] Placeholders críticos resolvidos ou “a definir” explícito  
- [ ] OK humano  
- [ ] Pronto para `./jojo run`  
