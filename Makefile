.DEFAULT_GOAL := help

.PHONY: uv
venv: ## Install uv/uvx
	@curl -LsSf https://astral.sh/uv/install.sh | sh

.PHONY: fmt
fmt: uv ## Run autoformatting and linting
	@uvx pre-commit install
	@uvx pre-commit run --all-files

.PHONY: help
help:  ## Display this help screen
	@echo -e "\033[1mAvailable commands:\033[0m"
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}' | sort

.PHONY: marimo
marimo: uv ## Install Marimo
	#@uv pip install marimo
	@uvx marimo edit --sandbox notebooks/openbb-demo.py

.PHONY: rest
rest: uv ## Start rest api
	@echo Visit localhost:8000/docs
	@uvx uvicorn openbb_core.api.rest_api:app --host 0.0.0.0 --port 8000 --reload

.PHONY: openbb
openbb: uv ## Start openbb cli
	@uvx openbb
