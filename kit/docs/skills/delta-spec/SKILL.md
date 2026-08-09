---
name: delta-spec
type: documentation
category: documentation
description: Spec only the change (ADDED/MODIFIED/REMOVED) for brownfield work. Use instead of rewriting the full product spec.
usedFor: [spec, brownfield, change]
appliesTo: [all]
requiredKnowledge: [requirements]
conflicts: []
---

# Skill: Delta Spec

## Quando usar

- Mudança em codebase existente  
- Item de `### Features` que altera comportamento localizado  

## Quando NÃO usar

- Greenfield total  
- Hotfix de 1 linha (use hotfix-path)  

## Formato

Template: `kit/templates/delta-spec.md`

```markdown
## Delta
### ADDED
- …
### MODIFIED
- …
### REMOVED
- …
```

Arquivo em `.ai/specs/` (máquina). Humano aprova no fluxo do agent; backlog continua em `### Features`.

## Critérios de saída

- [ ] Delta testável e revisável em segundos  
- [ ] DoD observável  
