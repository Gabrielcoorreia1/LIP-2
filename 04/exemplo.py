# 1. Tipagem dinâmica: a variável 'dado' primeiro armazena um inteiro.
dado = 10
print(f"O valor é {dado} e o tipo é {type(dado)}")

# 2. Agora, a mesma variável armazena um texto. O tipo muda dinamicamente.
dado = "dez"
print(f"O valor agora é '{dado}' e o tipo mudou para {type(dado)}")

# 3. Tipagem forte em ação: Python não permite operações ambíguas.
# A linha abaixo, se fosse descomentada, causaria um ERRO DE EXECUÇÃO (TypeError),
# pois Python não sabe se deve somar ou concatenar.
# resultado = 10 + "5"
# print(resultado)

print("\nPython é fortemente tipado: uma operação como 10 + '5' resulta em erro.")