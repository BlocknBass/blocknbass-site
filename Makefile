.PHONY: install

build:
	python setup.py bdist_wheel

#clean:
#	pass

install: venv
	.venv/bin/pip install -e "."

install-dev: venv
	.venv/bin/pip install -e ".[dev]"

install-prod:
	.venv/bin/pip install -e ".[prod]"
	echo "#! /bin/sh" > server
	# Bind to port 8080 as the expected configuration is to run this behind a NGINX reverse-proxy.
	echo ".venv/bin/gunicorn --workers=4 --worker-class=sync --bind=:8080 'blocknbass:create_app()'" >> server
	chmod +x server

venv:
	python3 -m venv --symlinks .venv