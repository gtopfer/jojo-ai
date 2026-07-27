# Changelog

Todas as mudanças notáveis deste projeto são documentadas aqui. O formato segue livremente o [Keep a Changelog](https://keepachangelog.com/).

Cada entrada deve descrever impacto (o que mudou para usuários/sistema), não detalhe de implementação.

## [Não Lançado]

### Adicionado
- **Guia do Usuário contínuo** (`docs/GUIA-DO-USUARIO.md`): jornada didática do init ao done, por fase, com comandos e frases para o chat
- **Pacote de maturidade**: `doctor`, `log`, `activate`, `hotfix`, `propose` com flags, `sync --migrate-lifecycle`, heurísticas UI no `review`, testes em `tests/`, CI GitHub Actions, hook `hooks/pre-commit`, skill `microcopy`, templates ADR/tech-spec, métricas `.ai/metrics.jsonl`
- **Trilha completa de UI/UX**: status `ux_approved`, fase `ux`, agent `ux-designer.agent.md`, skill `ui-ux.md`, `design-premises.md` operacional
- Comandos `./devkit sync` (specs órfãs → state) e `./devkit reject` (retrocesso de fase)
- Spec de baseline `SPEC-000` (`000_setup.md`) alinhada ao `state.md`
- Baseline técnica do produto DevKit-AI em `.ai/technical-spec.md`
- Sanitização no `./devkit init`: projetos-alvo recebem slate limpo (sem specs/ADRs do meta-repo)
- Detecção de stack Python via shebang do script `devkit` (sem extensão `.py`)

### Alterado
- Agents PM/QA/Developer/Squad Lead: paths corretos, Gherkin, DoD docs, `reject` em falha, skill code-review no Developer
- Skill TDD: deriva da **spec ativa** em `.ai/specs/` + `.feature`, não só do `template.specs`
- **Rewrite** de agents e skills: entradas, gates de approve/reject, anti-padrões, formatos de handoff e índices em `agents/README.md` + `skills/README.md`

### Corrigido
- Árvore de diretórios do README incompleta (faltavam `guidelines/`, `features.feature`, `tdd.md`, `SYSTEM_PROMPT.md`)
- Tabela do ciclo de vida desalinhada com a máquina de estados real (`pm` → `architect` → `qa_tdd` → …)
- `SYSTEM_PROMPT.md`: referência à seção errada do README e contagem incorreta de guidelines (4 → 5)
- `features.feature` com exemplo de “login” de app fictício; substituído por placeholder neutro
- Coluna do `state.md` renomeada de “Próxima Fase” para “Fase Ativa” (semântica correta)
- `./devkit review` falsos positivos de TODO/FIXME em Markdown/docs e na própria CLI; varredura limitada a comentários em arquivos de código
- `./devkit init` crash ao comparar destino com `abspath` em macOS (`/var` vs `/private/var`); agora usa `realpath`
- `./devkit sync` corrompia paths `.ai/...` com `lstrip("./")`; normalização corrigida

### Adicionado (histórico)
- Estrutura inicial do projeto (Dev ToolKit)
