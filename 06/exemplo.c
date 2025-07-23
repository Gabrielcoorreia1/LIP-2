#include <stdio.h>

// 1. Passagem por VALOR
// A função recebe uma CÓPIA da variável 'numero'.
void modificar_por_valor(int numero) {
    printf("   -> (Valor) Dentro da função, valor recebido: %d\n", numero);
    numero = 100; // Modifica apenas a cópia local.
    printf("   -> (Valor) Valor alterado para: %d\n", numero);
}

// 2. Passagem por REFERÊNCIA
// A função recebe o ENDEREÇO de memória da variável 'numero'.
void modificar_por_referencia(int *ponteiro_numero) {
    printf("   -> (Ref) Dentro da função, ponteiro recebido aponta para valor: %d\n", *ponteiro_numero);
    *ponteiro_numero = 100; // Modifica o valor no endereço de memória original.
    printf("   -> (Ref) Valor alterado para: %d\n", *ponteiro_numero);
}


int main() {
    int numero_original = 10;

    // --- Teste com Passagem por VALOR ---
    printf("--- Testando passagem por VALOR ---\n");
    printf("Valor original ANTES da função: %d\n", numero_original);
    modificar_por_valor(numero_original);
    printf("Valor original DEPOIS da função: %d (não mudou)\n", numero_original);

    numero_original = 10;

    // --- Teste com Passagem por REFERÊNCIA ---
    printf("--- Testando passagem por REFERÊNCIA ---\n");
    printf("Valor original ANTES da função: %d\n", numero_original);
    // Passamos o endereço da variável com o operador '&'
    modificar_por_referencia(&numero_original); 
    printf("Valor original DEPOIS da função: %d (MUDOU!)\n", numero_original);
    // Como não recebos uma copia e sim a referencia ao numeor original, a função consegue modificar o valor mesmo fora do scopo

    return 0;
}