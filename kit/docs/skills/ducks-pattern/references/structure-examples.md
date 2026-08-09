# Ducks — exemplos (L3)

## Estrutura Padrão de um Duck

```
src/ducks/[feature-name]/
├── types.ts          (Constants: ACTION_TYPES)
├── actions.ts        (Action creators)
├── reducer.ts        (State logic)
├── selectors.ts      (State queries)
├── utils.ts          (Helper functions)
├── constants.ts      (Feature-specific constants)
└── index.ts          (Public exports only)
```

### types.ts — Constants

```typescript
export const FETCH_USERS = 'users/FETCH_USERS'
export const FETCH_USERS_SUCCESS = 'users/FETCH_USERS_SUCCESS'
export const FETCH_USERS_ERROR = 'users/FETCH_USERS_ERROR'

export type User = {
  id: string
  name: string
  email: string
}

export type UsersState = {
  items: User[]
  loading: boolean
  error: string | null
}
```

### actions.ts — Action Creators

```typescript
import * as types from './types'

export const fetchUsers = () => ({
  type: types.FETCH_USERS,
})

export const fetchUsersSuccess = (users: types.User[]) => ({
  type: types.FETCH_USERS_SUCCESS,
  payload: users,
})

export const fetchUsersError = (error: string) => ({
  type: types.FETCH_USERS_ERROR,
  payload: error,
})
```

### reducer.ts — State Logic

```typescript
import * as types from './types'

const initialState: types.UsersState = {
  items: [],
  loading: false,
  error: null,
}

export default function reducer(
  state = initialState,
  action: any
): types.UsersState {
  switch (action.type) {
    case types.FETCH_USERS:
      return { ...state, loading: true }
    case types.FETCH_USERS_SUCCESS:
      return { ...state, items: action.payload, loading: false }
    case types.FETCH_USERS_ERROR:
      return { ...state, error: action.payload, loading: false }
    default:
      return state
  }
}
```

### selectors.ts — State Queries

```typescript
import { RootState } from '../../store'

export const selectUsers = (state: RootState) => state.users.items
export const selectUsersLoading = (state: RootState) => state.users.loading
export const selectUsersError = (state: RootState) => state.users.error

export const selectUserById = (id: string) => (state: RootState) =>
  state.users.items.find(u => u.id === id)
```

### index.ts — Public API (Exports Only)

```typescript
export * as types from './types'
export * as actions from './actions'
export * as selectors from './selectors'
export { default as reducer } from './reducer'
```

---

## Aplicável A

### Backend (Node.js)

```
src/features/
├── users/
│   ├── types.ts        (Interfaces, enums)
│   ├── controller.ts   (Request handlers)
│   ├── service.ts      (Business logic)
│   ├── repository.ts   (DB queries)
│   ├── routes.ts       (Express routes)
│   └── index.ts        (Exports)
├── posts/
│   └── (same structure)
```

### Frontend (React)

```
src/ducks/
├── ui/                 (Dialogs, modals, themes)
├── auth/               (Login, tokens, permissions)
├── users/              (User CRUD)
├── posts/              (Post CRUD)
```

### Qualquer Domínio

```
src/domains/
├── [domain-name]/
│   ├── types.ts
│   ├── [business-logic-1].ts
│   ├── [business-logic-2].ts
│   ├── utils.ts
│   └── index.ts
```

---

## Validação (Enforcement)

### Estrutura Obrigatória

Cada duck DEVE ter:
- [ ] `types.ts` — Tipos/constants
- [ ] Lógica principal (actions.ts, reducer.ts, controller.ts, service.ts)
- [ ] `selectors.ts` ou `queries.ts` — Forma pública de acessar
- [ ] `index.ts` — Public API (exports só o necessário)
- [ ] Sem exports diretos de arquivos internos (use index.ts)

### Verificação

```bash
# Script: validate-ducks.sh
for duck in src/ducks/*/; do
  if [ ! -f "$duck/types.ts" ]; then echo "❌ $duck missing types.ts"; fi
  if [ ! -f "$duck/index.ts" ]; then echo "❌ $duck missing index.ts"; fi
done
```

---

