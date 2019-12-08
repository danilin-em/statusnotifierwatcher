init:
	@python3 -m virtualenv venv
	@( \
		source venv/bin/activate; \
		python3 -m pip install -r requirements.txt; \
		python3 -m pip install -r requirements.dev.txt; \
	)
	@echo "Activate venv: source venv/bin/activate"
lint:
	@( \
		source venv/bin/activate; \
		python -m flake8 *.py; \
		python -m pylint --disable=fixme *.py; \
	)
clean:
	@rm -rf venv
