from unittest import TestCase
from funcoes.bora import *


class TestandoBora(TestCase):

    def test_soma_is_working(self):
        n1 = 10
        n2 = 12
        self.assertEqual(soma(n1, n2), 22)

    def test_raiz_ta_funfando(self):

        type_test = "A"
        with self.assertRaises(TypeError):
            raiz(type_test)

        value_test = -9
        with self.assertRaises(ValueError):
            raiz(value_test)

        self.assertEqual(raiz(144), 12)

    def test_lista(self):
        self.assertTrue(listadef(0))
        self.assertFalse(listadef(1))
