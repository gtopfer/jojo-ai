# AGENTS.MD

Régua universal + Especificação do Projeto.

**LLM-agnóstico.** **Humano opera com:** `./jojo` (`init` · `detect` · `run` · `sync` · `version`) + **agent de código (qualquer LLM)** no projeto.  
**Não** administre `kit/` no dia a dia.

| Arquivo (estado) | Função |
| --- | --- |
| **`agents.md`** (este) | Produto (Seção 1) + backlog **`### Features`** + regras (Seção 2) |
| **`system-design.md`** | Arquitetura + design system |
| **`CHANGELOG.md`** | Feito vs. falta |

---

## 🎯 Como Usar (humano)

### Em um projeto novo

```bash
# a partir do repo fonte jojo-ai
./jojo init /caminho/do/seu-projeto
cd /caminho/do/seu-projeto
```

### Todo dia

1. Backlog em **Seção 1 → `### Features`** (`- [ ]` / `- [x]`)
2. **Inicie um agent de código** no app (qualquer LLM/fornecedor)
3. Rode **`./jojo run`**
4. A IA (Squad Lead + fases) pede OK, implementa, marca `[x]`

**Onde a NOVA FEATURE entra:** só em **`### Features`** (abaixo).

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

> **Backlog** — só linhas `- [ ]` / `- [x]` contam para `./jojo run`.  
> CLI: `./jojo init` · `./jojo run` · `./jojo sync` · `./jojo detect` · `./jojo version`

**Backlog:**

- [ ] refatoracao completa do codigo para usar o duck pattern

---

## 📋 SEÇÃO 2: REGRAS DE AGENTES (Não Altere)

> **Roteador** — Seção 1 + Features no boot. Skills/runbooks sob demanda (progressive disclosure).

### Princípio de UX

```
Humano:  ./jojo  +  qualquer agent de código (LLM-agnóstico)
Backlog: agents.md → ### Features
Design:  system-design.md
Régua:   agents.md  (única; sem arquivo por fornecedor)
Máquina: kit/  ·  .ai/
```

- Fonte do backlog = **`### Features`**.  
- Specs detalhadas em `.ai/specs/` são internas.  
- Nunca peça arquivos extras de config ao humano.  
- **Não** duplique a régua em arquivos proprietários de IDE/LLM.  
- **`./jojo run` não implementa sozinho** — o agent de código que o humano abrir executa as fases.

### CLI real

```bash
./jojo init [dir]      # instala/atualiza kit (preserva 3 MDs humanos)
./jojo detect [dir]
./jojo run [dir]       # próxima - [ ]  (+ .ai/jojo-run.json)
./jojo sync [dir]      # registry + context + validate skills
./jojo version
```

Não invente `approve` / `reject` / `review` / `propose` como subcomandos desta CLI.  
Gates = OK humano + suíte do **app** + skills. Done = `- [x]` + CHANGELOG.

### Bootstrap kit (meta)

```bash
./jojo sync
# ou: cd kit && npm run sync
```

### 8 Fases (feature)

```
draft → spec_approved → ux_approved → tech_approved → test_red → code_review → tested → done
```

Hotfix: skill `hotfix-path` (path curto; ainda com qualidade).

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

### Skills (L1: `kit/generated/skills-registry.json`)

Layout: `kit/docs/skills/<id>/SKILL.md`

`onboard` · `handoff` · `hotfix-path` · `delta-spec` · `tdd` · `code-review` · `autonomous-loop` · `ducks-pattern` · `ui-ux` · `microcopy` · `a11y` · `api-contract` · `git-hygiene` · `security-basics`

Discovery: `kit/docs/recommendations.json` (não é config humana).

### Templates

`kit/templates/spec.md` · `delta-spec.md` · `technical-spec.md` · `adr.md`

### 5 Princípios

1. Simplicidade  
2. Sem laziness (causa raiz)  
3. Impacto mínimo  
4. Reversibilidade  
5. Verificação (suíte verde)

---

## 🔄 FLUXO (Para Agentes)

```
1. ./jojo run  (+ sync se necessário)
2. Lê agents.md Seção 1 + ### Features + system-design.md
3. Placeholders? → onboard
4. Classifica feature vs hotfix
5. OK humano → 8 fases (ou path curto)
6. Skills L2 sob demanda
7. Ao done: - [x] em Features + CHANGELOG + ./jojo run
```

### Checklist

- [ ] Leu **### Features** e `.ai/jojo-run.json`  
- [ ] Leu system-design.md  
- [ ] Runtime de IA no app  
- [ ] OK humano antes de codar (feature)  
- [ ] Ao terminar: `- [x]` + CHANGELOG  

---

## 📌 Resposta em uma linha

**Feature → `### Features` → `./jojo run` → IA nas fases → `[x]`**

**Versão:** 2.0 | CLI `init|detect|run|sync|version` · backlog Features · kit Agent Skills
