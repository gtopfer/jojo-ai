---
name: security-basics
type: development
category: quality
description: Baseline security — secrets, input validation, auth. Use during code-review on sensitive changes.
usedFor: [security, review]
appliesTo: [backend, frontend]
requiredKnowledge: [security-basics]
conflicts: []
---

# Skill: Security Basics

## Quando usar

- Auth, PII, uploads, admin, pagamentos  
- Complemento de code-review  

## Quando NÃO usar

- Docs puras sem superfície de ataque  

## Checklist

- [ ] Sem secrets no código/logs  
- [ ] Validação na borda  
- [ ] AuthZ em rotas sensíveis  
- [ ] Queries/ORM seguros  

## Critérios de saída

- [ ] Críticos ok ou risco documentado  
