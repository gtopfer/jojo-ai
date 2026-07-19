```
┌────────────────────────────────────────────────────────────────────┐
│                                                                    │
│   ██████╗ ███████╗██╗   ██╗██╗  ██╗██╗████████╗       █████╗ ██╗   │
│   ██╔══██╗██╔════╝██║   ██║██║ ██╔╝██║╚══██╔══╝      ██╔══██╗██║   │
│   ██║  ██║█████╗  ██║   ██║█████╔╝ ██║   ██║   █████╗███████║██║   │
│   ██║  ██║██╔══╝  ╚██╗ ██╔╝██╔═██╗ ██║   ██║   ╚════╝██╔══██║██║   │
│   ██████╔╝███████╗ ╚████╔╝ ██║  ██╗██║  ██║         ██║  ██║██║   │
│   ╚═════╝ ╚══════╝  ╚═══╝  ╚═╝  ╚═╝╚═╝   ╚═╝         ╚═╝  ╚═╝╚═╝   │
│                                                                    │
│        Dev ToolKit de IA — spec-driven · stateful · CLI            │
│              compatível com Claude Code e Gemini CLI               │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

# 🚀 DevKit-AI — Guia Completo (Para Iniciantes / For Dummies)

Bem-vindo ao **DevKit-AI**! Este é um guia passo a passo detalhado para você entender o que é o kit, como ele funciona e como utilizá-lo no seu dia a dia de desenvolvimento — seja para começar um projeto do zero ou para organizar um projeto que já está em andamento.

---

## 1. O que é o DevKit-AI? (Sem termos difíceis)

Imagine que você está contratando um programador freelancer de IA para criar o seu software. Sem regras, a IA pode:
1. Escrever código direto no seu projeto sem testar, correndo o risco de quebrar o que já funcionava.
2. Esquecer as regras visuais que você definiu (como cores e fontes).
3. Entregar o trabalho incompleto ou sem documentar o que mudou.

O **DevKit-AI** resolve isso criando uma **esteira de produção (pipeline)** automatizada e com **memória local (estado)**. Ele obriga a IA a seguir um fluxo profissional passo a passo, validando cada etapa com você e testando fisicamente o código no seu computador antes de dar a tarefa por encerrada.

---

## 2. A CLI `devkit` — Seus Comandos Explicados

O coração do DevKit é o comando `./devkit` na raiz do seu projeto. Veja o que cada comando faz:

### A) `./devkit init [diretório_alvo]`
* **O que faz**: Instala o cérebro do DevKit no seu projeto.
* **Na prática**: Copia as pastas de regras (`.ai/`, `docs/`) e os arquivos de configuração para a pasta que você indicar.
* **Exemplo**: `./devkit init .` (instala na pasta atual).

### B) `./devkit propose`
* **O que faz**: Abre o assistente interativo para criar uma nova tarefa/funcionalidade.
* **Na prática**: Ele fará perguntas rápidas no terminal (Título, História de Usuário e Requisitos básicos). Ele criará um arquivo de rascunho em `.ai/specs/00X_nome.md` e colocará a tarefa como `draft` (Rascunho) no painel.

### C) `./devkit status`
* **O que faz**: Exibe um painel visual lindo do progresso das tarefas no terminal.
* **Na prática**: Mostra quais tarefas estão concluídas (`done`), quais estão em andamento e em qual fase elas estão travadas (PM, Architect, Developer, etc.).

### D) `./devkit approve`
* **O que faz**: Aprova a fase atual e move a tarefa ativa para a próxima etapa.
* **Na prática**: Você roda este comando no terminal sempre que alinhar algo com a IA no chat e quiser que ela avance para o próximo passo no ciclo de vida. Ele atualiza o `.ai/state.md` automaticamente.

### E) `./devkit review`
* **O que faz**: O fiscal de qualidade do código.
* **Na prática**: Ele descobre a stack do projeto (Python, Node.js, Rust, Go) e executa fisicamente o build, o linter (formatador) e a suíte de testes. Além disso, ele varre os arquivos buscando comentários esquecidos como `TODO`, `FIXME` ou placeholders de IA (como `// o resto do código continua igual`).

---

## 3. As Fases do Ciclo de Vida da Tarefa

Toda funcionalidade que você pedir passará por 6 fases gerenciadas no arquivo `.ai/state.md`. Cada fase ativa um "Runbook" (um papel especializado da IA):

| Status | Papel da IA | O que acontece | Próximo Passo |
|---|---|---|---|
| **`draft`** | **Product Manager (PM)** | A IA conversa com você no chat para detalhar o escopo da feature, expectativas visuais e regras. | Rodar `./devkit approve` no terminal. |
| **`spec_approved`** | **Architect** | A IA escreve a modelagem técnica em `.ai/technical-spec.md` (diagramas, interface, banco de dados). | Rodar `./devkit approve` no terminal. |
| **`tech_approved`** | **QA (TDD)** | A IA escreve os testes automatizados da feature (que estarão falhando por enquanto - Fase Vermelha). | Rodar `./devkit approve` (muda para `test_red`). |
| **`test_red`** | **Developer** | A IA implementa o código e roda `./devkit review` até tudo passar com sucesso. | Rodar `./devkit approve` (muda para `code_review`). |
| **`code_review`** | **QA (Validação)** | O QA roda a suíte de testes completa para garantir que nada quebrou. | Se passar, roda-se `./devkit approve`. |
| **`tested`** | **PM (DoD)** | O PM revisa se todos os itens da Definition of Done (DoD) foram cumpridos. | Rodar `./devkit approve` para finalizar (`done`). |

---

## 4. Tutoriais de Uso passo a passo

### 💡 Tutorial 1: Usando em uma Aplicação Nova (Começando do Zero)

1. **Inicialize**:
   ```bash
   $ ./devkit init /caminho/do/meu/novo/projeto
   ```
2. **Crie a feature**:
   ```bash
   $ ./devkit propose
   ```
   * Digite o título: `Criar página de Login`.
   * Complete as perguntas. A especificação `SPEC-001` será criada.
3. **Refine no Chat**:
   Abra a IA (ex: Claude Code) e diga: *"Vamos detalhar a SPEC-001?"*. A IA atuará como PM. Quando estiver satisfeito com os requisitos propostos, rode no terminal:
   ```bash
   $ ./devkit approve
   ```
4. **Crie a Arquitetura**:
   A IA agirá como Architect e preencherá a stack oficial em `.ai/guidelines/architecture-guidelines.md` e `.ai/technical-spec.md`. Após validar a modelagem técnica, rode:
   ```bash
   $ ./devkit approve
   ```
5. **Escreva Testes e Código**:
   Prossiga rodando `./devkit approve` após os testes de QA serem criados. A IA (Developer) escreverá o código da página de login. Ela executará `./devkit review` no console para verificar a qualidade. Quando tudo estiver verde, o ciclo será encerrado com o DoD do PM e a tarefa mudará para `done`.

---

### 💡 Tutorial 2: Usando em uma Aplicação que Já Existe (Já em Desenvolvimento)

Se você já possui um projeto com códigos e quer organizar o fluxo de trabalho com o DevKit, siga este roteiro:

1. **Instale na pasta atual**:
   Vá para a raiz do seu repositório atual e rode:
   ```bash
   $ /caminho/onde/baixou/o/devkit-ai/devkit init .
   ```
   * O DevKit copiará os arquivos sem apagar o seu código de produção.
   * A spec `SPEC-000` (Setup Inicial) estará marcada como `done` no painel. Seu projeto atual é o ponto de partida!

2. **Rode o Mapeamento Inicial no Chat (Obrigatório)**:
   Antes de pedir qualquer feature, abra o chat da IA e digite:
   > **"Aja como o Architect. Leia o código existente deste repositório e preencha as diretrizes de arquitetura em `.ai/guidelines/architecture-guidelines.md` e a especificação técnica baseline em `.ai/technical-spec.md`."**
   * A IA fará a varredura das pastas, descobrirá sua stack e preencherá as documentações com a realidade atual do seu código (sem inventar nada do zero).

3. **Defina suas Regras de Design**:
   Abra o arquivo `.ai/guidelines/design-premises.md` e escreva o design system ou frameworks visuais que o seu projeto já utiliza (ex: *"Esta aplicação usa Tailwind CSS com tema escuro padrão e botões arredondados"*).

4. **Proponha a primeira alteração**:
   Agora que o DevKit conhece a estrutura do seu projeto atual, rode:
   ```bash
   $ ./devkit propose
   ```
   E siga o fluxo normal! As próximas mudanças respeitarão a arquitetura e premissas mapeadas.

---

## 5. Dicas de Uso e Resolução de Problemas

### 🛠️ E se os requisitos mudarem no meio do caminho?
Se você alterar um requisito no arquivo de especificação ativo (ex: de `.ai/specs/001_login.md`) enquanto a IA está codificando, o orquestrador do DevKit detectará a discrepância no início da sessão. 
A IA retrocederá automaticamente o status no `.ai/state.md` para a fase correta (ex: voltando para `spec_approved` ou `tech_approved`), avisando você no chat: *"Requisitos modificados no arquivo da spec. Retomando da fase de arquitetura para alinhar o código"*.

### 🔄 O que fazer se a IA entrar em loop de testes falhando?
Os runbooks de desenvolvimento contêm **condições de parada obrigatórias**. Se o comando `./devkit review` falhar devido a algum erro persistente, a IA tentará se autocorrigir no máximo **3 vezes** na mesma causa raiz. Se falhar na terceira, ela parará e perguntará no chat: *"Esgotei as tentativas de correção para o erro X. Preciso de sua ajuda para decidir se mudamos a spec ou o código."*

### 🎨 Onde defino os meus padrões visuais?
Use sempre o arquivo [design-premises.md](file:///Users/gtopfer/Documents/Projetos/GitHubProject/devkit-ai/.ai/guidelines/design-premises.md). Escreva lá como você quer que os componentes visuais pareçam. As diretivas da IA obrigam a leitura deste arquivo antes de qualquer codificação, garantindo fidelidade visual ao seu design system.
