package:
	# Cria o pacote no formato tar.gz e insere no diretório dist
	python3 setup.py sdist bdist_wheel

install_test:
	# Instala o pacote no formato tar.gz
	pip3 install ./dist/{{cookiecutter.package}}-{{cookiecutter.version}}.tar.gz

install:
	# instala o pacote publicado
	pip3 install {{cookiecutter.package}}

uninstall:
	# Desistalar o pacote tar.gz
	pip3 uninstall {{cookiecutter.package}}

pypi_test:
	# Enviando o pacote para o PyPI Test
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

pypi:
	# Enviando o pacote para o PyPI Live
	twine upload dist/*

flake8:
	# Roda a folha de estilo.
	flake8