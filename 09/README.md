# Desafio 09 - Concorrência

## Proposta

O desafio consiste em explicar a diferença entre threads e processos e, em seguida, implementar um exemplo personalizado de concorrência. O objetivo é demonstrar o entendimento dos conceitos básicos de execução paralela de tarefas.

## Solução

A solução está dividida em duas partes: uma explicação conceitual sobre processos e threads e um exemplo prático de concorrência usando a linguagem **Java**, conforme sugerido no material de apoio.

### Diferença entre Processos e Threads

A melhor forma de entender a diferença é através de uma analogia com um navegador de internet:

* **Processo:** Pense no navegador em si (ex: Chrome, Firefox) como um processo. Ele é um programa independente, com seu **próprio espaço de memória isolado**. Se você abrir dois navegadores diferentes, eles não compartilham memória. Criar um processo é uma operação "pesada" para o sistema operacional.

* **Thread:** Pense nas abas abertas dentro de um único navegador. Cada aba pode ser vista como uma thread. Elas são "leves" e **compartilham o mesmo espaço de memória** do processo principal (o navegador). Isso permite que elas se comuniquem de forma rápida e fácil. Se uma thread travar (uma aba para de responder), ela pode afetar as outras, mas não necessariamente fechará o processo inteiro.

### Exemplo

O código Java simula duas tarefas sendo executadas de forma concorrente: um "downloader" e um "processador".

A solução foi estruturada em três arquivos:
* `Downloader.java` e `Processador.java`: Duas classes que implementam a interface `Runnable`. O método `run()` de cada uma contém a lógica da tarefa a ser executada.
* `Main.java`: A classe principal que cria e gerencia as threads. Ela instancia as tarefas, as associa a objetos `Thread` e as inicia. O método `join()` é usado para garantir que o programa principal espere a conclusão de ambas as threads.

Ao rodar o programa, as mensagens de ambas as tarefas aparecem de forma intercalada no console, demonstrando a concorrência.