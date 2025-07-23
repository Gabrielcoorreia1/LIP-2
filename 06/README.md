# Desafio 06 - Subprogramas

## Proposta

O desafio consiste em implementar funções que demonstrem a passagem de parâmetros por valor e por referência em linguagens de programação diferentes. O objetivo é ilustrar como a alteração de um parâmetro dentro de uma função afeta (ou não) a variável original.

## Solução

Foram escolhidas as linguagens C e Python, conforme sugerido, por demonstrarem claramente os dois conceitos. Em ambos os exemplos, o objetivo é o mesmo: uma função tenta alterar o valor de uma variável que foi declarada fora dela.

### **1. Passagem por Valor (Python)**

Python, ao lidar com tipos imutáveis como números, utiliza uma abordagem equivalente à passagem por valor. A função recebe uma cópia do valor da variável, e não a referência à variável original. Portanto, qualquer modificação no parâmetro fica restrita ao escopo da função.

* **No código (`exemplo.py`):** A função `tentar_modificar` recebe o valor de `numero_original`. Ao alterar o valor do parâmetro, a variável `numero_original` permanece intacta.

### **2. Passagem por Referência (Exemplo com C)**

A linguagem C permite simular a passagem por referência de forma explícita, utilizando ponteiros. Em vez de passar o valor, passamos o endereço de memória da variável. A função então utiliza esse endereço para acessar e modificar diretamente o valor da variável original.

* **No código (`exemplo.c`):** A função `modificar_por_referencia` recebe um ponteiro (`int *ponteiro_numero`). Ao modificar o valor apontado pelo ponteiro, a variável `numero_original` na função `main` é permanentemente alterada.