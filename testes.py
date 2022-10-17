import unittest
from calculadora import Calculadora


class TddExemplo(unittest.TestCase):
    def teste_soma(self):
        calc = Calculadora()
        result = calc.somar(-20, 40)
        self.assertEqual(20, result)


if __name__ == '__main__':
    unittest.main()
