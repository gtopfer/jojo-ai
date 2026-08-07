# Plano de Melhoria — jojo-ai

**jojo-ai** é um SPECKIT minimalista para inicializar qualquer projeto com suporte a AI.

---

## 🎯 Propósito Real

```
Novo Projeto
    ↓
Copia jojo-ai/
    ↓
Preenche agents.md + docs/ + templates/
    ↓
Agentes IA lêem context + guardrails
    ↓
Agentes executam tasks (código, docs, UX, knowledge, etc)
```

---

## 📊 Análise de agent-skills → Oportunidades para jojo-ai

### Similaridades
- **Modular** — agent-skills tem packages; jojo-ai tem docs/templates
- **Skills reutilizáveis** — ambas usam competências especializadas
- **Metadados** — SKILL.md com frontmatter = facilita discovery
- **Agnóstico** — agent-skills: 20+ agentes; jojo-ai: qualquer modelo

### O que agent-skills faz bem
1. **Frontmatter YAML** — Skills com metadados estruturados
2. **Registry gerado** — skills-registry.json para discovery
3. **Validação de qualidade** — checklist de skill descriptor
4. **Categorias** — Agrupar skills por tipo (quality, design, infra, etc)
5. **Versioning** — Conventional commits + Nx Release

---

## 🚀 Melhorias Recomendadas para jojo-ai

### Tier 1: Estrutura de Skills (Semana 1)

#### 1.1 **Add Frontmatter a Skills**
Hoje: `docs/skills/tdd.md` é só markdown.  
Futuro: YAML frontmatter com metadados:

```markdown
---
name: TDD
type: development
category: quality
description: Test-Driven Development — RED/GREEN/REFACTOR cycle
usedFor: [code, tests, refactor]
appliesTo: [backend, frontend]
requiredKnowledge: [testing-frameworks, assertions]
---

# TDD
...
```

**Benefício:** Agentes descobrem skills sem ler arquivo inteiro.

---

#### 1.2 **Skills Registry Generator**
Script que scan `docs/skills/` e gera `skills-registry.json`:

```json
{
  "version": "1.0",
  "generated": "2026-08-07T11:00:00Z",
  "skills": [
    {
      "name": "tdd",
      "type": "development",
      "category": "quality",
      "path": "docs/skills/tdd.md",
      "description": "Test-Driven Development",
      "appliesTo": ["backend", "frontend"],
      "hash": "sha256:abc123"
    },
    {
      "name": "code-review",
      "type": "development",
      "category": "quality",
      ...
    }
  ]
}
```

**Uso:** Agentes lêem registry, descobrem que skills existem + onde estão.

**Implementação:** Simple Node script no Makefile:
```bash
npm run generate:registry
```

---

#### 1.3 **Skill Types & Categories**
Padronizar tipos de skills:

| Type | Exemplos |
| --- | --- |
| **development** | TDD, code-review |
| **documentation** | writing, technical-spec |
| **design** | ui-ux, accessibility |
| **knowledge** | search, summarization |
| **refinement** | text-cleanup, structure |

**Benefício:** Agentes filtram skills por necessidade ("preciso de skill de refactor").

---

### Tier 2: Validação & Quality (Semana 2)

#### 2.1 **Skill Validator Checklist**
`docs/skill-validator.md` — checklist que SKILL.md deve atender:

```markdown
# Skill Validator Checklist

- [ ] Frontmatter YAML válido (name, type, category, description)
- [ ] Description < 1024 chars
- [ ] "Use when" section existe
- [ ] "Do NOT use for" section existe (previne overlap)
- [ ] Nenhum XML/ângulos (< >)
- [ ] Exemplos práticos inclusos
- [ ] Link para refs se houver deps
- [ ] Seções bem organizadas
```

**Uso:** Antes de mergear skill nova:
```bash
./scripts/validate-skill.sh docs/skills/new-skill.md
```

---

#### 2.2 **Add "requiredKnowledge" & "appliesTo"**
Metadados que ajudam agentes a auto-selecionarem skills:

```yaml
requiredKnowledge: [react, typescript, jest]
appliesTo: [frontend, tests]
conflicts: [no-tests, skip-review]
```

**Benefício:** Agente sabe "esse skill precisa de React; meu projeto usa Vue? Skip".

---

### Tier 3: Project Context Structure (Semana 3)

#### 3.1 **Standardize Project Context**
Hoje: `.ai/guidelines/*` é livre-form.  
Futuro: Schema mínimo obrigatório:

```
.ai/guidelines/
├── stack.md          ← Languages, frameworks, versions
├── conventions.md    ← Code style, naming, patterns
├── guardrails.md     ← What NOT to do; compliance; security
├── architecture.md   ← Layers, packages, decisions
└── integrations.md   ← External services, APIs, databases
```

**Exemplo `stack.md`:**
```markdown
# Stack

| Layer | Technology | Version |
| --- | --- | --- |
| Frontend | React | 18+ |
| Backend | Node.js | 18 LTS |
| Database | PostgreSQL | 14+ |
| Testing | Jest | 30+ |
```

**Exemplo `guardrails.md`:**
```markdown
# Guardrails

## DO NOT
- [ ] Hardcode secrets
- [ ] Delete database migrations
- [ ] Skip tests for "speed"
- [ ] Use eval() or unsafe code

## Security
- [ ] All inputs validated
- [ ] XSS prevention
- [ ] SQL injection protection
```

**Benefício:** Agentes lêem contexto estruturado; reduz erros.

---

#### 3.2 **Project Context Schema (JSON)**
Generate `project-context.json` from .ai/guidelines:

```json
{
  "name": "my-app",
  "description": "E-commerce platform",
  "stack": {
    "frontend": "React 18",
    "backend": "Node.js 18 LTS",
    "database": "PostgreSQL 14"
  },
  "conventions": {
    "codeStyle": "prettier-no-semicolons",
    "namingPattern": "camelCase-components-PascalCase"
  },
  "guardrails": {
    "mustHave": ["tests", "types", "auth-check"],
    "mustNOT": ["hardcoded-secrets", "eval"]
  },
  "skills": [
    "tdd",
    "code-review",
    "ui-ux"
  ]
}
```

**Uso:** Agent reads this, auto-configures behavior.

---

### Tier 4: Agent Discovery & Selection (Semana 4+)

#### 4.1 **Agent Profiler**
Criar `docs/agents-profile.md` — quais agents você quer usar:

```markdown
# Agents Profile

## Available
- Claude Code (primary)
- Cursor (alternative)
- Gemini (experimental)

## For Each Task Type
| Task | Agent | Role |
| --- | --- | --- |
| Code Implementation | Claude Code | primary |
| Code Review | Cursor | secondary |
| Documentation | Claude | writer |
| Search in KB | Gemini | researcher |
```

**Benefício:** Agentes sabem quando chamar quem; handoffs automáticos.

---

#### 4.2 **Skills Recommendation Engine**
Simple JSON que recomenda skills por contexto:

```json
{
  "when_starting_project": ["stack.md", "guardrails.md"],
  "when_writing_code": ["tdd", "code-review"],
  "when_designing_ui": ["ui-ux"],
  "when_documenting": ["technical-spec-template"],
  "when_searching_kb": ["knowledge-search"]
}
```

---

## 📋 Comparação: agent-skills vs. jojo-ai (Futuro)

| Aspecto | agent-skills | jojo-ai (hoje) | jojo-ai (com melhorias) |
| --- | --- | --- | --- |
| **Propósito** | Registry + installer de skills | SPECKIT | SPECKIT + discovery |
| **Skills** | 50+ curated, published | 3 core skills | 3-5 core + project-custom |
| **Metadados** | YAML frontmatter | Nenhum | YAML frontmatter |
| **Registry** | CDN-served | Nenhum | Local JSON |
| **Validation** | Snyk security scan | Code review skill | Validation checklist |
| **Project Context** | N/A (skills registry) | Free-form docs | Structured JSON schema |
| **Agent Selection** | CLI wizard | N/A | Recommendation engine |
| **Distribution** | npm, jsDelivr | Copy-paste | Copy-paste (same) |

---

## 🎯 Roadmap (Próximas 4 Semanas)

### **Week 1: Tier 1 — Structure**
- [ ] Add YAML frontmatter para skills
- [ ] Skill type + category constants
- [ ] skills-registry.json generator
- **Output:** `npm run generate:registry` pronto

---

### **Week 2: Tier 2 — Quality**
- [ ] Skill validator checklist
- [ ] requiredKnowledge + appliesTo metadados
- [ ] Update docs/skills/ com novo formato
- **Output:** Todas skills em novo formato validado

---

### **Week 3: Tier 3 — Context**
- [ ] Schema for .ai/guidelines/ (stack, conventions, guardrails, etc)
- [ ] project-context.json generator
- [ ] Template exemplos em templates/
- **Output:** `npm run generate:context` pronto

---

### **Week 4: Tier 4 — Discovery**
- [ ] Agent profiler (quem faz o quê)
- [ ] Skill recommendation logic
- [ ] Update agents.md com novo flow
- **Output:** Agentes podem descobrir skills + agents automaticamente

---

## 🚀 Quick Win (Comece Hoje)

Se quer começar **agora** (1-2 horas):

1. **Add frontmatter a uma skill:**
```markdown
---
name: TDD
type: development
category: quality
description: Test-Driven Development cycle
usedFor: [tests, code]
---
```

2. **Create `scripts/generate-registry.js`:**
```javascript
const fs = require('fs')
const path = require('path')

const skillsDir = path.join(__dirname, '../docs/skills')
const skills = fs.readdirSync(skillsDir)
  .filter(f => f.endsWith('.md'))
  .map(f => ({
    name: f.replace('.md', ''),
    path: `docs/skills/${f}`
  }))

fs.writeFileSync(
  path.join(__dirname, '../skills-registry.json'),
  JSON.stringify({ skills }, null, 2)
)
```

3. **Add npm script:**
```json
{
  "scripts": {
    "generate:registry": "node scripts/generate-registry.js"
  }
}
```

**Tempo:** ~30 min | **Impacto:** Foundation para tudo mais.

---

## 🎓 Filosofia

jojo-ai evolui como:

```
SPECKIT Minimalista
    ↓ (Week 1)
+ Metadados estruturados
    ↓ (Week 2)
+ Validação de qualidade
    ↓ (Week 3)
+ Project context schema
    ↓ (Week 4)
+ Agent discovery & selection
    ↓
= Agnóstico toolkit para AI projects
```

Mantendo **minimalismo** mas adicionando **estrutura** para descoberta automática.

---

**Status:** Plan only — não implementado. Simples de fazer, grande impacto.
