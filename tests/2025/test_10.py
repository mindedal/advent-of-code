import sys
from importlib import util
from pathlib import Path

from utils.io import read_input_lines

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DAY10_PATH = PROJECT_ROOT / "2025" / "10" / "main.py"


def load_day10_module():
    spec = util.spec_from_file_location("aoc2025_day10", DAY10_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {DAY10_PATH}")
    module = util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


day10 = load_day10_module()


def test_sample_parts():
    lines = read_input_lines(2025, 10, variant="sample")
    machines = day10.parse_input(lines)
    assert day10.part1(machines) == 7
    assert day10.part2(machines) == 33


def test_single_button_machine():
    machines = day10.parse_input(["[#] (0) {5}"])
    assert day10.part1(machines) == 1


def test_combo_button_shortcut():
    machines = day10.parse_input(["[##] (0) (1) (0,1) {1,1}"])
    assert day10.part1(machines) == 1
