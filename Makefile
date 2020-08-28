.PHONY: help
help: ## see what commands are avaiable
	@echo "Reference card for usual actions."
	@echo "Here are available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: sortimports
sortimports: ## sort imports
	pip install isort
	isort -rc .


.PHONY: build
build: ## build the package
	. venv/bin/activate
	python setup.py sdist bdist_wheel


.PHONY: upload
upload: ## upload to pypi
	. venv/bin/activate
	python setup.py sdist bdist_wheel


.PHONY: test
test: ## run unittests
	. venv/bin/activate
	pytest
