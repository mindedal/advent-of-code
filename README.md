# Advent of Code (multi-year)

Monorepo for Advent of Code solutions using Python and [uv](https://docs.astral.sh/uv/).

## Layout

- `2025/01/`, `2025/02/`, ... — year/day solution folders (add another top-level folder for a new year).
- `inputs/<year>/<day>.txt` — puzzle inputs; add variants with `.<variant>.txt` (e.g., `01.sample.txt`).
- `utils/` — reusable helpers (I/O, algorithms, etc.).
- `tests/` — regression tests for each day.
- `uv.lock` — locked dependency graph managed by `uv`.

## Requirements

- Python 3.11+ (works great with 3.12).
- uv installed: `pipx install uv` or see the docs linked above.

## Getting started

```bash
uv sync                        # install dependencies (project + dev)
uv run pytest                  # run tests
uv run ruff check .            # lint the repo
uv run ruff format .           # format the repo
uv run ty check                # strict type checking
uv run python 2025/01/main.py  # run a day from the repo root
```

## Adding a new day/year

1. Copy an existing day folder (e.g., `2025/01`) into the appropriate year and day slot.
2. Drop your input into `inputs/<year>/<day>.txt` (and `<day>.sample.txt` for samples).
3. Implement `part1` and `part2`, and add typed tests under `tests/`.

## Quality checks

This repo is managed with `uv`, formatted and linted with `ruff`, and type-checked with `ty` with all rules enabled. A good local loop is:

```bash
uv sync
uv run ruff check .
uv run ruff format .
uv run ty check
uv run pytest
```

Happy puzzling! 🎄
