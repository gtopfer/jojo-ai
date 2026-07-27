# Estado do Desenvolvimento (Task Tracker)

Este arquivo é lido e atualizado automaticamente pela IA para rastrear o status de cada especificação no diretório `.ai/specs/` e gerenciar a transição de fases.

## Como funciona
1. **Rastreamento Automático**: A IA verifica os arquivos na pasta `.ai/specs/` e atualiza a tabela abaixo com o status correspondente.
2. **Ciclo de Vida (Fases)**:
   - `draft` (Rascunho inicial do PM)
   - `spec_approved` (Requisitos de negócio aprovados; aguardando UI/UX)
   - `ux_approved` (UI/UX aprovada; aguardando arquitetura técnica)
   - `tech_approved` (Especificação técnica aprovada; aguardando testes TDD)
   - `test_red` (Testes TDD escritos e falhando; aguardando implementação)
   - `code_review` (Implementado; validação de QA)
   - `tested` (Testes ok; validação de DoD do PM)
   - `done` (Entregue, documentado e concluído)

---

## Lista de Especificações Ativas

| Código | Título da Spec | Caminho do Arquivo | Status Atual | Fase Ativa | Última Atualização |
|--------|----------------|-------------------|--------------|------------|---------------------|
| SPEC-000 | Configuração Inicial | `.ai/specs/000_setup.md` | `done` | `done` | 2026-07-26 |

---

## Histórico de Execuções Recentes

* **2026-07-26**: Pacote de maturidade: doctor, log, activate, hotfix, propose flags, testes CLI, microcopy, CI/hooks.
* **2026-07-26**: UI/UX completo: fase `ux_approved`, agent `ux-designer`, skill `ui-ux`, design-premises e CLI.
* **2026-07-18**: Inicialização do repositório devkit-ai.
