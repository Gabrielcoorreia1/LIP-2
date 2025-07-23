# Desafio 03 - Descrições Sintáticas e Semânticas

## Proposta

[cite_start]O desafio consiste em criar uma mini-gramática fictícia para uma linguagem inventada, demonstrando o conceito com um exemplo prático de análise léxica[cite: 17, 18]. O objetivo é mostrar como as regras formais (sintaxe) de uma linguagem são definidas e como o código-fonte é quebrado em seus componentes básicos (tokens) antes de ser processado.

## Solução

Para este desafio, foi criada uma linguagem fictícia chamada **"GeoSimples"**, projetada para dar comandos básicos de desenho geométrico. A solução abaixo descreve seus componentes léxicos (o vocabulário) e sua gramática (as regras de formação de frases), finalizando com um exemplo prático.

---

### **1. A Linguagem GeoSimples**

A GeoSimples permite criar formas geométricas simples com um comando. Sua estrutura é `CRIAR <forma> <tamanho>;`.

### **2. Análise Léxica (Os "Tokens")**

A análise léxica é o primeiro passo, onde o código-fonte é dividido em "tokens" (peças fundamentais). Para a GeoSimples, os tokens são:

* **COMANDO**: A palavra reservada `CRIAR`.
* **FORMA**: Uma palavra que define a forma. Pode ser `QUADRADO`, `CIRCULO` ou `LINHA`.
* **NUMERO**: Um valor inteiro que representa o tamanho.
* **PONTO_VIRGULA**: O caractere `;` que finaliza uma instrução.

### **3. Gramática Fictícia (As "Regras")**

A gramática define como os tokens podem ser combinados para formar uma instrução válida. Usando uma notação similar à BNF (Backus-Naur Form), as regras são:

* **Leitura da regra:** Uma `<instrucao>` válida é composta por um token `COMANDO`, seguido por um `<tipo_forma>`, um `NUMERO` e finalizada com um `PONTO_VIRGULA`.

---

### **4. Exemplo Prático**

Vamos analisar um código escrito em GeoSimples.

**Código de exemplo:**

**Análise Léxica (Tokenização):**

Ao processar o código acima, o analisador léxico produziria a seguinte sequência de tokens:

1.  `CRIAR` -> **[COMANDO]**
2.  `QUADRADO` -> **[FORMA]**
3.  `10` -> **[NUMERO]**
4.  `;` -> **[PONTO_VIRGULA]**

**Análise Sintática:**

Após a tokenização, o analisador sintático verifica se a sequência de tokens `[COMANDO, FORMA, NUMERO, PONTO_VIRGULA]` obedece à regra da gramática.

* A sequência corresponde exatamente à regra `<instrucao>`.
* Portanto, o código `CRIAR QUADRADO 10;` é **sintaticamente válido** na linguagem GeoSimples.
