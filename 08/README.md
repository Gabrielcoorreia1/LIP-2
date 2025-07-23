# Desafio 08 - Programação Orientada a Objetos

## Proposta

O desafio consiste em modelar uma hierarquia simples de classes em um domínio de preferência, como personagens, transportes ou serviços. O objetivo é aplicar os conceitos fundamentais da Programação Orientada a Objetos (POO), como classes, herança e polimorfismo.

## Solução

Para este desafio, foi utilizado o domínio **"Veículos"** e a linguagem **Java**. A estrutura criada demonstra os principais pilares da POO. Devido às convenções do Java, cada classe é definida em seu próprio arquivo.

A hierarquia é composta por:

1.  **Classe Base (`Veiculo.java`):**
    * Representa o conceito mais genérico, com atributos comuns a todos os veículos: `marca` e `modelo`.

2.  **Classes Derivadas (`Carro.java` e `Bicicleta.java`):**
    * **Herança:** Ambas as classes herdam de `Veiculo` usando a palavra-chave `extends`.
    * **Especialização:** Adicionam seus próprios atributos (`portas`, `tipo`) e métodos (`abastecer()`, `pedalar()`).
    * **Polimorfismo:** Ambas sobrescrevem o método `exibirInfo()` (com a anotação `@Override`) para exibir suas informações de forma específica.
