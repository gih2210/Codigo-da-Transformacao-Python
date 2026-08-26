from faker import Faker

fake = Faker("pt_BR")


# UTILIDADES
def soma(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def potencializar(a, b):
    return a ** b


# PROGRAMA
print("=== UTILIDADES ===")

print("Soma:", soma(10, 5))
print("Subtração:", subtrair(10, 5))
print("Multiplicação:", multiplicar(10, 5))
print("Potência:", potencializar(10, 5))


print("\n=== DADOS FALSOS ===")

print("Nome:", fake.name())
print("E-mail:", fake.email())
print("Telefone:", fake.phone_number())