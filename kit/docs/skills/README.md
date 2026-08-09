# Skills (jojo-ai)

Layout **Agent Skills**: `kit/docs/skills/<id>/SKILL.md`.  
Humano **não** edita isto — CLI + agent de código; raiz: `agents.md`, `system-design.md`, `CHANGELOG.md`.

| Skill | Categoria | Notas |
| --- | --- | --- |
| [tdd](./tdd/SKILL.md) | quality | RED→GREEN |
| [code-review](./code-review/SKILL.md) | quality | suíte do app + diff |
| [autonomous-loop](./autonomous-loop/SKILL.md) | quality | máx. 3× |
| [ui-ux](./ui-ux/SKILL.md) | design | se houver UI |
| [microcopy](./microcopy/SKILL.md) | design | copy |
| [a11y](./a11y/SKILL.md) | design | acessibilidade |
| [ducks-pattern](./ducks-pattern/SKILL.md) | organization | **obrigatório** |
| [onboard](./onboard/SKILL.md) | process | bootstrap |
| [handoff](./handoff/SKILL.md) | process | anti context-rot |
| [hotfix-path](./hotfix-path/SKILL.md) | process | bugfix curto |
| [delta-spec](./delta-spec/SKILL.md) | documentation | brownfield |
| [api-contract](./api-contract/SKILL.md) | architecture | APIs |
| [git-hygiene](./git-hygiene/SKILL.md) | quality | commits |
| [security-basics](./security-basics/SKILL.md) | quality | review sensível |

## Discovery

- L1: `../../generated/skills-registry.json`  
- Recommendations: `../recommendations.json`  
- Validar: `./jojo sync` ou `cd kit && npm run validate:skills`  
