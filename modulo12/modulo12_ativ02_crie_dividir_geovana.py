import unittest

# Classe Calculadora
class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b


# Classe de testes unitários
class TestCalculadora(unittest.TestCase):

    def setUp(self):
        # Executado antes de cada método de teste
        self.calc = Calculadora()

    def test_somar(self):
        self.assertEqual(self.calc.somar(10, 5), 15)

    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(10, 5), 5)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(4, 3), 12)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

    def test_divisao_por_zero(self):
        # Verifica se o erro ValueError é lançado na divisão por zero
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)


if __name__ == '__main__':
    unittest.main()