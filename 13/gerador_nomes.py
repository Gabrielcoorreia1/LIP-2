import random

adjetivos = [
    "rapido", "veloz", "agil", "sonolento", "curioso", "valente",
    "esperto", "sabio", "vermelho", "azul", "verde", "dourado"
]

substantivos = [
    "leao", "tigre", "rio", "sol", "lua", "fantasma",
    "guerreiro", "mago", "dragao", "corvo", "lobo", "trovao"
]

def gerar_nomes_aleatorios(quantidade):
    
    print("\n--- Gerando Nomes de Usuário ---\n")
    if quantidade <= 0:
        print("Por favor, insira um número maior que zero.")
        return

    for i in range(quantidade):
        adjetivo_sorteado = random.choice(adjetivos)
        substantivo_sorteado = random.choice(substantivos)

        numero_aleatorio = random.randint(10, 99)

        nome_gerado = f"{adjetivo_sorteado}_{substantivo_sorteado}{numero_aleatorio}"

        print(f"Nome {i+1}: {nome_gerado}")

    print("\n--- Geração Concluída ---")

if __name__ == "__main__":
    print("--- Bem-vindo ao Gerador de Nomes de Usuário ---")
    
    try:
        num_nomes = int(input("Quantos nomes de usuário você quer gerar? "))
        gerar_nomes_aleatorios(num_nomes)

    except ValueError:
        print("\nErro: Entrada inválida. Por favor, digite um número inteiro.")