poetry.lock : pyproject.toml
	poetry lock

requirements.txt : poetry.lock
	poetry export --output requirements.txt
