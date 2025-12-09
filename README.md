# Advent of Code (multi-year)

Monorepo for Advent of Code solutions using Python and [uv](https://docs.astral.sh/uv/).

## Layout

-   `2025/01/`, `2025/02/`, ... — year/day solution folders (add another top-level folder for a new year).
-   `inputs/<year>/<day>.txt` — puzzle inputs; add variants with `.<variant>.txt` (e.g., `01.sample.txt`).
-   `utils/` — reusable helpers (I/O, algorithms, etc.).
-   `.vscode/tasks.json` — quick tasks to sync deps, test, or run a day.

## Requirements

-   Python 3.11+ (works great with 3.12).
-   uv installed: `pipx install uv` or see the docs linked above.

## Getting started

```bash
uv sync                        # install dependencies (project + dev)
uv run python -m pytest        # run tests
uv run python 2025/01/main.py  # run a day from the repo root
```

## Adding a new day/year

1. Copy an existing day folder (e.g., `2025/01`) into the appropriate year and day slot.
2. Drop your input into `inputs/<year>/<day>.txt` (and `<day>.sample.txt` for samples).
3. Implement `part1` and `part2`, and add tests under `tests/` that load the module from its path.

Happy puzzling! 🎄
