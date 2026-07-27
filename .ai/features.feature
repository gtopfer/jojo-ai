# language: pt
# Nota: o Gherkin tem suporte nativo a português — a diretiva "# language: pt" ativa
# as palavras-chave Funcionalidade/Cenário/Dado/Quando/Então/E abaixo.
# Substitua (ou acrescente) cenários conforme a feature ativa em `.ai/specs/`.
# Ferramentas de BDD (Cucumber, Behave, etc.) reconhecem esta sintaxe.

Funcionalidade: [Nome da Feature]

  Como um(a) [persona]
  Eu quero [ação]
  Para que [valor]

  Cenário: [Comportamento principal — a preencher com o QA/PM]
    Dado que [pré-condição]
    Quando [ação do usuário ou sistema]
    Então [resultado observável esperado]
