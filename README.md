```
┌──────────────────────────────────────────────────┐
│                                                  │
│      ██╗ ██████╗      ██╗ ██████╗                │
│      ██║██╔═══██╗     ██║██╔═══██╗               │
│      ██║██║   ██║     ██║██║   ██║               │
│ ██   ██║██║   ██║██   ██║██║   ██║               │
│ ╚█████╔╝╚██████╔╝╚█████╔╝╚██████╔╝               │
│  ╚════╝  ╚═════╝  ╚════╝  ╚═════╝                │
│                    · a i ·                       │
│                                                  │
│     ★  ./jojo  →  ship  ★                        │
│        CLI é a interface · agentes por baixo     │
│                                                  │
└──────────────────────────────────────────────────┘
```

# jojo-ai — guia de uso

SPECKIT minimalista para desenvolver com agentes de IA.

Este README é o **manual de operação**. Você opera com a **CLI `./jojo`** e um **agent de código** (qualquer LLM/fornecedor). jojo **não** amarra o projeto a um modelo ou IDE.

---

## 1. Ideia em 30 segundos

| Você faz | O sistema faz |
| --- | --- |
| `./jojo init …` | Instala/atualiza kit + CLI no projeto |
| Abre um **agent de código** no projeto | Lê a régua (`agents.md`) e executa as fases |
| `./jojo run` | Seleciona a próxima feature do backlog e orienta o loop |
| `./jojo sync` | Regenera registry/context e valida skills |
| `./jojo detect` / `version` | Diagnóstico e versão |

**Princípio:** CLI governa o ciclo; **qualquer** agent que leia o repo executa.  
`kit/` é máquina — você não precisa abri-lo no dia a dia.

### LLM-agnóstico

- **Régua única:** `agents.md` (não um arquivo por fornecedor).  
- Skills/runbooks em Markdown portátil (`kit/`).  
- Adaptadores opcionais: `kit/adapters/` — só se a ferramenta descobrir skills por pasta.  
- jojo **não** exige Claude, GPT, Gemini, Grok, Cursor, etc.

> **`./jojo run` sozinho não “pensa”.** Mapeia a feature e o contrato do loop. Quem implementa é o agent de código que **você** iniciar no app.

---

## 2. CLI — referência completa

Única superfície de operação humana.

```bash
# A partir do repositório fonte jojo-ai (este):
./jojo init /caminho/do/seu-projeto   # instala OU atualiza o kit
./jojo detect /caminho/do/seu-projeto # já tem jojo? qual versão?
./jojo version

# Dentro do projeto onde o kit foi instalado:
./jojo run                            # próxima feature do backlog
./jojo sync                           # registry + validate skills
./jojo detect .
```

| Comando | O que faz |
| --- | --- |
| `init [dir]` | Copia/atualiza kit + CLI no alvo; **preserva** `agents.md`, `system-design.md`, `CHANGELOG.md` |
| `detect [dir]` | Diz se jojo está instalado e mostra metadados |
| `run [dir]` | Lê `agents.md` → `### Features`, seleciona a **primeira** `- [ ]` e prepara o loop (**requer** agent de código no projeto — ver §3) |
| `sync [dir]` | `npm run sync` no `kit/` (registry, context, validate skills) |
| `version` | Versão da CLI |

```bash
./jojo --help
./jojo init --help
```

**Flags do `init`:**

| Flag | Efeito |
| --- | --- |
| `--force` | Sobrescreve também `agents.md`, `system-design.md` e `CHANGELOG.md` (perde edições humanas) |
| `--reset-human` | No update, reseta só os 3 templates humanos, sem forçar o resto |
| `--skip-sync` | Não roda `npm run sync` no kit ao final |
| `--yes` | Não pede confirmação em casos especiais (ex.: alvo = repo fonte) |

**Versões:** a CLI `jojo` (constante `VERSION` no script) e o `kit/` (`kit/package.json`) têm versionamento independente; `detect` mostra a versão da CLI instalada.

**Atualizar** o kit num projeto já instalado: de novo `./jojo init /caminho/do/seu-app` (detecta instalação antiga sozinho; não apaga a Seção 1 humana salvo flags de force).

---

## 3. Setup do zero

Caminhos abaixo são **exemplos genéricos** — troque pelos seus.

```bash
# 1) Clone / abra o repo fonte jojo-ai
git clone <url-do-jojo-ai> jojo-ai
cd jojo-ai
chmod +x ./jojo
./jojo version

# 2) Instale o kit no seu app
./jojo init /caminho/do/seu-app
cd /caminho/do/seu-app

# 3) Garanta backlog em agents.md → ### Features  (linhas - [ ] …)  — ver §6

# 4) Abra um agent de código / assistente de IA no diretório do app
#    (qualquer fornecedor — jojo não escolhe o modelo por você)

# 5) No terminal do app (com o agent já ativo no mesmo projeto):
./jojo run
#    → a CLI aponta a feature; o agent executa o loop (8 fases)
```

Ordem mental:

1. `init` no app  
2. Produto/design em `agents.md` Seção 1 + `system-design.md` (uma vez)  
3. Itens em `### Features`  
4. **Agent de código** no app (LLM-agnóstico)  
5. `./jojo run` → o agent segue a régua → `- [x]` + CHANGELOG  

Não crie `stack.md`, profile JSON nem config dentro de `kit/`.

### CLI + agent (papéis)

| Peça | Papel |
| --- | --- |
| `./jojo` | Estado, backlog, init/update do kit, qual feature é a próxima |
| Agent de código (qualquer LLM) | Ler `agents.md`, skills, implementar, testar, marcar fases |

Sem um agent lendo o repo, `run` só diz *o que* fazer — não implementa sozinho.

---

## 4. Fluxos via CLI

### 4.1 Feature nova

```text
# no repo fonte
./jojo init /caminho/do/seu-app

# no app: backlog com - [ ] em ### Features
# no app: abra o agent de código (qualquer LLM) neste diretório
cd /caminho/do/seu-app
./jojo run
  → CLI aponta a primeira - [ ]
  → agent: 8 fases (PM → UX → Architect → QA → Dev → QA → PM → done)
  → - [x] + CHANGELOG
```

**8 fases:**

```text
draft → spec_approved → ux_approved → tech_approved
  → test_red → code_review → tested → done
```

| Fase | Agente | Gate |
| --- | --- | --- |
| `draft` | Product Manager | Spec + DoR |
| `spec_approved` | UX Designer | UI/estados **ou** N/A |
| `ux_approved` | Architect | Tech-spec / contratos |
| `tech_approved` | QA | Testes **RED** |
| `test_red` | Developer | Implementação + qualidade |
| `code_review` | QA | Review / suíte verde |
| `tested` | Product Manager | DoD de negócio |
| `done` | — | Feature `[x]` |

### 4.2 Retomar

```bash
# 1) Abra de novo o agent de código no app
# 2) Terminal:
./jojo detect .
./jojo run
```

Estado no disco: `agents.md` (`### Features`), `.ai/`, `system-design.md`.

### 4.3 Atualizar o kit no app

```bash
# a partir do repo fonte jojo-ai
./jojo init /caminho/do/seu-app
```

---

## 5. Arquivos na raiz (estado, não “UI”)

A CLI e os agentes leem/gravam estes arquivos. Você **não** opera o dia a dia abrindo pastas — só garante que o backlog e o produto existam.

| Arquivo | Função |
| --- | --- |
| [`agents.md`](./agents.md) | Produto (Seção 1) + backlog **`### Features`** + regras (Seção 2) |
| [`system-design.md`](./system-design.md) | Arquitetura + design system |
| [`CHANGELOG.md`](./CHANGELOG.md) | Feito vs. falta |

`kit/`, `.ai/`, skills, registry = **máquina** (instalados/atualizados por `init`).

---

## 6. Features — contrato do backlog

`./jojo run` só enxerga linhas de checklist em `agents.md`:

```markdown
### Features

**Backlog:**

- [ ] minha feature em linguagem de negócio
- [x] feature já entregue
```

Regras:

- Só `- [ ]` / `- [x]` contam.
- A **primeira** `- [ ]` de cima para baixo é a próxima do `run`.
- Ao concluir: `- [x]` + CHANGELOG.
- Specs detalhadas podem ir para `.ai/specs/` (interno).

Sem linha `- [ ]`, o `run` não tem o que selecionar.

---

## 7. Agentes (papéis no loop — rodando no seu agent de código)

Orquestrador: **Squad Lead**. São runbooks que o **seu** agent de código segue após `./jojo run`, não pastas que você abre.

| Papel | Entrega |
| --- | --- |
| Product Manager | Spec, DoR/DoD |
| UX Designer | UI/estados **ou** N/A |
| Architect | Tech-spec, contratos |
| QA | RED depois validação |
| Developer | Diff mínimo, testes verdes |

Runbooks: `kit/docs/agents/*.agent.md`  
Skills: `kit/docs/skills/` · catálogo `kit/generated/skills-registry.json`

---

## 8. Qualidade e guardrails

1. **Ducks Pattern** (ou estrutura feature-first em `system-design.md` §2)  
2. **TDD:** RED → GREEN → refactor  
3. Review / suíte verdes antes de `done`  
4. Loop autônomo com limite (sem spin infinito)  
5. Sem segredos no repo; sem TODO de “resto do código”  

---

## 9. O que **não** fazer

| Evite | Por quê |
| --- | --- |
| Tratar `kit/` como setup manual | `init` gerencia |
| 10 arquivos de config humana | Só os 3 da raiz |
| Feature fora de `### Features` | `run` não vê |
| Pular `init` e copiar pastas à mão | Drift de versão |
| Spec monstro para mudança mínima | Escopo enxuto / delta |
| Medo de `init` apagar Seção 1 | Preserva os 3 humanos (salvo force) |

---

## 10. Mapa do repositório (fonte)

```text
jojo-ai/
  README.md            ← este manual
  jojo                 ← CLI (init | detect | run | sync | version)
  agents.md            ← régua única (LLM-agnóstica) + Features
  system-design.md
  CHANGELOG.md
  kit/                 ← máquina (agents, skills, adapters, scripts)
  kit/adapters/        ← skills portáteis opcionais (não amarram LLM)
  .ai/                 ← estado/specs internas
  .github/workflows/
```

Após `init` no app: mesma ideia — `jojo` + `kit/` gerenciados + 3 MDs.

Mantenedores do kit (meta):

```bash
cd kit && npm run sync
```

Detalhes: [`kit/README.md`](./kit/README.md).

---

## 11. FAQ

**Qual é a interface humana?**  
CLI (`init`, `detect`, `run`, `sync`, `version`) + um agent de código à sua escolha.

**jojo depende de qual LLM?**  
De nenhum. A régua é `agents.md` + CLI. Qualquer agent que leia o repo serve.

**`run` implementa sozinho?**  
Não. A CLI escolhe a feature e o contrato do loop. Um agent de código no projeto executa.

**Qual modelo / IDE usar?**  
Qualquer um, desde que siga `agents.md` e `./jojo run`. Não mantenha réguas duplicadas por ferramenta.

**Preciso editar markdown todo dia?**  
Não. Backlog em `### Features` quando criar item; o resto é `run` + agent.

**Como atualizo o kit no app?**  
No repo fonte: `./jojo init /caminho/do/seu-app`.

**E se o agent pedir outro arquivo de config?**  
Recuse: superfície = CLI + 3 MDs na raiz (`agents.md` é a única régua).

**`run` não acha feature?**  
Confira `### Features` com pelo menos um `- [ ]`.

---

## 12. Checklist

- [ ] `./jojo version` / `detect` ok no app  
- [ ] Seção 1 + system-design preenchidos (uma vez)  
- [ ] `- [ ]` em `### Features`  
- [ ] Agent de código **iniciado** no app (qualquer LLM)  
- [ ] `./jojo run`  
- [ ] Fases concluídas com qualidade  
- [ ] `- [x]` + CHANGELOG  
- [ ] Sem edição manual de `kit/`  
- [ ] Sem amarrar o repo a um único fornecedor de LLM  

---

## 13. Licença

[GPL-3.0](./LICENSE)

---

**UX:** CLI (`init|detect|run|sync|version`) · **LLM-agnóstico** · backlog = `### Features` · régua = `agents.md` · resto máquina
