from setuptools import setup, find_packages


setup(
    name='quina',
    version='0.0.7',
    description='PySide2 MVVM Framework',
    url='https://github.com/KD-Group/quina',
    author='KD-Group',
    author_email='sfzhou.scut@gmail.com',

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
