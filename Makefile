poetry.lock : pyproject.toml
	poetry lock

requirements.txt : poetry.lock
	poetry export --output requirements.txt

.PHONY: safety-check
safety-check: requirements.txt
	cat requirements.txt | poetry run safety check --full-report --stdin
