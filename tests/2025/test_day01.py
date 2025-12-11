import sys
from importlib import util
from pathlib import Path

from utils.io import read_input_lines

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DAY01_PATH = PROJECT_ROOT / "2025" / "01" / "main.py"


def load_day01_module():
    spec = util.spec_from_file_location("aoc2025_day01", DAY01_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {DAY01_PATH}")
    module = util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


day01 = load_day01_module()


def test_sample_parts():
    lines = read_input_lines(2025, 1, variant="sample")
    rotations = day01.parse_input(lines)
    assert day01.part1(rotations) == 3
    assert day01.part2(rotations) == 6


def test_large_rotation_hits_zero_multiple_times():
    rotations = day01.parse_input(["R1000"])
    assert day01.part2(rotations, start=50) == 10
