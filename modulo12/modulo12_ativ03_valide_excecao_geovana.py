import unittest

# Função a ser testada com validação de entradas
def dividir(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Os parâmetros devem ser números.")
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    return a / b


class TestValidacaoEntradas(unittest.TestCase):

    # Teste para divisão por zero
    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    # Teste para entradas que não são números (texto, listas, etc.)
    def test_entradas_nao_numericas(self):
        with self.assertRaises(TypeError):
            dividir("10", 2)
            
        with self.assertRaises(TypeError):
            dividir(10, "2")


if __name__ == '__main__':
    unittest.main()