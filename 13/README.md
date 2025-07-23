# Desafio 13 - Linguagens para Scripts e Web

## Proposta

O desafio consiste em criar um pequeno roteiro ou script usando uma linguagem de script para automação ou manipulação de dados, com um contexto próprio.

## Solução

Foi desenvolvido um script em **Python** com o contexto de um **Gerador de Nomes de Usuário Aleatórios**.

O objetivo do script é criar nomes de usuário criativos e únicos de forma automática, combinando palavras de listas predefinidas e adicionando números aleatórios. Este é um exemplo de script útil para gerar dados de teste ou sugerir opções em um formulário de cadastro.

Para isso, foi utilizado o módulo padrão do Python:
* **`random`**: Para fazer escolhas aleatórias de palavras nas listas e para gerar os números.

### Como o Script Funciona

1.  **Listas de Palavras:** O script contém duas listas: uma de adjetivos e uma de substantivos.
2.  **Interação com o Usuário:** O programa pergunta ao usuário quantos nomes ele deseja gerar.
3.  **Geração Aleatória:** Para cada nome a ser criado, o script:
    * Escolhe um adjetivo aleatório da lista.
    * Escolhe um substantivo aleatório da lista.
    * Gera um número aleatório entre 10 e 99.
4.  **Combinação e Exibição:** As três partes (adjetivo, substantivo e número) são combinadas para formar o nome de usuário final, que é então exibido no console.

O código completo da implementação está no arquivo `gerador_nomes.py`.