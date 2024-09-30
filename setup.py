from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("mastering.pyx"),
    zip_safe=False,
)
