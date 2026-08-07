# Skills (jojo-ai)

Competências reutilizáveis para agentes. **O usuário do SPECKIT não edita estes arquivos** — só `agents.md`.

| Skill | Categoria | Obrigatória |
| --- | --- | --- |
| [tdd.md](./tdd.md) | quality | não |
| [code-review.md](./code-review.md) | quality | não (gate de fase) |
| [ui-ux.md](./ui-ux.md) | design | se houver UI |
| [ducks-pattern.md](./ducks-pattern.md) | organization | **sim** |

## Discovery

- Catálogo gerado: `../../skills-registry.json`
- Recomendações por fase: `../recommendations.json`
- Validar: `npm run validate:skills`
- Regenerar registry: `npm run generate:registry`

## Nova skill (mantenedor)

1. Copie o frontmatter de uma skill existente  
2. Inclua **Quando usar** e **Quando NÃO usar**  
3. Siga `../skill-validator.md`  
4. Rode `npm run sync`  
