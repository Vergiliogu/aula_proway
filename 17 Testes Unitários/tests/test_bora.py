import unittest
from funcoes.bora import *


class TestBora(unittest.TestCase):

    def test_soma_funciona(self):
        n1 = 10
        n2 = 20
        self.assertEqual(soma(n1, n2), 30)
