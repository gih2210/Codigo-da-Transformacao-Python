from datetime import datetime

nome = input("Qual é o seu nome? ")
hora = datetime.now().strftime("%H:%M:%S")

print(f"Olá, {nome}! Seja bem-vindo(a)!")
print(f"Agora são {hora}.")