# Adaptadores de ferramenta (opcional)

jojo-ai é **LLM-agnóstico**.

## Contrato único

Qualquer agent de código / assistente de IA deve ler:

1. `agents.md` (régua + `### Features`)
2. `system-design.md`
3. Saída de `./jojo run` (`.ai/jojo-run.json`)
4. Runbooks em `kit/docs/agents/` e skills em `kit/docs/skills/<id>/SKILL.md`

**Não** existe dependência de fornecedor (nenhuma marca de modelo é requisito).

## O que há nesta pasta

Skills portáteis no formato aberto **Agent Skills** (`SKILL.md`), úteis se a sua ferramenta descobrir skills por pasta:

| Pasta | Uso |
| --- | --- |
| `jojo-init/` | Como instalar o kit via `./jojo init` |
| `jojo-run/` | Como rodar o backlog via `./jojo run` |

Sua IDE/CLI pode:

- apontar para estes paths, ou  
- copiar/symlink para o diretório de skills **dela** (se tiver um)

jojo **não** exige isso. A CLI + `agents.md` bastam.

## O que não fazer

- Criar `CLAUDE.md` / `GEMINI.md` / regras proprietárias como fonte da verdade  
- Duplicar a régua por ferramenta — edite só `agents.md`  
- Assumir um único runtime de LLM no projeto  
