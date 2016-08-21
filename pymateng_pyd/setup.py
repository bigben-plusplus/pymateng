# setup.py

import distutils
from distutils.core import setup, Extension

MATLABROOT = "D:\\Program Files\\MATLAB\\R2010a"
mod_pymateng = Extension("_pymateng", \
	sources = ["src/pymateng.c", "src/pymateng.i"], \
	include_dirs = [MATLABROOT+"\\extern\\include"], \
	library_dirs = [MATLABROOT+"\\extern\\lib\\win32\\microsoft"], \
	libraries = ["libeng"]
	)

setup (
	name = "pymateng",
	version = "1.0",
	author = "bigben",
    description = "A python binding to Matlab Engine",
	ext_modules = [mod_pymateng]
)
