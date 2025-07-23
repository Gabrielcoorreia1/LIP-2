# Contexto: Um robô coletor explora um campo em busca de recursos.
# Ele tem uma capacidade máxima de armazenamento.

# -- Configurações Iniciais --
capacidade_maxima = 10
armazenamento_atual = 0
# O campo a ser explorado, representado por uma lista de itens.
campo_de_recursos = ["metal", "cristal", "obstaculo", "metal", "cristal", "cristal", "metal"]

print(f"--- Iniciando a exploração do robô ---")
print(f"Capacidade máxima do armazenamento: {capacidade_maxima}")
print("-" * 35)

# 1. ESTRUTURA DE REPETIÇÃO (for)
# O robô percorre cada item no campo de recursos.
for item_encontrado in campo_de_recursos:

    print(f"Analisando local... Item encontrado: {item_encontrado}")

    # 2. ESTRUTURA DE SELEÇÃO (if/elif/else)
    # O robô decide o que fazer com base no item.
    if item_encontrado == "cristal":
        print(">> Recurso valioso! Adicionando 2 ao armazenamento.")
        armazenamento_atual += 2
    
    elif item_encontrado == "metal":
        print(">> Recurso comum. Adicionando 1 ao armazenamento.")
        armazenamento_atual += 1

    elif item_encontrado == "obstaculo":
        print("!! Obstáculo encontrado. Ignorando e passando para o próximo local.")
        # 3. CONTROLE DE FLUXO (continue)
        # Pula o resto do código do loop e vai para a próxima iteração.
        continue 

    # Verificação de capacidade após a coleta
    if armazenamento_atual >= capacidade_maxima:
        print("\n!! ATENÇÃO: Armazenamento cheio!")
        # 3. CONTROLE DE FLUXO (break)
        # Encerra o loop 'for' prematuramente.
        break

    print(f"   (Armazenamento atual: {armazenamento_atual}/{capacidade_maxima})\n")


print("-" * 35)
print("--- Exploração Finalizada ---")
print(f"Total de recursos coletados: {armazenamento_atual}")