---
name: ducks-pattern
type: architecture
category: organization
description: Modular code organization by feature, not by file type. Use when adding features or organizing modules.
usedFor: [backend, frontend, organization]
appliesTo: [all]
requiredKnowledge: [modular-architecture, project-structure]
conflicts: [layer-by-type-folders]
mandatory: true
---

# Skill: Ducks Pattern (Guardrail)

## Quando usar

- Toda nova feature/domínio em projetos jojo-ai.
- Reorganização de código espalhado por tipo (`actions/`, `reducers/`, `types/`).

## Quando NÃO usar

- Utilities globais e componentes reutilizáveis → `src/shared/`.
- Shared cross-cutting (não é um “duck” de feature).

## O Que É

**Ducks Pattern** = Coloca tudo relacionado a um "conceito/feature" em uma pasta única, em vez de espalhado por `actions/`, `reducers/`, `types/`, etc.

```
❌ BAD (fragmentado):
src/
├── actions/
│   ├── users.js
│   └── posts.js
├── reducers/
│   ├── users.js
│   └── posts.js
├── types/
│   ├── USERS.js
│   └── POSTS.js

✅ GOOD (Ducks):
src/
├── ducks/
│   ├── users/
│   │   ├── actions.js
│   │   ├── reducer.js
│   │   ├── types.js
│   │   ├── selectors.js
│   │   └── index.js (exports)
│   └── posts/
│       ├── actions.js
│       ├── reducer.js
│       ├── types.js
│       ├── selectors.js
│       └── index.js (exports)
```

---

## Por Que É Obrigatório

1. **Coesão** — Código relacionado junto
2. **Escalabilidade** — Fácil adicionar features
3. **Testabilidade** — Mock/test um "duck" inteiro
4. **Manutenibilidade** — Achar o que precisa é óbvio
5. **Padronização** — Todos sabem onde procurar

---

## Estrutura Padrão de um Duck

Pasta por feature com public API (`index`). Detalhes: [references/structure-examples.md](references/structure-examples.md).

## Anti-Padrões

❌ **Não faça:**

```typescript
// ❌ Importar internals direto
import { someHelper } from 'src/ducks/users/utils.ts'

// ❌ Exports diretos sem index
export * from './actions.ts'
export * from './reducer.ts'

// ❌ Features em pastas aleatórias
src/utils/users/
src/helpers/posts/
src/lib/auth/

// ❌ Mixin de tipos de features
src/types/users.ts
src/types/posts.ts
```

✅ **Faça:**

```typescript
// ✅ Importar via index (public API)
import { actions, selectors } from 'src/ducks/users'

// ✅ Exports via index
// (index.ts controla o que é público)

// ✅ Tudo em ducks/[name]/ ou features/[name]/
src/ducks/users/
src/ducks/posts/

// ✅ Tipos com a feature
src/ducks/users/types.ts
src/ducks/posts/types.ts
```

---

## Checklist — Feature Nova

Ao criar nova feature:

- [ ] Criada pasta `src/ducks/[feature-name]/`
- [ ] `types.ts` com tipos + constants
- [ ] Lógica principal (actions/reducer ou service/repository)
- [ ] `selectors.ts` ou `queries.ts`
- [ ] `utils.ts` se houver helpers
- [ ] `index.ts` com public API
- [ ] Nenhum import direto de arquivo interno
- [ ] Tests em `__tests__/` na mesma pasta

---

## Exemplo Completo — Feature de Autenticação

```
src/ducks/auth/
├── types.ts
│   ├── User interface
│   ├── AuthState interface
│   ├── ACTION_TYPES constants
│
├── actions.ts
│   ├── loginRequest()
│   ├── loginSuccess(user)
│   ├── loginError(error)
│   ├── logout()
│
├── reducer.ts
│   ├── Initial state
│   ├── Handle all actions
│
├── selectors.ts
│   ├── selectUser()
│   ├── selectIsAuthenticated()
│   ├── selectError()
│
├── utils.ts
│   ├── parseJWT()
│   ├── validateToken()
│
├── __tests__/
│   ├── actions.test.ts
│   ├── reducer.test.ts
│   ├── selectors.test.ts
│
└── index.ts
    export { types, actions, selectors, reducer, utils }
```

Uso em outro componente:

```typescript
import { actions, selectors } from 'src/ducks/auth'

// ✅ Correto — via public API
const user = useSelector(selectors.selectUser)
dispatch(actions.loginRequest(email, password))
```

---

## Guardrail Obrigatório

**Este padrão é OBRIGATÓRIO em todo projeto que usa jojo-ai.**

Validação:
- [ ] Projeto segue Ducks Pattern
- [ ] Cada feature em pasta dedicada
- [ ] Public API clara (index.ts)
- [ ] Sem imports diretos de internals
- [ ] Tests colocation

---

**Quando usar:** Toda nova feature/domínio  
**Quando NÃO usar:** Utilities globais, componentes reusáveis (esses ficam em `src/shared/`)  
**Exceção:** Shared code vai em `src/shared/` (não em ducks/)

---

**Leia também:** `system-design.md` §2 (camadas e pastas **deste** projeto).  
Se §2 definir estrutura diferente de “ducks” nominal mas **coesa por feature**, siga o `system-design.md` e mantenha o espírito do padrão (feature-first, public API, sem pasta por tipo de arquivo).
