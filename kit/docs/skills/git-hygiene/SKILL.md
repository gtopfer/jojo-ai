---
name: git-hygiene
type: development
category: quality
description: Atomic commits, clear messages, no force-push to shared main. Use before finishing a feature or opening a PR.
usedFor: [git, commit, pr]
appliesTo: [all]
requiredKnowledge: [git]
conflicts: []
---

# Skill: Git Hygiene

## Quando usar

- Antes de marcar feature `[x]`  
- Após loop autônomo com vários patches  

## Quando NÃO usar

- Exploração local descartável  

## Regras

1. Commits atômicos  
2. Mensagem com o porquê  
3. Sem secrets / `.env`  
4. Sem force-push em main sem OK  

## Critérios de saída

- [ ] Diff revisado  
- [ ] Branch/mensagens ok  
