def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

def boas_vindas():
    print("Bem-vindo ao projeto!")

boas_vindas()

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

print("Soma:", soma(n1, n2))
print("Multiplicação:", multiplicacao(n1, n2))