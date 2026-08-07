---
name: jojo-init
description: >
  Install jojo-ai SPECKIT into a repository (agents.md, system-design.md,
  kit/, CLI). Use when the user runs /jojo-init, says "jojo init",
  "instalar jojo", "setup spekit", or wants to bootstrap a new project
  without copying files by hand.
---

# /jojo-init

Instala o kit **jojo-ai** no repositório alvo via CLI (sem copiar pastas à mão).

## Passos

1. Confirme o diretório alvo (default: raiz do projeto atual).
2. Rode:

```bash
# a partir do repo jojo-ai (fonte do kit), ou ./jojo já no projeto
./jojo init /caminho/do/projeto
```

### Detecção + update automático

Se o alvo **já tem jojo** (`.ai/jojo-install.json`, `./jojo` + `kit/`, etc.):

1. **Remove** artefatos gerenciados: `kit/`, `./jojo`, `LICENSE`, skills `.grok/skills/jojo-*`
2. **Reinstala** versões novas da fonte
3. **Preserva** edições humanas: `agents.md`, `system-design.md`, `CHANGELOG.md`

```bash
./jojo detect .          # ver se já tem jojo + versão
./jojo init .            # install OU update automático
./jojo init . --reset-human   # update e também reseta templates humanos
./jojo init . --force         # igual --reset-human nos arquivos humanos
./jojo init . --skip-sync     # sem npm run sync
```

3. O que é gerenciado (sempre substituído no update):
   - `kit/`, `jojo`, `LICENSE`, `.grok/skills/jojo-init`, `.grok/skills/jojo-run`

4. O que é humano (preservado no update):
   - `agents.md`, `system-design.md`, `CHANGELOG.md`

5. Oriente o humano:

```text
1. Edite agents.md → ### Features
2. Edite system-design.md
3. ./jojo run  ou  /jojo-run
```

6. Não reimplemente o install em shell ad-hoc — use a CLI `jojo`.

## Se `jojo` não existir no projeto

- Use o path absoluto do repositório fonte jojo-ai:  
  `/path/to/jojo-ai/jojo init .`
- Ou clone/instale o kit e rode de novo.
