### FORMAT
# ¯¯¯¯¯¯¯¯

format.black: ## Run black on every file
	docker-compose run --rm server bash -c "python vendor/bin/black src/ test/ --exclude vendor/"

format.isort: ## Sort imports
	docker-compose run --rm server bash -c "python vendor/bin/isort -rc src/ test/ --skip vendor/ --skip src/models/__init__.py"
