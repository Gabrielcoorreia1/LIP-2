# Desafio 07 - Implementação de Subprogramas

## Proposta

O desafio consiste em desenhar e explicar a pilha de chamadas de um exemplo recursivo. O objetivo é demonstrar o entendimento de como as chamadas de função são gerenciadas na memória, especialmente em casos de recursão.

## Solução

O exemplo escolhido para a demonstração é a clássica função recursiva para o cálculo de **fatorial**. O código de exemplo está no arquivo `fatorial.py`.

A explicação a seguir descreve o comportamento da pilha de chamadas (call stack) para a execução de `fatorial`, vamos usar como paramentro nessa pilha `fatorial(3)`. Esta descrição serve como um roteiro para o diagrama visual da pilha.

### Explicação da Pilha de Chamadas para `fatorial(3)`

A pilha de chamadas é uma estrutura de dados que o programa usa para saber qual função está em execução. Em uma recursão, cada nova chamada é "empilhada" sobre a anterior.

#### **Fase 1: Empilhamento (Resumo)**

A fase de empilhamento começa quando `fatorial(3)` é chamada e adicionada à pilha. Como seu resultado depende de `fatorial(2)`, a execução de `fatorial(3)` é pausada e uma nova chamada a `fatorial(2)` é empilhada sobre a anterior. Esse processo se repete sucessivamente: `fatorial(2)` chama `fatorial(1)`, e `fatorial(1)` chama `fatorial(0)`. A cada nova chamada, um novo quadro (contendo os dados daquela função) é colocado no topo da pilha, e a função anterior fica em estado de espera. A pilha cresce até atingir a chamada do caso base, `fatorial(0)`.

#### **Fase 2: O Caso Base**

A função `fatorial(0)` não faz uma nova chamada recursiva. Ela entra na condição `if n == 0` e simplesmente retorna o valor `1`, iniciando o processo de desempilhamento.

#### **Fase 3: Desempilhamento (Pop)**

1.  **Primeiro retorno:** `fatorial(0)` retorna `1` para a função que a chamou (`fatorial(1)`) e é removida da pilha.
2.  **Segundo retorno:** `fatorial(1)` recebe o `1`, calcula `1 * 1 = 1`, retorna o resultado para `fatorial(2)` e é removida da pilha.
3.  **Terceiro retorno:** `fatorial(2)` recebe o `1`, calcula `2 * 1 = 2`, retorna o resultado para `fatorial(3)` e é removida da pilha.
4.  **Retorno final:** `fatorial(3)` recebe o `2`, calcula `3 * 2 = 6`, retorna o resultado para o programa principal e é removida da pilha.

O resultado final, `6`, é obtido e a pilha de chamadas relacionada a essa computação fica vazia.

[imagem_fatorial_recursivo](fatorial.png)]