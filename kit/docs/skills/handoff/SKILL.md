---
name: handoff
type: process
category: process
description: Compact phase handoff so the next turn trusts disk not chat history. Use at every phase change or session resume.
usedFor: [orchestration, session, context]
appliesTo: [all]
requiredKnowledge: []
conflicts: []
---

# Skill: Handoff (anti context-rot)

## Quando usar

- Troca de fase no loop de 8 fases  
- Retomar após `./jojo run` em nova sessão  
- Antes de encerrar o turno do agent de código  

## Quando NÃO usar

- Dentro do micro-loop de fix (use autonomous-loop)  

## Formato (≤ ~15 linhas)

```text
[Handoff] Feature: <título de ### Features>
Path: feature | hotfix
Fase: <status> · Agente: <papel>
Artefatos: .ai/specs/… · system-design.md · .ai/jojo-run.json
Gate cumprido: …
Próximo gate: …
Como validar: <comando da suíte do app>
Não re-ler: transcript inteiro — confie no disco
```

## Regras

1. Disco > chat (`agents.md`, `system-design.md`, `.ai/jojo-run.json`)  
2. Um papel de agente por vez  
3. Após done: `- [x]` em Features + CHANGELOG  

## Critérios de saída

- [ ] Próximo turno sabe o que ler sem o histórico completo  
