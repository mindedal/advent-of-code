import sys
from importlib import util
from pathlib import Path

from utils.io import read_input_lines

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DAY03_PATH = PROJECT_ROOT / "2025" / "03" / "main.py"


def load_day03_module():
    spec = util.spec_from_file_location("aoc2025_day03", DAY03_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {DAY03_PATH}")
    module = util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


day03 = load_day03_module()


def test_sample_total_joltage():
    lines = read_input_lines(2025, 3, variant="sample")
    banks = day03.parse_input(lines)
    assert day03.part1(banks) == 357
    assert day03.part2(banks) == 3121910778619


def test_bank_maximum_in_order():
    assert day03.max_bank_joltage("12345") == 45
    assert day03.max_bank_joltage("818181911112111") == 92
    assert day03.max_bank_joltage("21") == 21


def test_max_k_digits_helper_general():
    helper = day03._max_joltage_k_digits
    # pick 12 digits from descending then ones
    assert helper("987654321111111", 12) == 987654321111
    # ensure drops trim from end when no better digit appears
    assert helper("111234", 3) == 234
    # ensure greedy keeps order across ups and downs
    assert helper("818181911112111", 12) == 888911112111
