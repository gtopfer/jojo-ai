```
┌────────────────────────────────────────────────────────────────────┐
│                                                                    │
│   ██████╗ ███████╗██╗   ██╗██╗  ██╗██╗████████╗       █████╗ ██╗   │
│   ██╔══██╗██╔════╝██║   ██║██║ ██╔╝██║╚══██╔══╝      ██╔══██╗██║   │
│   ██║  ██║█████╗  ██║   ██║█████╔╝ ██║   ██║   █████╗███████║██║   │
│   ██║  ██║██╔══╝  ╚██╗ ██╔╝██╔═██╗ ██║   ██║   ╚════╝██╔══██║██║   │
│   ██████╔╝███████╗ ╚████╔╝ ██║  ██╗██║   ██║         ██║  ██║██║   │
│   ╚═════╝ ╚══════╝  ╚═══╝  ╚═╝  ╚═╝╚═╝   ╚═╝         ╚═╝  ╚═╝╚═╝   │
│                                                                    │
│        Dev ToolKit de IA — spec-driven · multi-agente · TDD        │
│              compatível com Claude Code e Gemini CLI               │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

## Sumário

0. [Antes de Começar: Conceitos-Chave](#0-antes-de-começar-conceitos-chave)
1. [O que é isto](#1-o-que-é-isto)
2. [Regra Absoluta — o motor de tudo](#2-regra-absoluta--o-motor-de-tudo)
3. [Estrutura de Diretórios e Arquivos](#3-estrutura-de-diretórios-e-arquivos)
4. [Compatibilidade: Claude Code & Gemini CLI](#4-compatibilidade-claude-code--gemini-cli)
5. [Passo a Passo de Uso](#5-passo-a-passo-de-uso)
6. [O Fluxo da Squad, visualmente](#6-o-fluxo-da-squad-visualmente)
7. [Cada Peça, Explicada](#7-cada-peça-explicada)
8. [Exemplo Prático Completo](#8-exemplo-prático-completo)
9. [Perguntas Frequentes](#9-perguntas-frequentes)

---

## 0. Antes de Começar: Conceitos-Chave

Este README usa alguns termos técnicos o tempo todo. Se você já conhece todos, pule direto pra seção 1 — mas se um deles soar vago, vale 2 minutos aqui, porque tudo daqui pra frente assume que você sabe o que cada um significa.

| Termo | O que é, em uma frase | Por que aparece neste kit |
|---|---|---|
| **BDD** (Behavior-Driven Development) | Descrever o comportamento esperado do sistema em frases estruturadas, antes de escrever qualquer código | É como a spec de negócio vira critério testável — ver `.ai/features.feature` |
| **Gherkin** | A sintaxe usada para escrever BDD: `Dado` (situação inicial), `Quando` (ação), `Então` (resultado esperado) | Formato do arquivo `.feature` — em português nativo neste kit |
| **TDD** (Test-Driven Development) | Escrever o teste **antes** do código: primeiro um teste que falha (fase vermelha), depois o código mínimo pra fazê-lo passar (fase verde) | O QA sempre escreve os testes antes do Developer tocar em código de implementação |
| **DoR** (Definition of Ready) | Checklist do que precisa estar decidido **antes** de começar a implementar | Evita começar a codar algo que ainda tem pergunta em aberto |
| **DoD** (Definition of Done) | Checklist do que precisa ser verdade pra uma entrega ser considerada terminada | Faz "pronto" ser um critério objetivo, checado por outro papel (o PM) — não opinião de quem programou |
| **ADR** (Architecture Decision Record) | Registro histórico de uma decisão técnica: o que foi decidido, por quê, o que foi descartado | Neste kit não é um arquivo separado — vira uma entrada na seção 9 de `.ai/technical-spec.md` |
| **Clean Architecture** | Organizar o código em camadas onde a regra de negócio não depende de detalhes técnicos (banco, framework) — só o contrário | É a arquitetura padrão deste kit, em `.ai/guidelines/architecture-guidelines.md` |
| **RAG** (Retrieval-Augmented Generation) | Buscar a informação certa antes de responder, em vez de confiar só na memória do modelo | Aqui vira "disciplina de contexto": a IA lê o arquivo certo antes de decidir, nunca adivinha |

> 💡 Não precisa decorar nada disso agora — a ideia é você ter pra onde voltar quando um termo aparecer de novo mais abaixo.

---

## 1. O que é isto

Imagine contratar uma pessoa freelancer pra mexer no seu sistema. Sem processo nenhum, ela pode: editar arquivos direto, sem te consultar; esquecer um padrão de código que você definiu semana passada; entender errado o que você pediu porque a instrução foi vaga; e sumir sem atualizar nenhuma documentação sobre o que mudou. `devkit-ai` existe pra essa pessoa freelancer — que, neste caso, é a própria IA — nunca poder trabalhar desse jeito.

`devkit-ai` é um **kit de inicialização**: uma pasta que qualquer IA de código (Claude Code, Gemini CLI, ou outro agente) lê para trabalhar num projeto de software seguindo sempre o mesmo processo disciplinado, em vez de cada sessão inventar sua própria forma de trabalhar.

Ele resolve, especificamente, os quatro problemas do parágrafo acima:

| Problema | Como o devkit-ai resolve |
|---|---|
| A IA edita código direto, sem processo, sem revisão | **Regra Absoluta**: toda mudança passa por um fluxo de 4 especialistas simulados (PM → Architect → QA → Developer) |
| Cada sessão de IA "esquece" os padrões do projeto | `.ai/global.instructions` + `.ai/guidelines/` são lidos antes de qualquer tarefa, em toda sessão |
| Specs vagas geram código que não é o que você pediu | Todo trabalho nasce de uma spec com critérios de aceitação, DoR e DoD em `.ai/template.specs` |
| Documentação fica desatualizada | Toda entrega atualiza `docs/CHANGELOG.md` e, se mudou arquitetura, uma entrada nova em `.ai/technical-spec.md` |

O jeito de usar é **copiar esta pasta inteira** para a raiz de cada projeto novo — não recriar o conteúdo. O `SYSTEM_PROMPT.md` na raiz não é um gerador: é o prompt de **adaptação inicial**, que instrui a IA a personalizar só os poucos pontos que variam por projeto (nome, descrição, stack) e então operar sob a Regra Absoluta que já vem ativa na cópia.

---

## 2. Regra Absoluta — o motor de tudo

Tudo neste kit gira em torno de uma única regra, definida em [`​.ai/global.instructions`](.ai/global.instructions) e repetida em [`CLAUDE.md`](CLAUDE.md) / [`GEMINI.md`](GEMINI.md) (os arquivos que cada ferramenta carrega sozinha, sem você precisar colar nada):

> **A IA nunca edita, cria ou modifica arquivo de código diretamente.**
> Toda mudança — feature, bugfix, ajuste visual, por menor que seja — é delegada ao [`.ai/agents/squad-lead.agent.md`](.ai/agents/squad-lead.agent.md), que orquestra PM → Architect → QA → Developer com aprovação humana em dois pontos.

Não existe exceção para "é só um ajuste rápido". Essa rigidez é proposital: é o que garante que toda mudança tenha uma spec, um teste escrito antes do código, e um code review — mesmo quando ninguém lembra de pedir isso explicitamente.

> 💡 **Por que ser tão rígido?** Pense num pedido inocente: "só muda a cor desse botão". Sem a Regra Absoluta, a IA edita o CSS, você confere visualmente, aprova — e ninguém percebeu que esse botão também controlava uma condicional de acessibilidade que quebrou. Com a regra, até esse pedido "trivial" passa por QA e code review, que existem exatamente para pegar o que a inspeção visual não pega. A rigidez custa duas pausas de aprovação; a ausência dela custa bugs silenciosos.

---

## 3. Estrutura de Diretórios e Arquivos

```
devkit-ai/
│
├── .ai/                                  # Cérebro do toolkit — tudo que a IA lê
│   │
│   ├── global.instructions               # ★ Regra Absoluta + 4 paradigmas de engenharia + disciplina de docs
│   ├── template.specs                    # Spec #1: requisito do app (negócio, DoR/DoD) — preenchida pelo PM
│   ├── technical-spec.md                 # Spec #2: especificação técnica de construção — preenchida pelo Architect
│   ├── features.feature                  # Exemplo de cenário BDD em Gherkin (pt-BR)
│   │
│   ├── agents/                           # Os 5 "papéis" que simulam uma squad de desenvolvimento
│   │   ├── squad-lead.agent.md           #   orquestrador — ÚNICO ponto de entrada para mudança de código
│   │   ├── product-manager.agent.md      #   escreve template.specs (não-técnico)
│   │   ├── architect.agent.md            #   confirma/desafia a arquitetura, mantém technical-spec.md
│   │   ├── developer.agent.md            #   implementa, roda TDD + code review + autocorreção
│   │   └── qa.agent.md                   #   escreve testes (fase vermelha) e valida a entrega
│   │
│   ├── guidelines/                       # Regras técnicas que Developer e Architect leem sempre
│   │   ├── conventions.md                #   nomenclatura, imports, Conventional Commits
│   │   ├── architecture-guidelines.md    #   stack do projeto (vazia até o 1º uso) + Clean Architecture
│   │   ├── backend-guidelines.md         #   use cases, auth, persistência, variáveis de ambiente
│   │   └── frontend-guidelines.md        #   componentes, estado, roteamento, acessibilidade
│   │
│   └── skills/                           # Procedimentos reutilizáveis, chamados pelos agents
│       ├── code-review.md                #   checklist obrigatório antes de declarar algo "pronto"
│       ├── tdd.md                        #   como derivar testes dos cenários Gherkin
│       └── autonomous-loop.md            #   loop planejar→escrever→testar→avaliar→refatorar + quando parar
│
├── docs/                                 # Documentação viva do projeto (não do toolkit)
│   ├── README.md                         #   índice: aponta para as duas specs e o changelog
│   └── CHANGELOG.md                      #   uma linha por entrega, em linguagem de impacto
│
├── CLAUDE.md                             # ★ Carregado automaticamente pelo Claude Code
├── GEMINI.md                             # ★ Carregado automaticamente pelo Gemini CLI
├── .gitignore
├── SYSTEM_PROMPT.md                      # ★ Prompt de adaptação inicial — usado após copiar a pasta, não gera nada
└── README.md                             # Este arquivo
```

`★` marca os quatro arquivos que fazem o toolkit funcionar sozinho: `global.instructions` (a regra), `CLAUDE.md`/`GEMINI.md` (os gatilhos automáticos) e `SYSTEM_PROMPT.md` (a adaptação inicial pós-cópia).

Repare no que **não** está aqui: `backend/`, `frontend/`, `tests/`, `.env.example`, qualquer `src/`. De propósito — nada estrutural de código é pré-criado. Esse kit é só instrução pra IA; a estrutura real do projeto (pastas, `.env.example` com as variáveis reais, testes) nasce quando o Architect e o Developer trabalham na primeira feature de verdade, não antes. Pré-criar `backend/`/`frontend/` vazios significaria assumir uma stack e uma divisão de camadas antes de qualquer decisão real — o oposto do que `architecture-guidelines.md` com `_(a definir)_` está protegendo.

---

## 4. Compatibilidade: Claude Code & Gemini CLI

| Ferramenta | Arquivo que ela carrega sozinha | O que acontece |
|---|---|---|
| **Claude Code** | `CLAUDE.md` (raiz) | Lê a Regra Absoluta, segue o link para `.ai/global.instructions` |
| **Gemini CLI** | `GEMINI.md` (raiz) | Mesmo conteúdo, mesmo comportamento |
| Qualquer outra IA | — | Cole o conteúdo de `.ai/global.instructions` como instrução de sistema, ou aponte a IA para o arquivo |

`CLAUDE.md` e `GEMINI.md` são **ponteiros finos** — o mesmo texto nos dois, cada um só troca o título. Nenhuma regra é duplicada: a fonte da verdade é sempre `.ai/global.instructions`. Se você editar uma regra, edite lá; os dois ponteiros continuam válidos sem tocar neles.

Nada neste kit usa sintaxe proprietária de nenhuma ferramenta — é tudo Markdown puro, lido por qualquer LLM.

---

## 5. Passo a Passo de Uso

Esta seção pega você pela mão do zero absoluto até a primeira feature entregue. É uma jornada em **4 etapas** — cada uma com o que fazer, o que esperar na tela, e o que fazer se algo não sair como o esperado. Leia em ordem na primeira vez; depois, use como referência.

```
 ETAPA 1          ETAPA 2              ETAPA 3            ETAPA 4
instalar    →    1ª feature      →    dia a dia     →    quando foge
o devkit         define a stack       (pedir, aprovar)    do previsto
```

### Visão geral em 60 segundos

Antes de entrar em detalhe, o mapa completo — isso é tudo que vai acontecer, do início ao fim de uma feature:

```
   você digita UMA frase, em português, sem mencionar agente nenhum
                              │
                              ▼
      CLAUDE.md/GEMINI.md já carregado → IA sabe da Regra Absoluta
                              │
                              ▼
        Squad Lead entra sozinho, explora o projeto, alinha escopo
                              │
                              ▼
     ⏸  pausa 1 — você aprova a spec de negócio (o QUÊ)
                              │
                              ▼
     ⏸  pausa 2 — você aprova a spec técnica (o COMO)
                              │
                              ▼
        QA → Developer → code review → QA valida → PM confere DoD
                              │
                              ▼
        entrega aprovada + CHANGELOG.md e README.md já atualizados
```

Só duas pausas exigem você. O resto — spec, testes, código, review, docs — acontece sem precisar cutucar a IA de novo. Guarda esse diagrama na cabeça: cada etapa abaixo é um zoom numa parte dele.

---

### 🧭 Etapa 1 de 4 — Instalar o devkit-ai num projeto novo

**O que você vai fazer aqui:** colocar a pasta do kit dentro do seu projeto e deixar a IA se apresentar a ele. Leva menos de 2 minutos.

Primeiro, um ponto que vale repetir porque muda tudo: **não existe geração aqui, só cópia.** Você não pede pra IA "criar" nada nesta etapa — a estrutura inteira (seção 3 deste README) já é um conjunto de arquivos prontos, você só posiciona eles no lugar certo.

**Checklist da etapa:**

- [ ] **1. Copie a pasta `devkit-ai` inteira** para a raiz do seu projeto (novo ou já existente). Sim, a pasta inteira — `.ai/`, `docs/`, `CLAUDE.md`, `GEMINI.md`, `SYSTEM_PROMPT.md`, tudo junto.
- [ ] **2. Abra sua IA de código** (Claude Code, Gemini CLI, ou outra) dentro dessa pasta. Nesse momento, sem você fazer nada além de abrir, `CLAUDE.md`/`GEMINI.md` já são lidos automaticamente — a Regra Absoluta já está de pé.
- [ ] **3. Cole o conteúdo de `SYSTEM_PROMPT.md`** como sua primeira mensagem pra IA. Isso dispara a "adaptação inicial" — a IA confere se a cópia está íntegra e personaliza só o que muda de projeto pra projeto (nome, descrição).
- [ ] **4. Diga o nome e (se já souber) a stack do projeto**, como no exemplo abaixo.

```
você:  Execute este SYSTEM_PROMPT pra adaptar o devkit ao projeto.
       Nome: Ticket Manager. Stack: Next.js + PostgreSQL (ou "a definir")

IA:    Estrutura do devkit-ai conferida — íntegra.
       README.md personalizado com nome/descrição/stack.
       .ai/guidelines/architecture-guidelines.md segue "a definir"
       até a primeira feature real passar pelo Architect.
       Regra Absoluta ativa. Pode mandar o primeiro pedido de feature.
```

> ✅ **Sinal de que deu certo:** a IA confirma a estrutura e te devolve o controle, sem ter criado `backend/`, `frontend/`, `src/` ou qualquer arquivo de código. Se ela tentar criar algo assim nesta etapa, ela não seguiu a instrução — pare e reforce: "não crie estrutura de código ainda, só a adaptação inicial".

> ⚠️ **Repare no que NÃO acontece aqui:** a stack não é fixada de verdade neste passo, mesmo se você já disse "Next.js + PostgreSQL". Isso é só uma intenção declarada — a decisão oficial (que vira lei) só acontece na Etapa 2, com o Architect analisando o pedido de uma feature real.

**Já tenho um projeto rodando — e agora?**
Mesmo passo 1: copia a pasta inteira pra raiz dele. A diferença é só na Etapa 2 — em vez de partir de uma tela em branco, o Architect vai ler o código que já existe pra descobrir a stack, não inventar uma do zero.

---

### 🧭 Etapa 2 de 4 — A primeira feature define a stack (acontece uma vez só)

**O que você vai fazer aqui:** pedir a primeira feature de verdade — é esse pedido que faz o Architect decidir (ou confirmar) a stack do projeto.

Antes desse momento, o arquivo `.ai/guidelines/architecture-guidelines.md` está deliberadamente incompleto:

```diff
| Camada     | Tecnologia       |
|------------|------------------|
- | Linguagem  | _(a definir)_    |
- | Framework  | _(a definir)_    |
```

Isso não é um bug nem um esquecimento — é assim de propósito, pra ninguém presumir uma stack antes de existir uma decisão real por trás (ver seção 0, termo **Clean Architecture**, e a explicação na seção 3). Quando você pede a primeira feature, o Architect lê essa lacuna, decide com base no que você pediu (ou confirma o que você já sinalizou na Etapa 1), e reescreve:

```diff
| Camada     | Tecnologia       |
|------------|------------------|
+ | Linguagem  | TypeScript       |
+ | Framework  | Next.js 15       |
```

> ✅ **A partir daqui, esse arquivo é lei.** Toda feature seguinte é avaliada contra essa stack. Um desvio dela não é proibido, mas exige uma entrada no histórico de decisões de `.ai/technical-spec.md` justificando o porquê — nunca é uma troca silenciosa.

> 💡 **Não sabe a stack ainda?** Sem problema — diga "a definir" ou simplesmente não mencione. O Architect vai perguntar o que precisa saber antes de decidir (volume de dados esperado, tempo real ou não, etc.) em vez de chutar.

Essa etapa acontece **uma única vez** por projeto. Nas próximas features, o kit já sabe qual é a stack e pula direto pra implementação.

---

### 🧭 Etapa 3 de 4 — O dia a dia: pedir, aprovar, receber

**O que você vai fazer aqui, todo dia a partir de agora:** falar o que você quer, em português normal, e aprovar duas vezes por feature.

#### Como pedir

Nada de sintaxe especial, nada de invocar agente por nome. Você fala como falaria com um dev humano sentado ao seu lado:

```
"Quero um filtro de status na listagem de tickets."
"Corrige o bug: o campo de e-mail não valida formato."
"Preciso migrar a paginação para cursor-based."
```

Por trás da cena, sem você digitar nada extra, a cadeia que já vimos na seção 2 dispara sozinha:

```
CLAUDE.md/GEMINI.md → .ai/global.instructions → Regra Absoluta
                                                      │
                                    "delego ao Squad Lead" (automático)
```

Se o seu pedido for ambíguo, o Squad Lead pergunta **antes** de acionar qualquer especialista — ele nunca presume por você:

```
IA:    Rapidinho antes de seguir: o filtro de status é só pra listagem
       principal de tickets, ou também pro board kanban? E deve ser
       um filtro único ou múltipla seleção?
```

#### Como aprovar — as duas pausas, na prática

O fluxo inteiro (seção 6 tem o diagrama completo) só para pra te ouvir em dois momentos. Veja exatamente o que aparece na tela em cada um:

**⏸ Pausa 1 — depois do PM, você aprova o QUÊ:**

```
IA:    📋 SPEC PRONTA PARA REVISÃO

       Como usuário, quero filtrar tickets por status,
       para encontrar mais rápido os que preciso.

       Critérios de aceitação: [...]
       DoR: [...]   DoD: [...]

       Aprova essa spec? Quer ajustar algo?

você:  aprovado
```

**⏸ Pausa 2 — depois do Architect, você aprova o COMO:**

```
IA:    ✅ ARQUITETURA CONFIRMADA — nenhuma mudança estrutural necessária

       [diagrama Mermaid da camada afetada]
       [tabela de stack] [contrato de interface] [riscos]

       Aprova a spec técnica e os diagramas?

você:  aprovado
```

> ⚠️ **Regra de ouro das pausas:** qualquer resposta que não seja uma aprovação clara é tratada como pedido de ajuste. Não existe "avançar por silêncio" — se você não disser algo equivalente a "aprovado", a IA não segue pro próximo passo. Se quiser ajustar, só diga o que mudar; a IA reapresenta a versão corrigida e espera de novo.

Depois da segunda pausa, você não precisa mais fazer nada até a entrega — QA escreve os testes, Developer implementa, code review roda, QA valida de novo, e o PM confere o DoD, tudo sem te chamar (a menos que algo seja reprovado — próxima etapa).

---

### 🧭 Etapa 4 de 4 — Quando algo foge do previsto

Duas situações comuns que não são erro do processo — são o processo funcionando como deveria.

#### Se algo for reprovado no meio do caminho

Reprovação não aborta nada — ela só reabre um passo específico e segue de novo:

```
                Developer entrega
                       │
                       ▼
              ⛔ code review reprova
                       │
          "Developer, corrige X e Y e roda
           o checklist de novo antes de reenviar"
                       │
                       ▼
              Developer corrige → reenvia
                       │
                       ▼
                (segue o fluxo normal)
```

O mesmo vale se o **QA de validação** reprovar (volta pro Developer) ou se o **PM** achar que o DoD não foi atendido (idem). Você só é chamado de novo se a reprovação exigir uma decisão sua — o resto o próprio fluxo resolve sozinho, sem te interromper.

> 💡 **Isso é bom sinal, não ruim.** Uma reprovação pega no code review é um bug que não chegou até você. É exatamente o trabalho que essas pausas existem pra fazer.

#### Se você só quiser uma opinião, sem gerar código

Pra uma consulta pontual — não uma feature real, não algo que vira código de produção — você pode pular direto pra um especialista:

```
"Aja como o Architect definido em .ai/agents/architect.agent.md
 e avalia se essa ideia de cache faz sentido."

"Usa o QA de .ai/agents/qa.agent.md pra revisar se estes testes
 cobrem os cenários certos."
```

> ⚠️ Isso é uma consulta isolada, não um atalho. Pra qualquer coisa que vire código de produção, o fluxo completo das Etapas 3 e 4 continua sendo obrigatório — não existe "só dessa vez sem passar pelo QA".

---

**Chegou até aqui?** Você já sabe tudo que precisa pro uso diário. As próximas seções são referência — o diagrama completo do fluxo (seção 6), o que cada arquivo faz em detalhe (seção 7), um exemplo ponta a ponta (seção 8) e as perguntas mais comuns (seção 9).

---

## 6. O Fluxo da Squad, Visualmente

```
                              você
                               │
                               │  "quero uma feature X"
                               ▼
                    ┌─────────────────────┐
                    │      SQUAD LEAD      │   ← único ponto de entrada
                    └──────────┬──────────┘
                               │ 0. explora o projeto, alinha escopo com você
                               ▼
                    ┌─────────────────────┐
                    │   PRODUCT MANAGER    │   escreve a spec (DoR + DoD)
                    └──────────┬──────────┘
                               │
                     1.5  ╔════▼════╗
                          ║ VOCÊ    ║  aprova a spec de negócio?
                          ╚════╤════╝
                               │ sim
                               ▼
                    ┌─────────────────────┐
                    │      ARCHITECT       │   confirma/desafia arquitetura, atualiza technical-spec.md
                    └──────────┬──────────┘
                               │
                     1.8  ╔════▼════╗
                          ║ VOCÊ    ║  aprova a spec técnica + diagramas?
                          ╚════╤════╝
                               │ sim
                               ▼
                    ┌─────────────────────┐
                    │     QA (TDD)         │   escreve testes → FASE VERMELHA
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │      DEVELOPER       │   implementa até os testes passarem
                    └──────────┬──────────┘
                               │
                        ⛔ GATE DE CODE REVIEW
                          reprovado? volta pro Developer
                               │ aprovado
                               ▼
                    ┌─────────────────────┐
                    │   QA (VALIDAÇÃO)     │   roda testes, aprova/reprova
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │  PM (CHECA O DoD)    │   confere item a item da Definition of Done
                    └──────────┬──────────┘
                               │ aprovado
                               ▼
                 ENTREGA APROVADA ✓
                 → docs/CHANGELOG.md atualizado
                 → docs/README.md linkado (feature)
                 → .ai/technical-spec.md ganha entrada no histórico, se houve decisão
```

Qualquer reprovação em qualquer ponto depois do Developer volta o fluxo pro passo 3 (Developer), nunca pula direto pro fim.

---

## 7. Cada Peça, Explicada

Pra cada arquivo/pasta: o que é, e uma analogia rápida pra fixar o papel dele.

### `.ai/global.instructions`
Fonte única da verdade. Contém a Regra Absoluta, os 4 paradigmas de engenharia (spec-driven/BDD, disciplina de contexto, test-first, loop autônomo com autocorreção) e a disciplina de documentação. Todo o resto do kit é referenciado a partir daqui.
> É o "contrato de trabalho" que todo mundo (IA e humano) assina antes de começar.

### `.ai/template.specs` — Spec #1: requisito do app
O molde que o Product Manager preenche pra cada feature, em linguagem de negócio. Força campos de **DoR** (o que precisa estar pronto antes de começar) e **DoD** (o que prova que terminou) — sem eles, "pronto" vira opinião, não critério.
> É o "pedido do cliente" por escrito — o que ele quer, não como vai ser construído.

### `.ai/technical-spec.md` — Spec #2: especificação técnica de construção
O par técnico do arquivo acima, mantido pelo Architect. Junto com `template.specs`, são as **únicas duas specs** deste kit — não existe um terceiro arquivo de "design" ou "decisão" solto em `docs/`. Guarda diagrama de arquitetura, stack, contratos de interface, riscos e — na seção 9 — um **histórico de decisões arquiteturais append-only**: cada veredito do Architect vira uma entrada nova no topo, nunca sobrescrita. É o substituto direto de ADRs individuais e de um documento de solution-design separado.
> É a "planta baixa" da construção — como o pedido do cliente vira estrutura real, e por que cada escolha foi feita.

### `.ai/features.feature`
Exemplo de cenário em Gherkin (`Dado/Quando/Então`), já em português nativo (`# language: pt`). O QA deriva os testes automatizados diretamente destes cenários.
> É o "roteiro de teste de aceitação" — a régua que decide se o que foi construído bate com o que foi pedido.

### `.ai/agents/*.agent.md`
Cinco papéis com responsabilidade única cada — a separação existe pra impedir que a mesma "cabeça" que decide arquitetura também decida se o teste passou, por exemplo. Frontmatter usa só `name` e `description` (campos reconhecidos por ferramentas como o VS Code); qualquer outra informação de contexto vai no corpo do arquivo.
> São os "crachás" da squad — cada um define o que aquela pessoa (papel) pode e não pode fazer.

### `.ai/guidelines/*.md`
Regras técnicas duráveis — não mudam a cada feature. `architecture-guidelines.md` começa vazia (`_a definir_`) porque este kit é agnóstico de stack; o Architect a preenche na primeira execução real e ela vira lei a partir daí.
> É o "manual do funcionário" — não se reescreve a cada tarefa, só se consulta.

### `.ai/skills/*.md`
Procedimentos que os agents seguem: como fazer code review, como derivar testes TDD, como o Developer se autocorrige em loop quando algo falha (com condição de parada — 3 tentativas na mesma causa raiz e escala pra você, nunca fica preso em loop infinito).
> São os "procedimentos operacionais padrão" — o passo a passo de como fazer bem uma tarefa recorrente, não o que fazer.

### `docs/`
Documentação do **produto**, não do toolkit — e deliberadamente enxuta. `README.md` é só um índice apontando para as duas specs em `.ai/`; `CHANGELOG.md` recebe uma linha por feature entregue, em linguagem de impacto. Arquitetura, stack e decisões não moram aqui — moram em `.ai/technical-spec.md`.
> É a "vitrine" do que já foi entregue — não onde se decide o que construir, só onde se registra o que já foi.

---

## 8. Exemplo Prático Completo

Pedido do usuário:
> "Adiciona um filtro por status na listagem de tickets."

O que acontece, em ordem:

1. **Squad Lead** lê o projeto, identifica que é uma *feature nova*, confirma que não há ambiguidade de escopo.
2. **PM** produz uma spec: "Como usuário, quero filtrar tickets por status, para encontrar mais rápido os que preciso" + critérios de aceitação + DoR + DoD.
3. Você aprova a spec.
4. **Architect** confirma que a stack e a Clean Architecture já definidas no projeto suportam isso sem mudança estrutural — atualiza `.ai/technical-spec.md` (diagrama, contrato de interface) mas **não** adiciona entrada no histórico de decisões, porque não houve desvio nem decisão nova, só confirmação do que já existia.
5. Você aprova a spec técnica.
6. **QA** escreve os testes do filtro (ainda falhando — não existe implementação).
7. **Developer** implementa o filtro, faz os testes passarem, roda o checklist de code review e entrega o relatório.
8. Gate de code review aprova.
9. **QA** roda a suíte completa, aprova.
10. **PM** confere o DoD item a item, emite "ENTREGA APROVADA".
11. `docs/CHANGELOG.md` ganha uma linha; `docs/README.md` ganha o link da spec.

Você só falou uma frase — o processo inteiro ficou registrado.

---

## 9. Perguntas Frequentes

**Preciso digitar "use o squad-lead" toda vez?**
Não. A Regra Absoluta em `CLAUDE.md`/`GEMINI.md` já faz a IA delegar sozinha assim que ela lê esses arquivos (o que acontece automaticamente ao abrir o projeto).

**E se eu quiser só uma resposta rápida, sem todo o processo?**
Peça pra IA "agir como" um agente específico (Etapa 4 de 4, seção 5) pra consulta — mas para qualquer coisa que vire código de produção, o fluxo completo é o ponto.

**Posso usar isso num projeto que já existe?**
Sim — copie `.ai/`, `docs/`, `CLAUDE.md`, `GEMINI.md` e `SYSTEM_PROMPT.md` pra raiz do projeto. Na primeira feature, o Architect vai olhar o código existente e preencher `architecture-guidelines.md` e `.ai/technical-spec.md` com a realidade atual, em vez de partir de um esqueleto vazio.

**Por que só duas specs (`template.specs` e `technical-spec.md`) e não um arquivo de arquitetura vivo + ADRs separados?**
Porque um documento de arquitetura vivo e um ADR por decisão viram, na prática, três a quatro arquivos crescendo por projeto — fácil de esquecer de atualizar um dos três. Consolidar em duas specs (negócio + técnica) com histórico de decisões *dentro* da spec técnica reduz a superfície de manutenção sem perder nada: a seção 9 de `technical-spec.md` é append-only, então o histórico continua existindo, só que num lugar só.

**O que faço se a IA travar num loop de correção de teste?**
Pela regra em `.ai/skills/autonomous-loop.md`, ela mesma para depois de 3 tentativas na mesma causa raiz e te avisa exatamente o que tentou e o que precisa de decisão sua — você não deveria ver um loop infinito.

**Isso funciona em outra IA além de Claude e Gemini?**
Sim — o conteúdo é Markdown puro sem sintaxe proprietária. Só não existe um arquivo "auto-carregado" equivalente a `CLAUDE.md`/`GEMINI.md` pra outras ferramentas; nesse caso, aponte manualmente pra `.ai/global.instructions` no início da sessão.
