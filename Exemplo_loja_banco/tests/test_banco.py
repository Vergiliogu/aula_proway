from unittest import TestCase, mock
from funcoes.banco import *


class TestBanco(TestCase):

    @mock.patch("funcoes.banco.Banco")
    @mock.patch("funcoes.banco.datetime.datetime")
    def test_gerar_codigo_boleto(self, mock_datetime, mock_banco):
        mock_datetime.now.return_value = "0000-00-00 00:00:00.000000"
        mock_banco.codigo_banco.return_value = "180"

        dados = dict(valor=10.56)
        resultado = Banco().gerar_codigo_boleto(dados)
        self.assertEqual(resultado, "180000000000000000000001056")

        mock_datetime.now.assert_called_once()
