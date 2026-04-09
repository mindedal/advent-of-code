from __future__ import annotations

from typing import Protocol, cast

from tests._helpers import PROJECT_ROOT, load_module

DAY09_PATH = PROJECT_ROOT / "2025" / "09" / "main.py"


Point2D = tuple[int, int]


class Day09Module(Protocol):
    def parse_input(self, lines: list[str]) -> list[Point2D]: ...

    def part1(self, points: list[Point2D]) -> int: ...

    def part2(self, points: list[Point2D]) -> int: ...


day09 = cast(Day09Module, load_module("aoc2025_day09", DAY09_PATH))


SAMPLE_INPUT = [
    "7,1",
    "11,1",
    "11,7",
    "9,7",
    "9,5",
    "2,5",
    "2,3",
    "7,3",
]


def test_sample_max_area_two_corners() -> None:
    points = day09.parse_input(SAMPLE_INPUT)
    assert day09.part1(points) == 50


def test_sample_green_limited_area() -> None:
    points = day09.parse_input(SAMPLE_INPUT)
    assert day09.part2(points) == 24


def test_concave_shape_blocks_outside_rectangles() -> None:
    concave = [
        (0, 0),
        (4, 0),
        (4, 2),
        (2, 2),
        (2, 4),
        (0, 4),
    ]
    # Unrestricted rectangle would span the full 5x5 box.
    assert day09.part1(concave) == 25
    # Green-limited rectangle cannot cover the missing quadrant; expect smaller area.
    assert day09.part2(concave) < 25
