# Especificação Técnica: [Nome do Projeto ou Feature]

**Última atualização:** AAAA-MM-DD
**Versão:** X.Y
**Veredito arquitetural:** Confirmado | Desafiado (ver seção 9)

> Preenchido e mantido pelo agente Architect (`.ai/agents/architect.agent.md`). É o par técnico de `.ai/template.specs` (que é do PM, em linguagem de negócio) — juntos, esses dois arquivos são as únicas duas specs deste kit: **o quê** (requisito do app) e **como** (construção técnica).

## 1. Visão Geral
[2-4 frases: o que o sistema/feature faz e que problema técnico resolve]

## 2. Diagrama de Arquitetura

[Diagrama Mermaid principal — `graph TD` para dependências entre camadas]

## 3. Fluxo Principal

[`sequenceDiagram` ou `flowchart` descrevendo o caminho feliz]

## 4. Stack

| Camada | Tecnologia | Versão | Justificativa |
|--------|-----------|--------|---------------|
| ... | ... | ... | ... |

## 5. Componentes & Contratos de Interface

| Componente | Responsabilidade | Tecnologia |
|-----------|-----------------|------------|
| ... | ... | ... |

```typescript
// Contratos de interface entre camadas — o QA usa isto para escrever mocks corretos
```

## 6. Dependências Externas

| Sistema | Tipo | Protocolo | Observações |
|--------|------|----------|-------|
| ... | ... | ... | ... |

## 7. Modelo de Dados

[`erDiagram` — omitir se não houver persistência]

## 8. Riscos e Mitigações

| Risco | Severidade | Mitigação |
|-------|-----------|-----------|
| ... | 🔴/🟡/🟢 | ... |

## 9. Histórico de Decisões Arquiteturais

Cada decisão vira uma entrada nova aqui — mais recente no topo. Substitui ADRs em arquivos separados: o histórico completo vive neste único arquivo.

### AAAA-MM-DD — [Título da decisão]
**Contexto:** [por que esta decisão foi necessária]
**Decisão:** [o que foi decidido e como será implementado]
**Alternativas consideradas:** [alternativa → por que foi descartada]
**Trade-offs:** Ganha-se: [...] / Perde-se: [...]
**Consequências:** [impacto prático no código e em decisões futuras]

## 10. Histórico de Versões

| Versão | Data | Mudança |
|--------|------|---------|
| 1.0 | AAAA-MM-DD | Criação inicial |
