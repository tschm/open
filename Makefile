.DEFAULT_GOAL := help

.PHONY: venv
venv: ## Create the virtual environment
	@curl -LsSf https://astral.sh/uv/install.sh | sh
	@uv venv


.PHONY: install
install: venv ## Install a virtual environment
	@uv pip install --upgrade pip
	@uv pip install -r requirements.txt --prerelease=allow


.PHONY: fmt
fmt: venv ## Run autoformatting and linting
	@uv pip install pre-commit
	@uv run pre-commit install
	@uv run pre-commit run --all-files


.PHONY: help
help:  ## Display this help screen
	@echo -e "\033[1mAvailable commands:\033[0m"
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}' | sort


.PHONY: marimo
marimo: install ## Install Marimo
	@uv pip install marimo
	@uv run marimo edit notebooks

.PHONY: rest
rest: install ## Start rest api
	@echo Visit localhost:8000/docs
	@uv run uvicorn openbb_core.api.rest_api:app --host 0.0.0.0 --port 8000 --reload

