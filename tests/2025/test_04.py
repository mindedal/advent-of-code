import sys
from importlib import util
from pathlib import Path

from utils.io import read_input_lines

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DAY04_PATH = PROJECT_ROOT / "2025" / "04" / "main.py"


def load_day04_module():
    spec = util.spec_from_file_location("aoc2025_day04", DAY04_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {DAY04_PATH}")
    module = util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


day04 = load_day04_module()


def test_sample_accessible_rolls():
    lines = read_input_lines(2025, 4, variant="sample")
    grid = day04.parse_input(lines)
    assert day04.part1(grid) == 13
    assert day04.part2(grid) == 43


def test_edge_cells_count_neighbours_correctly():
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


def test_iterative_removal_clears_full_block():
    grid = day04.parse_input(
        [
            "@@@",
            "@@@",
            "@@@",
        ]
    )
    # Removals cascade until all 9 rolls are gone
    assert day04.part2(grid) == 9
