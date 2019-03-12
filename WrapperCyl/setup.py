from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

sourcefiles  = ['PyCyl.pyx', 'Cyl.cpp']
compile_opts = ['-std=c++17']
ext=[Extension('*',
            sourcefiles,
            extra_compile_args=compile_opts,
            language='c++')]

setup(
  ext_modules=cythonize(ext)
)