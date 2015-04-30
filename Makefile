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
	rm -rf build *egg* dist ./docs/_build .tox
	find . -name '*.pyc' -exec rm -f {} +

docs:
	$(VENVDIR)/bin/sphinx-build -b html -d $(SPHINX_BUILDDIR)/doctrees docs $(SPHINX_BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(SPHINX_BUILDDIR)/html/index.html"


