PYTHON = python3
SRC = src

.PHONY: all clean docs lint test typecheck scan

clean:
	rm -rf dist build docs/build *.egg-info

docs:
	cd docs && $(MAKE) html

lint:
	$(PYTHON) -m flake8
	$(PYTHON) -m black .
	$(PYTHON) -m isort .

test:
	$(PYTHON) -m tox

typecheck:
	$(PYTHON) -m mypy
	$(PYTHON) -m pytype

scan:
	$(PYTHON) -m bandit -f yaml -r $(SRC)
