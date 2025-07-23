#include <stdio.h>

void main() {
    // Declaração explícita: 'idade' será SEMPRE um inteiro.
    int idade = 25;

    // A linha abaixo, se fosse descomentada, causaria um ERRO DE COMPILAÇÃO.
    // Você não pode atribuir um texto a uma variável do tipo inteiro em C.
    // idade = "vinte e cinco";

    printf("A idade é: %d\n", idade);
}