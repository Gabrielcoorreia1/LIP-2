# Desafio 12 - Programação Lógica

## Proposta

O desafio consiste em modelar um pequeno problema lógico, como um quebra-cabeça ou uma genealogia, utilizando uma sintaxe inspirada na linguagem Prolog. O objetivo é demonstrar o entendimento sobre como representar conhecimento através de fatos e regras.

## Solução

Foi escolhido o problema de **árvore genealógica**, um exemplo clássico para a programação lógica. A solução abaixo define uma base de conhecimento com fatos (relações diretas) e regras (relações inferidas) e mostra como seriam feitas consultas a essa base.

A sintaxe é inspirada no Prolog, onde:
* `:-` significa "se" (condicional).
* `,` significa "e" (conjunção).
* Tudo que começa com letra maiúscula é uma variável.
* Tudo que começa com letra minúscula é um átomo (um valor constante).

---

### 1. Base de Conhecimento: Fatos

Os fatos são as informações que declaramos como sendo verdadeiras no nosso sistema. O texto a seguir define quem é o `genitor` de quem:

% Fato: genitor(Pai/Mãe, Filho/Filha).

genitor(joao, ana).
genitor(maria, ana).

genitor(joao, pedro).
genitor(maria, pedro).

genitor(pedro, carlos).
genitor(clara, carlos).

### 2. Base de Conhecimento: Regras

As regras nos permitem inferir novos fatos a partir dos que já existem.

**Regra para definir "irmão":**
A regra abaixo diz que `Pessoa1` e `Pessoa2` são irmãos se eles possuem um `Genitor` em comum e se não são a mesma pessoa.

% Regra: irmao(Pessoa1, Pessoa2).

irmao(Pessoa1, Pessoa2) :-
    genitor(Genitor, Pessoa1),
    genitor(Genitor, Pessoa2),
    Pessoa1 \= Pessoa2.

**Regra para definir "avô/avó":**
A regra abaixo diz que `Avo` é avô ou avó de `Neto` se `Avo` é genitor de `Genitor`, e `Genitor` é genitor de `Neto`.

% Regra: avo(Avo, Neto).

avo(Avo, Neto) :-
    genitor(Avo, Genitor),
    genitor(Genitor, Neto).

### 3. Realizando Consultas (Exemplos)

Com a base de conhecimento definida, poderíamos fazer "perguntas" ao sistema. As consultas abaixo e suas respostas também são parte da explicação.

* **Consulta:** "João é o genitor de Ana?"
    
    ?- genitor(joao, ana).
    
    * **Resultado esperado:** true. (Sim, pois é um fato definido.)

* **Consulta:** "Ana e Pedro são irmãos?"
    
    ?- irmao(ana, pedro).
    
    * **Resultado esperado:** true. (O sistema usa a regra `irmao`.)

* **Consulta:** "Quem são os avós de Carlos?"
    
    ?- avo(X, carlos).
    
    * **Resultado esperado:** X = joao. e X = maria. (O sistema encontra todos os valores para a variável `X`.)