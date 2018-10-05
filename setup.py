from setuptools import setup, find_packages

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
        price=app.scripts.price:cli
    ''',
)
