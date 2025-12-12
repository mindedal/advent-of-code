import sys
from importlib import util
from pathlib import Path

from utils.io import read_input_lines

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DAY12_PATH = PROJECT_ROOT / "2025" / "12" / "main.py"


def load_day12_module():
    spec = util.spec_from_file_location("aoc2025_day12", DAY12_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {DAY12_PATH}")
    module = util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


day12 = load_day12_module()


def test_sample_part1_count_fit_regions():
    lines = read_input_lines(2025, 12, variant="sample")
    parsed = day12.parse_input(lines)
    assert day12.part1(parsed) == 2


def test_sample_third_region_is_impossible_exact():
    lines = read_input_lines(2025, 12, variant="sample")
    parsed = day12.parse_input(lines)

    # The sample input has 3 regions; the 3rd is explicitly stated as impossible.
    assert len(parsed.regions) == 3
    assert day12.can_fit_region(parsed.shapes, parsed.regions[0]) is True
    assert day12.can_fit_region(parsed.shapes, parsed.regions[1]) is True
    assert day12.can_fit_region(parsed.shapes, parsed.regions[2]) is False


def test_area_pruning_rejects_obvious_overflow():
    # Single 3x3 full shape in a 2x2 region cannot fit.
    parsed = day12.parse_input(
        [
            "0:",
            "###",
            "###",
            "###",
            "",
            "2x2: 1",
        ]
    )
    assert day12.part1(parsed) == 0
