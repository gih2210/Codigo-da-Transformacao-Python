def maior_menor(numeros):
    maior = max(numeros)
    menor = min(numeros)

    return maior, menor


numeros = [10, 5, 8, 20, 3]

maior, menor = maior_menor(numeros)

print(f"Maior: {maior}")
print(f"Menor: {menor}")