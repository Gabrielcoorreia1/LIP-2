# Desafio 03 - Descrições Sintáticas e Semânticas

## Proposta

O desafio consiste em criar uma mini-gramática fictícia para uma linguagem inventada, demonstrando o conceito com um exemplo prático de análise léxica. O objetivo é mostrar como as regras formais de uma linguagem são definidas e como o código-fonte é quebrado em seus componentes básicos antes de ser processado.

## Solução

Para este desafio, foi criada uma linguagem fictícia chamada **"Geometry"**, projetada para dar comandos básicos de desenho geométrico. A solução abaixo descreve seus componentes léxicos e sua gramática (regras), junto com um exemplo prático.

---

### **1. A Linguagem Geometry**

A Geometry permite criar formas geométricas simples com um comando. Sua estrutura é `CRIAR <forma> <tamanho>;`.

### **2. Análise Léxica**

A análise léxica é o primeiro passo, onde o código-fonte é dividido. No nosso caso teremos:

* **COMANDO**: A palavra reservada `CRIAR`.
* **FORMA**: Uma palavra que define a forma. Pode ser `QUADRADO`, `CIRCULO` ou `LINHA` ou quais quer forma geometrica existente.
* **NUMERO**: Um valor inteiro que representa o tamanho.
* **PONTO_VIRGULA**: O caractere `;` que finaliza uma instrução.

### **3. Gramática**

A gramática define como as instruções podem ser combinados para formar comandos validos. Usando uma notação similar as regras são:

* **Leitura da regra:** Uma `<instrucao>` válida é composta por um `COMANDO`, seguido por um `<tipo_forma>`, um `NUMERO` e finalizada com um `PONTO_VIRGULA`.

---

### **4. Exemplo Prático**

Vamos analisar um código escrito em Geometry.

**Código de exemplo:**

**Análise Léxica:**

Ao processar o código acima, o analisador léxico produziria a seguinte sequência de tokens:

1.  `CRIAR` -> **[COMANDO]**
2.  `QUADRADO` -> **[FORMA]**
3.  `10` -> **[NUMERO]**
4.  `;` -> **[PONTO_VIRGULA]**

**Análise Sintática:**

O analisador sintático verifica se a sequência `[COMANDO, FORMA, NUMERO, PONTO_VIRGULA]` obedece à regra da gramática.

* A sequência corresponde exatamente à regra `<instrucao>`.
* Portanto, o código `CRIAR QUADRADO 10;` é **sintaticamente válido**