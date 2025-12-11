import sys
from importlib import util
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DAY07_PATH = PROJECT_ROOT / "2025" / "07" / "main.py"
SAMPLE_PATH = PROJECT_ROOT / "inputs" / "2025" / "07.sample.txt"


def load_day07_module():
    spec = util.spec_from_file_location("aoc2025_day07", DAY07_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {DAY07_PATH}")
    module = util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


day07 = load_day07_module()


def test_sample_splits_match_description():
    lines = SAMPLE_PATH.read_text(encoding="utf-8").splitlines()
    assert day07.part1(lines) == 21
    assert day07.part2(lines) == 40


def test_chain_reaction_with_adjacent_splitters():
    diagram = [
        "..S..",
        "..^..",
        ".^^^.",
        ".....",
    ]

    # First splitter creates two beams; the next row contains three splitters
    # that split the two incoming beams into three total beams.
    assert day07.part1(diagram) == 3
    # Quantum version keeps both timelines even when paths converge at the
    # middle column on the following row.
    assert day07.part2(diagram) == 4


def test_timelines_preserved_on_merge():
    diagram = [
        ".S.",
        ".^.",
        "^.^",
        "...",
    ]

    # Beams from the first splitter hit two splitters that both send beams
    # into the center column; quantum timelines add rather than merge.
    assert day07.part1(diagram) == 3
    assert day07.part2(diagram) == 2
