# Desafio 02 - Ambientes de Programação

## Proposta

Neste desafio, a proposta é elaborar um diagrama próprio que explique o funcionamento de compiladores, interpretadores e máquinas virtuais, utilizando exemplos de linguagens de programação para ilustrar cada conceito. O objetivo é diferenciar visualmente como o código-fonte se transforma em instruções executáveis em cada um desses ambientes.

## Solução

A solução apresentada é um guia textual dividido em três partes para a criação de diagramas que representam o fluxo de execução em ambientes compilados, interpretados e baseados em máquinas virtuais.

---

### 1. Compilador


---

* **O que ele faz:** O compilador é um programa que traduz **todo** o seu código-fonte de uma vez só, gerando um novo arquivo. Esse arquivo, chamado de "executável" (ex: `.exe` no Windows), contém instruções de baixo nível que o processador do computador consegue entender e executar diretamente. Após a compilação, você não precisa mais do compilador para rodar o programa.

[diagrama do compilador](Compilador.pdf)
---
### 2. Interpretador
---

* **O que ele faz:** O interpretador executa seu código-fonte **linha por linha**, em tempo real. Ele lê uma instrução, a traduz e a executa imediatamente, para então passar para a próxima. Ele não cria um arquivo executável separado. Por isso, o interpretador precisa estar presente toda vez que você quiser rodar o seu script.

[diagrama do interpretador](Interpretadorr.pdf)
---



### 3. Abordagem Híbrida
---

* **O que ela faz:** É uma abordagem híbrida. Primeiro, o código-fonte é **compilado** para um código intermediário chamado *bytecode*. Esse bytecode não é executável diretamente pelo processador, mas é universal. Em seguida, a Máquina Virtual (JVM, no caso do Java), que funciona como um **interpretador** para esse bytecode, o traduz para as instruções nativas do computador onde está rodando. Isso garante a portabilidade: o mesmo bytecode pode rodar em Windows, macOS ou Linux, desde que a JVM esteja instalada.

[diagrama do modelo hibrido](Hibrido.pdf)