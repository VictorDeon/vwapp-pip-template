from unittest import TestCase


class PackageTestCase(TestCase):
    """
    Casos de teste.
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
