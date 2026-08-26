from faker import Faker

import utilidades

fake = Faker("pt_BR")

print("=== UTILIDADES ===")
print("Soma:", utilidades.soma(10, 5))
print("Subtração:", utilidades.subtrair(10, 5))
print("Multiplicação:", utilidades.multiplicar(10, 5))
print("Potência:", utilidades.potencializar(10, 5))

print("\n=== DADOS FALSOS ===")
print("Nome:", fake.name())
print("E-mail:", fake.email())
print("Telefone:", fake.phone_number())