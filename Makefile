

.PHONY: help
help: ## Show this help
	@echo "\nSpecify a command. The choices are:\n"
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[0;36m%-12s\033[m %s\n", $$1, $$2}'
	@echo ""

.PHONY:
sync:
	uv sync --extra dev

.PHONY: format
format:
	uv run ruff format

.PHONY: lint
typecheck:
	uv run mypy packages --no-incremental --pretty --warn-unused-configs

.PHONY: check
check:
	uv run ruff --extend-select TCH

.PHONY: test
test:
	uv run pytest
