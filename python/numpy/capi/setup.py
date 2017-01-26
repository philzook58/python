from distutils.core import setup, Extension
import numpy

#RUN
#python setup.py build_ext --inplace

# define the extension module
square_module = Extension('square', sources=['square.c'])
asquare_module = Extension('array_square', sources=['array_square.c'],include_dirs=[numpy.get_include()])

# run the setup
setup(ext_modules=[square_module, asquare_module])