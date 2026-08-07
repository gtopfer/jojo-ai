# AGENTS.MD

Régua universal + Especificação do Projeto (em um arquivo).

Copie este arquivo para seu projeto novo, preencha com suas especificações, e rode.

---

## 🎯 Como Usar

1. Copie jojo-ai para seu projeto novo
2. Edite este arquivo (`agents.md`) com especificações do seu projeto
3. Agentes lêem este arquivo
4. Agentes validam com você antes de executar
5. Tudo é rastreado em `CHANGELOG.md`

---

## 📋 SEÇÃO 1: PROJETO (Preencha Aqui)

### Projeto: [Nome do Projeto]

**Stack:**

- Frontend: [tecnologia]
- Backend: [tecnologia]
- Database: [tecnologia]
- CI/CD: [tecnologia]

**Contexto:**
[Descrição breve do que o projeto faz]

**Usuários:**
[Quem usa]

**Guardrails Obrigatórios:**

- Ducks Pattern (obrigatório)
- [Seu guardrail 1]
- [Seu guardrail 2]

**Convenções:**

- Naming: [padrão]
- Code style: [padrão]
- [Sua convenção]

---

## 📋 SEÇÃO 2: REGRAS DE AGENTES (Não Altere)

### 8 Fases

```
draft → spec_approved → ux_approved → tech_approved → test_red → code_review → tested → done
```

### 6 Agentes

| Fase | Agente | Responsabilidade |
| --- | --- | --- |
| draft | Product Manager | Escrever spec com DoR/DoD |
| spec_approved | UX Designer | Desenhar interface (§3) |
| ux_approved | Architect | Modelar tech spec |
| tech_approved | QA | Testes RED (TDD) |
| test_red | Developer | Implementar (GREEN + REFACTOR) |
| code_review | QA | Validar testes verdes |
| tested | Product Manager | Validar DoD |

### 3 Skills

- **docs/skills/tdd.md** — RED → GREEN → REFACTOR
- **docs/skills/code-review.md** — Validação automatizada + manual
- **docs/skills/ui-ux.md** — Design, acessibilidade, estados
- **docs/skills/ducks-pattern.md** — Code organization (obrigatório)

### 5 Princípios

1. **Simplicidade** — Mude apenas o necessário
2. **Sem Laziness** — Encontre causas raiz
3. **Impacto Mínimo** — Zero bugs secundários
4. **Reversibilidade** — Confirme operações destrutivas
5. **Verificação** — Testes verdes antes de pronto

---

## 🔄 FLUXO DE EXECUÇÃO (Para Agentes)

### Quando Agente Lê Este Arquivo

```
1. Lê SEÇÃO 1 (Projeto)
   ↓
2. Lê SEÇÃO 2 (Regras)
   ↓
3. Verifica CHANGELOG.md
   ↓
4. Identifica o que já foi feito
   ↓
5. Identifica o que precisa ser feito
   ↓
6. Se algo novo:
   a. Apresenta para humano
   b. Aguarda validação
   c. Se OK: Executa
   d. Registra em CHANGELOG.md
```

### Checklist Antes de Executar Qualquer Feature

Agente DEVE:

- [ ] Ler agents.md (projeto + regras)
- [ ] Ler CHANGELOG.md (o que já foi feito)
- [ ] Verificar se feature já existe no CHANGELOG
- [ ] Se É NOVA: Apresentar para humano
- [ ] AGUARDAR validação do humano
- [ ] Após OK: Executar
- [ ] Registrar em CHANGELOG.md

---

## 📊 CHANGELOG.MD (Rastreamento)

Cada feature executada DEVE ser registrada:

```markdown
# CHANGELOG

## [1.0.0] - 2026-08-07

### Implemented
- [x] Project setup
- [x] Authentication (Basic)
- [x] User CRUD
- [x] API endpoints

### To Do (Validated by Human)
- [ ] Payment integration
- [ ] Email notifications
- [ ] Admin dashboard
```

---

## 🎯 Exemplo Completo

### SEÇÃO 1: Seu Projeto

```
## Projeto: E-commerce Platform

**Stack:**
- Frontend: React 18
- Backend: Node.js + Express
- Database: PostgreSQL
- CI/CD: GitHub Actions

**Contexto:**
Plataforma de e-commerce para vendas online

**Usuários:**
- Compradores
- Vendedores
- Admins

**Guardrails:**
- Ducks Pattern (obrigatório)
- TypeScript strict mode
- 100% test coverage
- Sem secrets hardcoded
```

### CHANGELOG.md

```
## [1.0.0] - 2026-08-07

### Implemented
- [x] Project setup
- [x] User authentication
- [x] Product catalog (list, detail, search)

### To Do (Waiting for Validation)
- [ ] Shopping cart
- [ ] Checkout flow
- [ ] Payment integration
```

### Agente Lê Tudo

```
Agente lê agents.md
  → Vê que precisa fazer "Shopping cart"
  → Vê que NÃO está marcado como feito em CHANGELOG
  → Apresenta para humano:
     "Próxima feature: Shopping cart
      - Adicionar itens ao carrinho
      - Ver total
      - Validar quantidade
      OK para implementar?"
  ↓ (Aguarda resposta)
  → Humano valida: "SIM, pode fazer"
  ↓
  → Agente implementa (segue 8 fases)
  ↓
  → Quando pronto: Atualiza CHANGELOG
     - [x] Shopping cart
```

---

## ⚙️ Prático

### Para Agente Implementar Algo

1. **Lê agents.md** (este arquivo)
2. **Procura em CHANGELOG.md** se feature existe
3. **Se NÃO existe:**

   ```
   Agente: "Achei que precisa de X.
            Requisitos:
            - [req 1]
            - [req 2]
            
            OK para eu implementar?"
   
   Humano: "SIM" ou "NÃO"
   
   Se SIM:
     → Agente faz tudo (fases)
     → Atualiza CHANGELOG.md com [x]
   ```

4. **Se JÁ existe:**

   ```
   Agente: "Vejo que X já foi feito."
           → Pula para próxima feature
   ```

---

## 📌 Resumo

- **agents.md** = Tudo (projeto + regras + como executar)
- **CHANGELOG.md** = O que foi feito vs o que falta
- **Fluxo:** Agente lê agents.md → Verifica CHANGELOG → Se novo, apresenta humano → Aguarda OK → Executa → Registra

---

**Versão:** 1.0 | **Status:** Production-ready
