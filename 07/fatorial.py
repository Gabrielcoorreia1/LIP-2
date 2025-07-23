def fatorial(n):

    if n == 0:
        return 1
    
    else:
        resultado_parcial = n * fatorial(n - 1)
        return resultado_parcial

n = 3

resultado_final = fatorial(n)

print(f"O fatorial de {n} é {resultado_final}")

