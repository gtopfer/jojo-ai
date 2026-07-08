# Skill: Checklist de Code Review

Execute este checklist antes de declarar qualquer implementação concluída. É agnóstico de linguagem/framework — adapte os comandos exatos à stack do projeto.

## 1. Integridade Estrutural
Para cada arquivo criado ou modificado, releia-o por completo após qualquer edição de busca-e-substituição. Falha comum: uma operação de substituição altera só parte de um bloco e deixa código duplicado ou órfão para trás.
- Nenhuma declaração duplicada de função/classe/tipo
- Nenhum código morto sobrando de uma edição parcial
- Tamanho do arquivo condizente com o que ele faz (checagem de sanidade com `wc -l`)

## 2. Conformidade Arquitetural
- O código novo está na camada/pasta correta conforme a estrutura do projeto (ver `.ai/technical-spec.md`, se existir)
- Nenhum import que viole camadas (ex.: lógica de domínio/negócio importando infraestrutura ou UI)
- Segue as regras de nomenclatura e estilo de `.ai/global.instructions`

## 3. Build e Checagem de Tipos
Rode o comando de build/typecheck do projeto (ex.: `tsc --noEmit`, `go build`, `mypy`, `cargo check`) e confirme zero erros.

## 4. Testes
Rode a suíte de testes do projeto. Todos devem passar — zero falhas conhecidas. Se a feature tem critérios de aceitação em `.ai/features.feature` ou numa spec, confirme que cada um está coberto por um teste.

## 5. Fundamentos de Segurança
- Validação de entrada (input) em todo dado externo/fornecido pelo usuário
- Nenhum segredo, chave ou credencial fixa no código (hardcoded) — deve vir de variáveis de ambiente (`.env`)
- Nenhum vetor de injeção óbvio (SQL, comando, XSS) introduzido

## Saída Esperada

```
Code Review — APROVADO
- Declarações duplicadas: nenhuma
- Código órfão: nenhum
- Conformidade arquitetural: OK
- Build/typecheck: 0 erros
- Testes: X passando
```

Ou, se algo falhou:

```
Code Review — REPROVADO
- [arquivo]:[linha] — [problema]
- Correção aplicada: [o que foi feito]
```
