import unittest
import cepel/cepel.py

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(soma(1,2), 4)
