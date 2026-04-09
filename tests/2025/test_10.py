from __future__ import annotations

from typing import Protocol, cast

from tests._helpers import PROJECT_ROOT, load_module
from utils.io import read_input_lines

DAY10_PATH = PROJECT_ROOT / "2025" / "10" / "main.py"


class Day10Module(Protocol):
    def parse_input(self, lines: list[str]) -> object: ...

    def part1(self, machines: object) -> int: ...

    def part2(self, machines: object) -> int: ...


day10 = cast(Day10Module, load_module("aoc2025_day10", DAY10_PATH))


def test_sample_parts() -> None:
    lines = read_input_lines(2025, 10, variant="sample")
    machines = day10.parse_input(lines)
    assert day10.part1(machines) == 7
    assert day10.part2(machines) == 33


def test_single_button_machine() -> None:
    machines = day10.parse_input(["[#] (0) {5}"])
    assert day10.part1(machines) == 1


def test_combo_button_shortcut() -> None:
    machines = day10.parse_input(["[##] (0) (1) (0,1) {1,1}"])
    assert day10.part1(machines) == 1
