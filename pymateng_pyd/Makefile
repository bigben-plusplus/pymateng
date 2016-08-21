
all: clean test

INSTALL_FLAGS  = --prefix "."

build:
	@python setup.py build ${BUILD_FLAGS}

build_ext:
	@python setup.py build_ext --inplace 

install:
	@python setup.py install --skip-build ${INSTALL_FLAGS}

test: clean build_ext
	@python -c "import _pymateng; print(dir(_pymateng));"
	@python -c "import sys; sys.path.append('./src'); import pymateng; print(dir(pymateng));"

clean:
	@-python setup.py clean --all
	@-rm src/*pymateng.py* src/pymateng_wrap.c
	@-rm -rf Lib
	@-rm _pymateng.pyd
