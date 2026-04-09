from __future__ import annotations

from typing import Protocol, cast

from tests._helpers import PROJECT_ROOT, load_module
from utils.io import read_input_lines

DAY01_PATH = PROJECT_ROOT / "2025" / "01" / "main.py"


class Day01Module(Protocol):
    def parse_input(self, lines: list[str]) -> object: ...

    def part1(self, rotations: object, start: int = 50) -> int: ...

    def part2(self, rotations: object, start: int = 50) -> int: ...


day01 = cast(Day01Module, load_module("aoc2025_day01", DAY01_PATH))


def test_sample_parts() -> None:
    lines = read_input_lines(2025, 1, variant="sample")
    rotations = day01.parse_input(lines)
    assert day01.part1(rotations) == 3
    assert day01.part2(rotations) == 6


def test_large_rotation_hits_zero_multiple_times() -> None:
    rotations = day01.parse_input(["R1000"])
    assert day01.part2(rotations, start=50) == 10
