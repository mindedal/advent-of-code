import sys
from importlib import util
from pathlib import Path

from utils.io import read_input_lines

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DAY02_PATH = PROJECT_ROOT / "2025" / "02" / "main.py"


def load_day02_module():
    spec = util.spec_from_file_location("aoc2025_day02", DAY02_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {DAY02_PATH}")
    module = util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


day02 = load_day02_module()


def test_sample_input_sum():
    lines = read_input_lines(2025, 2, variant="sample")
    ranges = day02.parse_input(lines)
    assert day02.part1(ranges) == 1227775554
    assert day02.part2(ranges) == 4174379265


def test_two_digit_invalids_sum():
    ranges = day02.parse_input(["10-99"])
    # Invalid IDs are 11, 22, ..., 99 (nine numbers, each 11 * k for k=1..9)
    assert day02.part1(ranges) == 495
    # For part2, same set because no 3+ repeats fit in 2 digits
    assert day02.part2(ranges) == 495


def test_part2_counts_multi_repeats():
    ranges = day02.parse_input(["111-115,999-1005,1010-1010"])
    # part1 only sees two-repeats of same half; here that's 1010.
    assert day02.part1(ranges) == 1010
    # part2 should include 111 ("1" x3), 999 ("9" x3), and 1010 ("10" x2).
    assert day02.part2(ranges) == 111 + 999 + 1010
