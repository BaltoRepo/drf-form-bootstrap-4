SHELL=/bin/bash

.PHONY: clean

clean-build: ## remove build artifacts
	rm -rf build/
	rm -rf dist/
	rm -frf *.egg-info

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

clean: clean-build clean-pyc

install: clean
	python setup.py install

lint: ## check style with flake8
	flake8 .

runserver: clean
	PYTHONPATH=$(shell pwd) django-admin runserver --settings=runserver_settings

sdist: clean
	python setup.py sdist

upload: lint sdist
	# You must have a ~/.pypirc file with your username and password.
	# You don't need to register new packages first- just upload and
	# everything is taken care of.
	twine upload dist/*.tar.gz
