from __future__ import annotations

from typing import Protocol, cast

from tests._helpers import PROJECT_ROOT, load_module
from utils.io import read_input_lines

DAY04_PATH = PROJECT_ROOT / "2025" / "04" / "main.py"


class Day04Module(Protocol):
    def parse_input(self, lines: list[str]) -> object: ...

    def part1(self, grid: object) -> int: ...

    def part2(self, grid: object) -> int: ...


day04 = cast(Day04Module, load_module("aoc2025_day04", DAY04_PATH))


def test_sample_accessible_rolls() -> None:
    lines = read_input_lines(2025, 4, variant="sample")
    grid = day04.parse_input(lines)
    assert day04.part1(grid) == 13
    assert day04.part2(grid) == 43


def test_edge_cells_count_neighbours_correctly() -> None:
    # Grid where only center has 8 neighbours; others have fewer
    grid = day04.parse_input(
        [
            "@@@",
            "@@@",
            "@@@",
        ]
    )
    # Center has 8 neighbours => not accessible; corners have 3 (<4) but edges have 5.
    # Accessible: 4 corners only
    assert day04.part1(grid) == 4


def test_iterative_removal_clears_full_block() -> None:
    grid = day04.parse_input(
        [
            "@@@",
            "@@@",
            "@@@",
        ]
    )
    # Removals cascade until all 9 rolls are gone
    assert day04.part2(grid) == 9
