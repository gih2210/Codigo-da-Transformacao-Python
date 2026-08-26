import random
import math

numero = random.randint(1, 100)

print("=== JOGO DE ADIVINHAÇÃO ===")

tentativa = int(input("Digite um número de 1 a 100: "))

if tentativa == numero:
    print("Você acertou!")
else:
    print("Você errou!")
    print("O número era:", numero)

print("Raiz quadrada:", round(math.sqrt(numero), 2))