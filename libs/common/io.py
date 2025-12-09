from __future__ import annotations

from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
_INPUT_DIR = _ROOT / "inputs"


def _day_str(day: int | str) -> str:
    day_int = int(day)
    return f"day{day_int:02d}"


def get_input_path(day: int | str, variant: str | None = None) -> Path:
    """Return the expected input path for a given day.

    Parameters
    ----------
    day: int | str
        Day number, e.g. 1 or "01".
    variant: str | None
        Optional suffix (e.g. "sample").
    """

    filename = _day_str(day)
    if variant:
        filename = f"{filename}.{variant}"
    return _INPUT_DIR / f"{filename}.txt"


def read_input(day: int | str, variant: str | None = None) -> str:
    """Read the entire input file as a string."""

    path = get_input_path(day, variant)
    if not path.exists():
        raise FileNotFoundError(
            f"Input for day {day} not found at {path}. Create it or adjust the path."
        )
    return path.read_text(encoding="utf-8").rstrip("\n")


def read_input_lines(day: int | str, variant: str | None = None) -> list[str]:
    """Read the input file and return a list of stripped lines."""

    content = read_input(day, variant)
    return [line.rstrip("\n") for line in content.splitlines()]
