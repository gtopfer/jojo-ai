---
name: jojo-init
description: >
  Install jojo-ai SPECKIT into a repository via ./jojo init.
  Use when the user wants to bootstrap or update jojo on a project.
---

# jojo init (adapter)

Instala o kit **jojo-ai** no repositório alvo via CLI.  
Funciona com **qualquer** agent de código — não depende de fornecedor de LLM.

## Passos

1. Confirme o diretório alvo.
2. Rode (a partir do repo fonte jojo-ai, ou `./jojo` já no projeto):

```bash
./jojo init /caminho/do/projeto
./jojo detect /caminho/do/projeto
```

### Update

Se o alvo já tem jojo:

- **Substitui** gerenciados: `kit/`, `./jojo`, `LICENSE`
- **Preserva** humanos: `agents.md`, `system-design.md`, `CHANGELOG.md`

```bash
./jojo init .                 # install ou update
./jojo init . --reset-human   # também reseta templates humanos
./jojo init . --skip-sync
```

## Depois do init

```text
1. agents.md Seção 1 + ### Features
2. system-design.md
3. Qualquer agent de código no app + ./jojo run
```

Não reimplemente o install em shell ad-hoc — use a CLI `jojo`.
