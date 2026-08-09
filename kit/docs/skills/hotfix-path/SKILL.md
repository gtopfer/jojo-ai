---
name: hotfix-path
type: process
category: process
description: Short lifecycle for small bugfixes and chores. Use when change is tiny and well-specified; skip full 8-phase theatre.
usedFor: [hotfix, bugfix, chore]
appliesTo: [all]
requiredKnowledge: [debugging]
conflicts: []
---

# Skill: Hotfix Path

## Quando usar

- Bugfix 1–3 arquivos, comportamento claro  
- Chore (lint, rename) sem UI de produto  
- Regressão com teste reprodutível  

## Quando NÃO usar

- Feature nova com UI/contratos  
- Escopo incerto  

## Fluxo curto

```
classificar (feature vs hotfix) — 1 confirmação
  → opcional: 1 teste RED
  → implementar mínimo
  → suíte do projeto verde + code-review skill
  → marcar done (Features [x] se estava no backlog, ou só CHANGELOG)
```

Ainda exige qualidade (testes/review). Se explodir → reclassifique como feature e use o loop completo + `./jojo run`.

## Anti-padrões

| Evite | Faça |
|-------|------|
| 8 fases para typo | Path curto |
| Hotfix de redesign | Feature completa |
| Pular suíte | Sempre validar |

## Critérios de saída

- [ ] Suíte / review ok  
- [ ] Humano ciente do path  
