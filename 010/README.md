# Desafio 10 - Gerenciamento de Memória

## Proposta

O desafio consiste em pesquisar como ocorre a gestão de memória em duas linguagens distintas e montar um comparativo. O objetivo é contrastar as diferentes filosofias e responsabilidades no ciclo de vida da memória em cada linguagem.

## Solução

Foram escolhidas as linguagens **C** e **Java**, pois representam dois modelos opostos de gerenciamento de memória: manual e automático, respectivamente. 

* **Gerenciamento Manual (C):** O programador tem total controle e responsabilidade sobre a alocação e, crucialmente, a liberação da memória do programa.
* **Gerenciamento Automático (Java):** A linguagem, através da Máquina Virtual Java (JVM), gerencia a memória de forma automática, utilizando um processo chamado *Garbage Collector* (Coletor de Lixo).

A seguir, os principais pontos são comparados.

---

### Comparativo: Gerenciamento de Memória (C vs. Java)

#### **1. Alocação de Memória**

* **Em C (Manual):** O programador aloca memória explicitamente usando funções como `malloc()` ou `calloc()`.
    ```c
    // Aloca espaço para 10 inteiros.
    int *arr = (int*) malloc(10 * sizeof(int));
    ```

* **Em Java (Automático):** A memória para objetos é alocada com a palavra-chave `new`.
    ```java
    // Aloca espaço para um objeto ArrayList.
    ArrayList<String> lista = new ArrayList<>();
    ```

#### **2. Liberação de Memória**

* **Em C (Manual):** O programador **deve** liberar a memória que alocou, usando a função `free()`. Esquecer de fazer isso causa um "vazamento de memória" (*memory leak*). 
    ```c
    // Libera a memória que foi alocada anteriormente.
    free(arr);
    ```

* **Em Java (Automático):** A liberação é feita automaticamente pelo *Garbage Collector* (GC). O GC identifica e remove objetos que não são mais referenciados por nenhuma parte do programa.

#### **3. Responsabilidade**

* **Em C (Manual):** A responsabilidade é **totalmente do programador**. Ele precisa gerenciar o ciclo de vida completo da memória.

* **Em Java (Automático):** A responsabilidade é **primariamente da JVM / Garbage Collector**. O programador se preocupa em criar os objetos, mas não em destruí-los.

#### **4. Principal Risco**

* **Em C (Manual):** O principal risco são os **vazamentos de memória** (esquecer de usar `free()`) e os **ponteiros soltos** (*dangling pointers*), que ocorrem ao tentar acessar uma área de memória que já foi liberada.

* **Em Java (Automático):** O risco são as **pausas no sistema** para que o GC possa executar sua limpeza, o que pode impactar a performance de aplicações sensíveis ao tempo. Além disso, o controle menos rigoroso pode levar a um consumo de memória maior que o necessário.

#### **5. Controle vs. Simplicidade**

* **Em C (Manual):** Oferece **máximo controle** sobre como e quando a memória é usada. É ideal para programação de baixo nível (sistemas operacionais, drivers), mas sua complexidade o torna propenso a erros.

* **Em Java (Automático):** Oferece **máxima simplicidade** e segurança, eliminando uma classe inteira de erros comuns de memória. É ideal para aplicações de negócio, mas oferece menos controle fino sobre a memória.