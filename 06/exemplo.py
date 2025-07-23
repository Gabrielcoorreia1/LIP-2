# Em Python, para tipos imutáveis (como números), a passagem é por valor.
# A função recebe apenas uma cópia do valor.

def tentar_modificar(numero):
    """Esta função recebe um número, o modifica e imprime o resultado."""
    print(f"   -> Dentro da função, o número recebido é: {numero}")
    numero = 100 # Modificação do parâmetro
    print(f"   -> Dentro da função, o número foi alterado para: {numero}")


# Variável original
numero_original = 10

print(f"O valor original do número é: {numero_original}")

# Chamada da função
print("Chamando a função 'tentar_modificar'...")
tentar_modificar(numero_original)
print("...função executada.")


# O valor original não é afetado pela execução da função.
print(f"O valor original do número após a função é: {numero_original}")
# com isso pode-se ver que recebemos apenas uma copia e não a referencia do numeor.