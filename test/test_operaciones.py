import unittest
from sxnti import Sumar, Restar

class TestOperaciones(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(Sumar(2, 3), 5)
        
    def test_restar(self):
        self.assertEqual(Restar(5, 3), 2)
        
if __name__ == '__main__':
    unittest.main()