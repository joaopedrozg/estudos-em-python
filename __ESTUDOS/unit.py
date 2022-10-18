import unittest

class ConverteNumeroRomano:

    def __init__(self):

        self.digito_map = {'M':1000, 'D':500, 'C':100, 'L':50, 'V':5, 'I':1}

    def conerte_para_decimal(self, numero_romano):
        val = 0
        for char in numero_romano:
            val += self.digito_map[char]

        return val


class TestConverteNumeroRomano(unittest.TestCase):
    def setUp(self):
        print('Construir objeto da class ConverteNumeroRomano')
        self.cnr = ConverteNumeroRomano()
    def tearDown(self):
        print('Destruir objeto da class ConverteNumeroRomano')
        self.cnr = None

    def test_mil(self):
        self.assertEqual(1000, self.cnr.conerte_para_decimal('M'))

    def test_cem(self):
        self.assertEqual(100, self.cnr.conerte_para_decimal('C'))

    def test_cinquenta(self):
        self.assertEqual(50, self.cnr.conerte_para_decimal('L'))

    def test_vazio(self):
        self.assertTrue(self.cnr.conerte_para_decimal('') == 0)
        self.assertFalse(self.cnr.conerte_para_decimal('') > 0)


if __name__ == '__main__':
    unittest.main()
