# AGENTS.MD

Régua universal + Especificação do Projeto.

---

## 🎯 Como Usar (humano)

1. Preencha **Seção 1** (projeto + **Features**)
2. Preencha **`system-design.md`** (arquitetura / design system)
3. Diga à IA: **"siga agents.md"**
4. A IA lê as Features abaixo, mapeia e começa o loop (com seu OK no chat)

**Onde escrever a NOVA FEATURE:**  
→ **Seção 1 → `### Features`** (lista com `- [ ]` / `- [x]`)

Não precisa criar arquivo em outro lugar para “pedir” a feature. A IA mapeia dali.

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

### Features

> **VOCÊ ESCREVE A FEATURE AQUI.**  
> A IA usa esta lista como backlog: pega o primeiro `- [ ]`, mapeia, pede OK e entra no ciclo (spec → UX → arch → TDD → código).

- [ ] refatoracao completa do codigo para usar o duck pattern.

**Como escrever (um item por feature):**

```markdown
- [ ] Título curto — o que o usuário ganha (1 linha). Detalhe opcional: quem usa, regra importante, fora de escopo.
- [x] Feature já entregue (a IA marca [x] quando done)
```

**Backlog (edite isto):**

- [ ] [Exemplo] Login com e-mail e senha — usuário entra e vê a home
- [ ] [Exemplo] Listar produtos — catálogo com busca por nome
- [ ] CLI `./jojo` — status, approve, reject, review, sync

---

## 📋 SEÇÃO 2: REGRAS DE AGENTES (Não Altere)

### Princípio de UX

```
Humano escreve features → agents.md Seção 1 · ### Features
Humano escreve design   → system-design.md
Agentes leem, mapeiam, pedem OK, executam, marcam [x]
```

- **Fonte da verdade do backlog = `### Features` neste arquivo.**  
- Nunca peça ao humano outro arquivo só para “cadastrar” feature.  
- Agente **pode** gerar `.ai/specs/…` por baixo dos panos (detalhe interno) — o humano **não** é obrigado a abrir isso.

### Bootstrap (agentes / CI)

```bash
cd kit && npm run sync
```

### 8 Fases

```
draft → spec_approved → ux_approved → tech_approved → test_red → code_review → tested → done
```

### 6 Agentes

| Fase | Agente | Runbook |
| --- | --- | --- |
| draft | Product Manager | `kit/docs/agents/product-manager.agent.md` |
| spec_approved | UX Designer | `kit/docs/agents/ux-designer.agent.md` |
| ux_approved | Architect | `kit/docs/agents/architect.agent.md` |
| tech_approved | QA | `kit/docs/agents/qa.agent.md` |
| test_red | Developer | `kit/docs/agents/developer.agent.md` |
| code_review | QA | `kit/docs/agents/qa.agent.md` |
| tested | Product Manager | `kit/docs/agents/product-manager.agent.md` |
| (sempre) | Squad Lead | `kit/docs/agents/squad-lead.agent.md` |

### Skills

Catálogo: `kit/generated/skills-registry.json`  
`tdd` · `code-review` · `ui-ux` · `ducks-pattern` · `autonomous-loop` · `microcopy`

### 5 Princípios

1. Simplicidade  
2. Sem laziness (causa raiz)  
3. Impacto mínimo  
4. Reversibilidade  
5. Verificação (testes verdes)

---

## 🔄 FLUXO (Para Agentes)

```
1. Lê agents.md SEÇÃO 1 (projeto)
2. Lê ### Features  ← backlog humano
3. Lê system-design.md
4. Pega o PRIMEIRO item - [ ] (não feito)
5. Apresenta resumo + plano no chat → AGUARDA OK do humano
6. Executa 8 fases (PM → … → done)
7. Marca - [x] na ### Features e registra em CHANGELOG.md
```

### Checklist

- [ ] Leu **### Features** em agents.md  
- [ ] Leu system-design.md  
- [ ] Feature nova = primeiro `- [ ]`  
- [ ] OK humano no chat antes de codar  
- [ ] Ao terminar: `- [x]` em Features + CHANGELOG  

---

## 📌 Resposta em uma linha

**Nova feature → Seção 1 → `### Features` → item `- [ ] ...`**

**Versão:** 1.4 | Backlog humano = `### Features`
