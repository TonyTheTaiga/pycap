from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='PyCap',
    version='0.1',
    author='Taiga Ishida',
    author_email='taigaishida.dev@gmail.com',
    url='https://github.com/TonyTheTaiga/pycap',
    description="CLI for coinmarketcap to do various things",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click', 'requests',
    ],
    entry_points='''
        [console_scripts]
        pycap=init:cli
    ''',
)
