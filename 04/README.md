# Desafio 04 - Tipos de Dados

## Proposta

O desafio propõe comparar a forma como os tipos de dados são tratados em três linguagens de programação diferentes. A demonstração deve ser feita com exemplos de código breves e comentados para ilustrar as principais características e diferenças entre os sistemas de tipagem.

## Solução

Para este desafio, foram escolhidas as linguagens C, Python e JavaScript, conforme sugerido no material de apoio da disciplina. A comparação foca em como cada uma lida com a declaração de variáveis e operações entre tipos diferentes, destacando os conceitos de tipagem estática, dinâmica, forte e fraca.

Os exemplos de código completos estão nos arquivos `exemplo.c`, `exemplo.py` e `exemplo.js.

---

### **1. C: Tipagem Estática e Forte**

* **O que significa:** O tipo de cada variável **deve ser declarado** antes do uso e **não pode ser alterado** durante a execução. O compilador impõe regras rígidas, impedindo operações entre tipos incompatíveis.
* **No código (`exemplo.c`):** A variável `idade` é declarada como `int` e não pode receber um valor de outro tipo. Tentar fazer isso impede o programa de ser compilado.

---

### **2. Python: Tipagem Dinâmica e Forte**

* **O que significa:** O tipo é associado ao valor, não à variável. Uma mesma variável pode armazenar um número e, depois, um texto. Apesar de dinâmico, o Python é **forte** e não permite operações ambíguas (como somar número com texto), gerando um erro em tempo de execução.
* **No código (`exemplo.py`):** A variável `dado` muda de `int` para `str`. A tentativa de somar `10 + "5"` é comentada, pois causaria um `TypeError`, mostrando a força da tipagem.

---

### **3. JavaScript: Tipagem Dinâmica e Fraca**

* **O que significa:** Assim como Python, é dinâmica. A grande diferença é a tipagem **fraca**, que significa que o JavaScript tenta **forçar a conversão** de tipos para que uma operação funcione, em vez de gerar um erro. Isso pode levar a comportamentos inesperados.
* **No código (`exemplo.js`):** A operação `10 + "5"` não gera um erro. O JavaScript realiza uma **coerção de tipo**, convertendo o número `10` para uma string e concatenando os valores, resultando na string `"105"`.
