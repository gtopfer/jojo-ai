# Premissas de Design & Produto

Diretrizes **permanentes** de UI/UX, design system e premissas de produto.  
Toda decisão de interface, fluxo ou biblioteca visual **deve** respeitar este arquivo.

> **Quem preenche**: humano + agent UX (fase `spec_approved`) na primeira feature com UI, e sempre que um padrão de produto mudar.  
> **Quem consome**: PM, UX, Architect, Developer, QA.  
> **Skill**: `.ai/skills/ui-ux.md` · **Agent**: `.ai/agents/ux-designer.agent.md`

Substitua os valores entre `_..._` pelos do produto real. Enquanto estiverem assim, a IA **deve perguntar** antes de inventar marca/stack visual.

---

## 1. UI & Design System

### 1.1 Stack visual (preencher)

| Item | Valor do produto |
|------|------------------|
| Biblioteca de componentes | _ex.: shadcn/ui + Radix · MUI · Chakra · HTML/CSS próprio_ |
| Estilo / utilitários | _ex.: Tailwind CSS · CSS Modules · vanilla-extract_ |
| Ícones | _ex.: lucide-react · heroicons_ |
| Motion (se houver) | _ex.: sem animação além de fade · framer-motion só em X_ |

### 1.2 Temas

- **Modos suportados**: _Light only · Dark only · Light + Dark (default: …)_  
- **Preferência do sistema**: _respeitar `prefers-color-scheme` · sim · não_  
- Todo componente visual novo deve funcionar em **todos** os modos suportados.

### 1.3 Tipografia

| Papel | Fonte / peso | Notas |
|-------|--------------|--------|
| UI (corpo) | _ex.: Inter / 400–500_ | |
| Títulos | _ex.: Inter / 600–700_ | |
| Mono (código/dados) | _ex.: JetBrains Mono · system mono_ | só se necessário |

Escala de tipo: _usar escala do design system / Tailwind `text-sm`… · documentar desvios_.

### 1.4 Cor e tokens

Defina **tokens semânticos**, não só hex soltos:

| Token | Uso | Exemplo |
|-------|-----|---------|
| `primary` | CTA principal, links fortes | _HSL / OKLCH …_ |
| `destructive` | Apagar, erros graves | |
| `muted` | Secundário, bordas suaves | |
| `background` / `foreground` | Superfície e texto | |
| `success` / `warning` | Feedback | |

- **Contraste**: texto normal ≥ 4.5:1; texto grande ≥ 3:1 (WCAG 2.1 AA).  
- Proibido: cor hex “mágica” no JSX/CSS de feature sem token.

### 1.5 Espaçamento, raio, elevação

- Espaçamento: _escala 4/8 · tokens `spacing`_  
- Raio: _ex.: `rounded-md` padrão em cards/inputs_  
- Sombra: _mínima · só em overlays_

---

## 2. UX (comportamento)

### 2.1 Navegação

- **Desktop**: _sidebar fixa · top nav · …_  
- **Mobile**: _bottom tabs · drawer · hamburger · …_  
- **Onde estou**: sempre sinalizar rota/seção ativa.  
- Breadcrumbs: _quando hierarquia ≥ 3 níveis · nunca · …_

### 2.2 Formulários

- Inserção rápida: _Dialog/Modal_  
- Fluxo longo (≥ ~5 campos ou multi-etapa): _página dedicada ou stepper_  
- Erros: **inline** sob o campo + resumo se muitos  
- Submit: desabilitado enquanto `submitting`; evitar double-submit  
- Validação: schema único (FE alinhado ao contrato do Architect)

### 2.3 Feedback assíncrono

| Situação | Padrão obrigatório |
|----------|-------------------|
| Carregamento de página/seção | Skeleton (preferencial) ou progress claro |
| Ação de botão | Loading no controle + disable |
| Erro recuperável | Mensagem + **Retry** |
| Sucesso de mutação | Toast/inline conforme densidade da tela |
| Lista vazia | Empty state com explicação + CTA se fizer sentido |

### 2.4 Densidade e conteúdo

- Produto _consumer · B2B denso · misto_ — preferir densidade: _confortável · compacta_.  
- Tabelas: definir colunas prioritárias em mobile.  
- Não esconder ação destrutiva sem confirmação.

### 2.5 Microcopy (tom)

- Tom de voz: _direto · formal · amigável_  
- Idioma da UI: _pt-BR · en · …_  
- CTA: verbo no infinitivo ou imperativo consistente em todo o app  
- Evitar jargão interno na UI

---

## 3. Acessibilidade (inegociável)

- Alvo: **WCAG 2.1 AA**  
- Navegação completa por teclado; foco visível  
- Não depender só de cor para status  
- `prefers-reduced-motion`: reduzir ou desligar animações não essenciais  
- Detalhes de implementação: `frontend-guidelines.md`

---

## 4. Premissas técnicas de produto (contexto para UI)

Preencha o que impacta experiência (o Architect detalha o resto na tech-spec):

| Tema | Premissa |
|------|----------|
| Auth na UI | _login obrigatório · papéis · telas públicas_ |
| Dados offline | _não · cache de leitura · …_ |
| i18n | _só pt-BR · multi-idioma futuro_ |
| Analytics de UX | _sem · eventos em CTAs principais_ |

---

## 5. Checklist rápido (feature com UI)

Antes de `./jojo approve` na fase UX:

- [ ] Alinhado a este arquivo (tokens, nav, forms, feedback)  
- [ ] Estados loading / empty / error / success definidos  
- [ ] A11y mínima considerada  
- [ ] Mobile/desktop cobertos se ambos forem alvo  
- [ ] Padrão novo (se houver) **registrado aqui**, não só na spec da feature  

---

## 6. Histórico de mudanças de premissa

Registre mudanças permanentes (append-only):

| Data | Mudança | Motivo |
|------|---------|--------|
| _AAAA-MM-DD_ | _ex.: Dark mode obrigatório_ | _…_ |
