# Makefile for initializing a new project

activate:  ## Activate the Poetry virtual environment
	@echo "Activating virtual environment..."
	source .venv/bin/activate

# Install pre-commit hooks
pre-commit:  ## Install pre-commit hooks
	@echo "Installing pre-commit hooks..."
	pre-commit install

# Install dependencies and tools, and set up the project
initialize_all: pre-commit activate  ## Initialize all
	@echo "Project successfully initialized."

# Help command to show available options
help:  ## Show this help message
	@echo "Available commands:"
	@echo "  make pre-commit            Install pre-commit hooks"
	@echo "  make initialize_all        Initialize everything (venv, pre-commit)"