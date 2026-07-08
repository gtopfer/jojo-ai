# Skill: Loop de Execução Autônoma (Planejar → Escrever → Testar → Avaliar → Refatorar)

Protocolo para trabalhar numa tarefa com mínima intervenção humana, mantendo-se dentro de limites seguros e reversíveis.

## O Loop

```
1. PLAN (planejar)     — reafirme a tarefa contra .ai/template.specs / os cenários .feature. Identifique os arquivos a tocar.
2. WRITE (escrever)    — implemente a menor mudança que satisfaz o passo atual (veja .ai/skills/tdd.md para a ordem test-first).
3. TEST (testar)       — rode a suíte de testes, build/typecheck e qualquer análise estática relevante.
4. EVALUATE (avaliar)  — passou? Bate com os cenários Gherkin? Alguma regressão em comportamento adjacente?
5. REFACTOR (refatorar) — limpe agora que o comportamento está verificado; rode TEST de novo após qualquer refatoração.
```

## Autocorreção em Caso de Falha (Self-Healing)

Quando um teste, build ou comando falha:
1. Leia o erro/stack trace real — não adivinhe a causa.
2. Localize a causa raiz (não só a linha do sintoma).
3. Corrija, depois rode o loop completo de novo a partir de TEST — uma correção não reverificada não conta.
4. Registre o que falhou e o que corrigiu nas suas notas de trabalho (não precisa ir em `docs/CHANGELOG.md`, a menos que mude o comportamento/escopo final).

## Condições de Parada (obrigatórias — nunca entre em loop infinito)

Escale para o humano em vez de tentar de novo quando:
- A mesma causa raiz sobrevive a **3 tentativas de correção** seguidas
- Corrigir a falha exigiria uma decisão fora da spec atual (nova dependência, mudança de schema, mudança de arquitetura não coberta por um ADR existente)
- A falha é de infraestrutura/ambiente, não do código que você escreveu (credenciais ausentes, serviço inacessível, CI instável sem relação com a mudança)
- Uma correção tocaria um arquivo ou sistema explicitamente fora do escopo da tarefa

Ao escalar: diga o que foi tentado, o que falhou em cada tentativa, e a pergunta/decisão específica que precisa do humano. Nunca abandone a tarefa silenciosamente nem declare sucesso sobre um estado que ainda falha.

## Definição de "concluído" para uma iteração do loop
- [ ] Suíte de testes passa limpa (ver `.ai/skills/tdd.md`)
- [ ] Checklist de `.ai/skills/code-review.md` passa
- [ ] O resultado bate com os cenários Gherkin do arquivo `.feature`, não só "compila"
- [ ] Nenhum arquivo fora do escopo foi alterado para "fazer funcionar"
