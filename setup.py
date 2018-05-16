import quina
from setuptools import setup, find_packages


setup(
    name=quina.__name__,
    version=quina.__version__,
    description=quina.__description__,
    url=quina.__github__,
    author=quina.__author__,
    author_email=quina.__email__,

    license='GPL-3.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],

    keywords='PySide2 MVVM',
    packages=find_packages(exclude=['docs', 'tests', 'examples']),
    install_requires=['PySide2', 'typing'],
    extras_require={'test': ['flake8', 'pytest', 'pytest-cov']}
)
