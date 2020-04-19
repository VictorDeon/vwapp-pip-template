from unittest import TestCase
from {{cookiecutter.package}} import *

class {{cookiecutter.package}}TestCase(TestCase):
    """
    {{cookiecutter.description}}
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

    def test_{{cookiecutter.package}}(self):
        """
        Teste {{cookiecutter.package}}.
        """

        self.assertEqual(True, True)
