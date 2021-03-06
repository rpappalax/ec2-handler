VENVDIR = ./venv
BINDIR = $(VENVDIR)/bin
PYTHON = $(BINDIR)/python
PIP = $(BINDIR)/pip
INSTALL = $(PIP) install
MAKEFILE_LIST=Makefile
SPHINX_BUILDDIR = docs/_build


.PHONY: all build test run clean docs 

all:	build test

build: $(VENVDIR)/COMPLETE
$(VENVDIR)/COMPLETE: requirements.txt
	virtualenv --no-site-packages --python=`which python` \
	    --distribute $(VENVDIR)
	$(INSTALL) -r ./requirements.txt
	$(PYTHON) ./setup.py develop
	touch $(VENVDIR)/COMPLETE

test:
	$(BINDIR)/nosetests

run:
	$(BINDIR)/demo

clean:
	rm -rf venv *egg* .tox
	find . -name '*.pyc' -exec rm -f {} +

