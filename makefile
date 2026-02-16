.PHONY: new-eval run-eval

test:
	uv run pytest tests/

new-eval:
	uv run python3 -m src.evals.generator.run

run-eval:
	uv run python3 -m src.evals.pipeline --case cases/$(CASE)