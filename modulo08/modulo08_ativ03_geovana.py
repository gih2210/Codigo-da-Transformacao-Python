class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"Carro: {self.marca} - {self.modelo}"

carro = Carro("Honda", "Civic")
print(carro)