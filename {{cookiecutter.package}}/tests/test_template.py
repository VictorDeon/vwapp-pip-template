from unittest import TestCase
from {{cookiecutter.src}} import *


class PackageTestCase(TestCase):
    """
    Para rodar o caso de teste primeiro tem que gerar o tar.gz do pacote.
    """

    def setUp(self):
        """
        Método executado a cada teste.
        """

        pass

    def tearDown(self):
        """
        Método executado após cada teste.
        """

        pass

    def test_success(self):
        """
        Teste para o caso de sucesso!.
        """

        self.assertEqual(True, True)
