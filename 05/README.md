# Desafio 05 - Estruturas de Controle

## Proposta

O desafio consiste em desenvolver um programa simples que utilize estruturas de seleção, repetição e controle de fluxo, inserido em um contexto original. O objetivo é demonstrar o domínio sobre como controlar a ordem de execução das instruções em um programa.

## Solução

Foi desenvolvido um programa em Python chamado **"Simulador de Robô Coletor"**. A escolha do Python se deu pela sua sintaxe clara e legível.

O contexto é um robô que explora um campo em busca de recursos, mas possui uma capacidade de armazenamento limitada. O programa utiliza as três estruturas de controle exigidas:

1.  **Estrutura de Repetição (`for`):** Simula a exploração do robô por uma sequência de locais no campo.
2.  **Estrutura de Seleção (`if`/`elif`/`else`):** Permite ao robô tomar uma decisão com base no item encontrado em cada local (um recurso valioso, um recurso comum ou um obstáculo).
3.  **Controle de Fluxo (`continue` e `break`):**
    * `continue`: É usado quando o robô encontra um `obstaculo`, fazendo-o pular para o próximo local sem coletar nada.
    * `break`: É acionado quando o armazenamento do robô atinge a capacidade máxima, encerrando a exploração imediatamente.

O código completo no arquivo `robo_coletor.py`.