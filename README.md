# Advent of Code 2025

Monorepo setup for solving Advent of Code 2025 puzzles with Python and [uv](https://docs.astral.sh/uv/).

## Layout

- `days/` — one package per day (start with `day01`).
- `inputs/` — raw puzzle inputs (ignored from git by default; add your own files).
- `libs/common/` — shared helpers (parsing, I/O, etc.).
- `.vscode/tasks.json` — quick tasks to run a day or the test suite.

## Requirements

- Python 3.11+ (works great with 3.12).
- uv installed: `pipx install uv` or see the docs linked above.

## Getting started

```bash
uv sync           # install dependencies
uv run pytest     # run tests
uv run python -m days.day01.main  # run day01
```

## Adding a new day

1. Copy `days/day01` to `days/dayXX`.
2. Add the new package to `tool.uv.workspace.members` in `pyproject.toml`.
3. Drop your input into `inputs/dayXX.txt` (git-ignored).
4. Implement `part1` and `part2`, add tests under `tests/`.

Happy puzzling! 🎄
