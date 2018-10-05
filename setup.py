from setuptools import setup, find_packages

setup(
    name='PyCap',
    version='0.1',
    author='Taiga Ishida',
    author_email='taigaishida.dev@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click', 'requests',
    ],
    entry_points='''
        [console_scripts]
        price=app.magic.price:cli
    ''',
)
