import sys
from importlib import util
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DAY09_PATH = PROJECT_ROOT / "2025" / "09" / "main.py"


def load_day09_module():
    spec = util.spec_from_file_location("aoc2025_day09", DAY09_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {DAY09_PATH}")
    module = util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


day09 = load_day09_module()


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


def test_sample_max_area_two_corners():
    points = day09.parse_input(SAMPLE_INPUT)
    assert day09.part1(points) == 50


def test_sample_green_limited_area():
    points = day09.parse_input(SAMPLE_INPUT)
    assert day09.part2(points) == 24


def test_concave_shape_blocks_outside_rectangles():
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
