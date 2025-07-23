# Desafio 11 - Programação Funcional

## Proposta

O desafio consiste em implementar uma solução funcional que utilize recursão e funções de alta ordem para resolver um problema real ou fictício. O objetivo é aplicar os conceitos do paradigma funcional, como imutabilidade, e o uso de funções como cidadãos de primeira classe.

## Solução

Foi escolhido um problema real e comum em análise de dados: **processar uma lista de vendas**. O objetivo é filtrar as vendas que atendem a um critério, aplicar um desconto e, por fim, calcular o total. A solução foi implementada em **JavaScript**.

Os seguintes conceitos do paradigma funcional foram aplicados:

1.  **Funções de Alta Ordem (`.filter()` e `.map()`):**
    * `.filter()`: Método de array que cria uma nova lista contendo apenas as vendas com valor acima de R$ 100,00. Ele recebe uma função (neste caso, uma *arrow function*) como critério.
    * `.map()`: Método de array que aplica uma transformação a cada item da lista filtrada, gerando uma nova lista com os valores após um desconto de 10%. Ele também recebe uma *arrow function* que define a transformação.

2.  **Recursão:**
    * Uma função `somaRecursiva` foi criada para calcular a soma total dos valores da lista final.Em vez de usar um laço `for`, a função chama a si mesma com uma parte menor da lista até que a lista esteja vazia (caso base), demonstrando a abordagem recursiva para processar coleções, conforme solicitado no desafio.

O código, que demonstra um fluxo de dados claro e o uso de `const` para favorecer a imutabilidade, está no arquivo `processamentoVendas.js`.