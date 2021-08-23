test:
	poetry run pytest src/

coding_standard:
	poetry run isort --gitignore src/
	poetry run black src/
	poetry run mypy src/

tdd:
	poetry run ptw src
