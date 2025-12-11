import sys
from importlib import util
from pathlib import Path

import pytest
from utils.io import read_input_lines

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DAY11_PATH = PROJECT_ROOT / "2025" / "11" / "main.py"


def load_day11_module():
    spec = util.spec_from_file_location("aoc2025_day11", DAY11_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {DAY11_PATH}")
    module = util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


day11 = load_day11_module()


def test_sample_paths_part1():
    lines = read_input_lines(2025, 11, variant="sample")
    graph = day11.parse_input(lines)
    assert day11.part1(graph) == 5


def test_sample_paths_part2_required_nodes():
    lines = read_input_lines(2025, 11, variant="sample2")
    graph = day11.parse_input(lines)
    assert day11.part2(graph) == 2


def test_unreachable_output():
    graph = day11.parse_input(
        [
            "you: a",
            "a: b",
            "b: c",
            "c: d",
        ]
    )
    assert day11.part1(graph) == 0
    # Start is "svr" by default for part2; unreachable graph should yield 0.
    assert day11.part2(graph) == 0


def test_cycle_detection():
    graph = day11.parse_input(
        [
            "you: a dac",
            "a: you fft",
            "dac: out",
            "fft: out",
            "out:",
        ]
    )
    with pytest.raises(ValueError):
        day11.part1(graph)
    with pytest.raises(ValueError):
        day11.part2(graph, start="you")
