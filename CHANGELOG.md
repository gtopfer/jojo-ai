# CHANGELOG

Rastreamento do projeto (o que foi feito vs o que falta).  
Atualizado por agentes com aceite humano. **Fica na raiz** junto com `agents.md` e `system-design.md`.

## [Unreleased]

### Implemented
- [x] SPECKIT: `agents.md` + `system-design.md` + `CHANGELOG.md` na raiz
- [x] Kit interno em `kit/` (agents, skills, scripts, templates)
- [x] CLI `./jojo` com `init` + `run` (init detecta e atualiza instalação existente)
- [x] Skills Grok `/jojo-init` e `/jojo-run`
- [x] README mínimo com ASCII + LICENSE GPL-3.0
- [x] Validação: paths `kit/`, 6 skills OK, CI `npm run sync`

### To Do (Validated by Human)
- [ ] Preencher Seção 1 de `agents.md` para o projeto real
- [ ] Preencher `system-design.md` do projeto
- [ ] Expandir CLI: approve / reject / review / status
