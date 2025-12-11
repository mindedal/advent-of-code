import sys
from importlib import util
from pathlib import Path

from utils.io import read_input_lines

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DAY05_PATH = PROJECT_ROOT / "2025" / "05" / "main.py"


def load_day05_module():
    spec = util.spec_from_file_location("aoc2025_day05", DAY05_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {DAY05_PATH}")
    module = util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


day05 = load_day05_module()


def test_sample_fresh_and_spoiled_counts():
    lines = read_input_lines(2025, 5, variant="sample")
    ranges, ids = day05.parse_input(lines)
    assert day05.part1(ranges, ids) == 3
    assert day05.part2(ranges) == 14


def test_overlapping_ranges_merge_and_count():
    ranges = [
        day05.IdRange(1, 3),
        day05.IdRange(5, 7),
        day05.IdRange(3, 5),
    ]
    ids = [1, 3, 4, 5, 7, 8]
    assert day05.part1(ranges, ids) == 5
    assert day05.part2(ranges) == 7


def test_empty_ranges_or_ids_handle():
    assert day05.part1([], [1, 2, 3]) == 0
    assert day05.part2([]) == 0
    assert day05.part1([day05.IdRange(10, 20)], []) == 0
