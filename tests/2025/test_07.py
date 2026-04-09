from __future__ import annotations

from typing import Protocol, cast

from tests._helpers import PROJECT_ROOT, load_module

DAY07_PATH = PROJECT_ROOT / "2025" / "07" / "main.py"
SAMPLE_PATH = PROJECT_ROOT / "inputs" / "2025" / "07.sample.txt"


class Day07Module(Protocol):
    def part1(self, lines: list[str]) -> int: ...

    def part2(self, lines: list[str]) -> int: ...


day07 = cast(Day07Module, load_module("aoc2025_day07", DAY07_PATH))


def test_sample_splits_match_description() -> None:
    lines = SAMPLE_PATH.read_text(encoding="utf-8").splitlines()
    assert day07.part1(lines) == 21
    assert day07.part2(lines) == 40


def test_chain_reaction_with_adjacent_splitters() -> None:
    diagram = [
        "..S..",
        "..^..",
        ".^^^.",
        ".....",
    ]

    # First splitter creates two beams; the next row contains three splitters
    # that split the two incoming beams into three total beams.
    assert day07.part1(diagram) == 3
    # Quantum version keeps both timelines even when paths converge at the
    # middle column on the following row.
    assert day07.part2(diagram) == 4


def test_timelines_preserved_on_merge() -> None:
    diagram = [
        ".S.",
        ".^.",
        "^.^",
        "...",
    ]

    # Beams from the first splitter hit two splitters that both send beams
    # into the center column; quantum timelines add rather than merge.
    assert day07.part1(diagram) == 3
    assert day07.part2(diagram) == 2
