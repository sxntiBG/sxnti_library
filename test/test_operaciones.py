import unittest
from sxnti import Sumar, Restar, Multiplicar, Dividir

class TestOperaciones(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(Sumar(2, 3), 5)
        self.assertEqual(Sumar(1, 2, 3, 4), 10)
        self.assertEqual(Sumar(), 0)  # Caso sin parámetros

    def test_restar(self):
        self.assertEqual(Restar(5, 3), 2)
        self.assertEqual(Restar(10, 2, 3), 5)
        with self.assertRaises(ValueError):
            Restar()  # Caso sin parámetros

    def test_multiplicar(self):
        self.assertEqual(Multiplicar(2, 3), 6)
        self.assertEqual(Multiplicar(1, 2, 3, 4), 24)
        self.assertEqual(Multiplicar(5), 5)  # Caso con un solo parámetro
        with self.assertRaises(ValueError):
            Multiplicar()  # Caso sin parámetros

    def test_dividir(self):
        self.assertEqual(Dividir(10, 2), 5)
        self.assertEqual(Dividir(100, 2, 5), 10)
        with self.assertRaises(ValueError):
            Dividir()  # Caso sin parámetros
        with self.assertRaises(ZeroDivisionError):
            Dividir(10, 0)  # Caso división por cero

if __name__ == '__main__':
    unittest.main()