.ONESHELL:
SHELL := /bin/bash
SRC = $(wildcard ./*.ipynb)

all: sql_formatter docs

sql_formatter: $(SRC)
	nbdev_build_lib
	touch sql_formatter

sync:
	nbdev_update_lib

docs_serve: docs
	cd docs && bundle exec jekyll serve

docs: $(SRC)
	nbdev_build_docs
	touch docs

test:
	nbdev_test_nbs

release: prepush &&\
	make-git-release &&\
	pypi &&\
	make-changelog &&\
	nbdev_bump_version

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist

prepush:
	nbdev_build_lib && nbdev_test_nbs && nbdev_build_docs

update_master:
	git checkout master && git pull
