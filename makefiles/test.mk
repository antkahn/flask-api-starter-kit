### TEST
# ¯¯¯¯¯¯¯¯


.PHONY: test
test: ## Launch tests in their own docker container
	docker-compose run --rm testserver

.PHONY: coverage
test.coverage: ## Generate test coverage
	docker-compose run --rm testserver bash -c "python -m pytest --cov-report term --cov-report html:coverage --cov-config setup.cfg --cov=src/ test/"

test.lint: ## Lint python files with flake8
	docker-compose run --rm server bash -c "python -m flake8 ./src ./test"

test.safety: ## Check for dependencies security breach with safety
	docker-compose run --rm server bash -c "python vendor/bin/safety check"
