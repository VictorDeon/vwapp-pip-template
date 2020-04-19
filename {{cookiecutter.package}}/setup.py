from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# Muda para o diretório desse arquivo
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='{{cookiecutter.package}}',
    version='{{cookiecutter.version}}',
    url='https://github.com/{{cookiecutter.author}}/{{cookiecutter.package}}',
    license='MIT License',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.email}}',
    keywords='{{cookiecutter.keywords}}',
    description=u'{{cookiecutter.description}}',
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
      'Development Status :: 4 - Beta',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7'
      'Topic :: Software Development :: Bug Tracking',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[]
)