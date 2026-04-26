# AGENTS.md
## Project mission
ChemQ Assist is an AI-assisted chemistry, structural biology, materials, and quantum-readiness intelligence platform.
The first product direction is an opportunity scanner that helps users identify:
- protein targets;
- AlphaFold structure availability;
- chemistry and materials use cases;
- literature and patent evidence;
- South African and international partners;
- feasible MVP pilots;
- future quantum/HPC pathways.

## Repository layout
- `docs/` contains concept notes, strategy, methods, and outreach material.
- `data/raw/` contains untouched source data.
- `data/interim/` contains intermediate working data.
- `data/processed/` contains cleaned reusable data.
- `data/external/` contains public reference templates and external metadata.
- `notebooks/` contains exploratory analysis.
- `src/chemq/` contains reusable Python code.
- `tests/` contains pytest tests.
- `outputs/` contains generated reports, tables, and figures.
- `prompts/` contains reusable AI workflow prompts.
- `backlog/` contains sprint tasks.

## Development setup
Prefer:
- Python 3.11 or 3.12
- uv for dependency management
- pytest for testing
- pydantic for schemas
- httpx for API clients
- pandas/polars for tabular data
- duckdb for local analytical storage

## Commands
Install dependencies:
```bash
uv sync
```

Run tests:
```bash
uv run pytest
```

Run formatting/checks when available:
```bash
uv run pytest
```

## Research integrity rules
- Do not make scientific claims without clearly stating the evidence source.
- Clearly distinguish between experimentally validated structures and predicted structures.
- Clearly distinguish literature evidence, patent evidence, model output, and business interpretation.
- Caveat AlphaFold outputs where confidence is low or biological interpretation is uncertain.
- Do not present early computational screening as clinical, regulatory, or wet-lab validation.

## Data rules
- Never modify files in `data/raw/`.
- Do not commit secrets, API keys, credentials, or private client data.
- Use `.env.example` for documenting required environment variables.
- Generated outputs must go to `outputs/`.
- Document external data sources in the relevant README or method note.

## Coding conventions
- Keep modules small and testable.
- Prefer clear schemas for data objects.
- Add tests for scoring logic and data transformations.
- Avoid large, hidden side effects.
- Use graceful failure for unavailable external APIs.
- Use offline fixtures for tests.

## Definition of done
A task is complete only when:
- changed files are listed;
- tests pass, or failures are explained;
- assumptions are documented;
- scientific limitations are noted;
- outputs are saved in the correct folder;
- no secrets are committed;
- the next recommended task is stated.

## Review guidelines
When reviewing changes:
- check for unsupported scientific claims;
- check that raw data is not modified;
- check that scoring formulas are transparent;
- check that functions have tests;
- check that external dependencies are justified;
- check that outputs are reproducible.
