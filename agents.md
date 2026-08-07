# AGENTS.MD

Régua universal + Especificação do Projeto.

**Superfície humana na raiz (3 arquivos):**

| Arquivo | O que o humano preenche / acompanha |
| --- | --- |
| **`agents.md`** (este · Seção 1) | Produto, stack resumo, usuários, guardrails, convenções |
| **`system-design.md`** | Arquitetura + design system **deste** projeto |
| **`CHANGELOG.md`** | O que foi feito vs o que falta (agentes atualizam com seu OK) |

Tudo o mais fica em **`kit/`** (runbooks, skills, scripts, templates, gerados).

---

## 🎯 Como Usar

1. Copie jojo-ai para o projeto (ou use como base)
2. Edite **`agents.md` (Seção 1)**
3. Edite **`system-design.md`**
4. Agentes leem os 3 da raiz + `kit/` quando precisar
5. Validam com você antes de executar
6. Registram progresso em **`CHANGELOG.md`**

### O que o humano edita vs. não edita

| Artefato | Quem mexe |
| --- | --- |
| `agents.md` Seção 1 | **Humano** |
| `system-design.md` | **Humano** (agentes só com aceite, se o design mudar) |
| `CHANGELOG.md` | Agentes (com OK) + humano pode ajustar prioridade |
| `agents.md` Seção 2 | Kit (não altere) |
| `kit/**` | Kit / agentes mantenedores — **não é setup do usuário** |

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

### Princípio de UX (inviolável)

```
Raiz (humano):
  agents.md  +  system-design.md  +  CHANGELOG.md

Kit (agentes / máquina):
  kit/docs  kit/scripts  kit/templates  kit/generated
```

**`system-design.md`** = fonte da verdade de arquitetura e design system.  
Conflito chat vs. arquivo → vence o arquivo (ou o humano o atualiza).

Nunca peça ao usuário arquivos extras de config (`stack.md`, `design-premises.md`, JSON de skills, etc.).

### Bootstrap de artefatos (agentes / CI)

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

### Skills (catálogo: `kit/generated/skills-registry.json`)

- `kit/docs/skills/tdd.md`
- `kit/docs/skills/code-review.md`
- `kit/docs/skills/ui-ux.md`
- `kit/docs/skills/ducks-pattern.md`
- `kit/docs/skills/autonomous-loop.md`
- `kit/docs/skills/microcopy.md`

Discovery: `kit/docs/recommendations.json` — humano **não** configura.

### Templates

- `kit/templates/spec.md`, `technical-spec.md`, `adr.md`, `feature.feature`

### 5 Princípios

1. **Simplicidade** — Mude apenas o necessário
2. **Sem Laziness** — Encontre causas raiz
3. **Impacto Mínimo** — Zero bugs secundários
4. **Reversibilidade** — Confirme operações destrutivas
5. **Verificação** — Testes verdes antes de pronto

---

## 🔄 FLUXO DE EXECUÇÃO (Para Agentes)

```
1. Lê agents.md SEÇÃO 1
2. Lê system-design.md
3. Lê agents.md SEÇÃO 2 + runbook em kit/docs/agents/
4. (Opcional) kit/generated/* + recommendations
5. Lê CHANGELOG.md
6. Se feature nova → apresenta humano → aguarda OK → executa → atualiza CHANGELOG
```

### Checklist

- [ ] `agents.md` + `system-design.md` + `CHANGELOG.md`
- [ ] Se design placeholder e tarefa de UI/código → co-preencher com humano
- [ ] Feature nova → OK humano antes de implementar
- [ ] Não violar `system-design.md`
- [ ] Registrar em `CHANGELOG.md`

---

## 📌 Resumo

| Raiz | Kit |
| --- | --- |
| `agents.md` · `system-design.md` · `CHANGELOG.md` | `kit/**` |

**Versão:** 1.3 | **UX:** 3 arquivos na raiz · resto em `kit/`
