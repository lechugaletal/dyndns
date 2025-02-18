.ONSHELL:
PROJECT_NAME=$(shell echo $${PWD##*/})
PY_VERSION=$(shell python3 -VV)
PY_VENV_VERSION=$(shell .venv/bin/python3 -VV)

.PHONY: help
help:   	## Show this help menu.
		@echo 'Usage: make <target>'
		@echo ''
		@echo 'Targets:'
		@grep '##' Makefile | grep -vE 'grep|PWD'

.PHONY: info
info:   	## Show project environment info.
		@echo 'Current environment:'
		@echo
		@echo '  > Project: $(PROJECT_NAME)'
		@echo '  > global version: $(PY_VERSION)'
		@if [ -f .venv/bin/python3 ]; then echo -n '  > venv version: ' && .venv/bin/python3 -VV ; fi

.PHONY: initvenv
initvenv:	## Create python virtual environment with venv.
		@echo 'Creating virtual environment...'
		@rm -rf .venv
		@python3 -m venv .venv
		@echo 'Installing dependencies...'
		@.venv/bin/pip3 install -r requirements.txt
		@echo ''
		@echo ''
		@echo 'Run "source .venv/bin/activate" to enable the environment'

.PHONY: cleanup
cleanup:	## Remove project tmp files and virtual environment.
		@echo 'Cleaning up project...'
		@rm -rf .venv
		@rm -rf .cache
		@find ./ -name '__pycache__' -exec rm -rf {} \;
		@echo 'Done!'