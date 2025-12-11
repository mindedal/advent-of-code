import sys
from importlib import util
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DAY06_PATH = PROJECT_ROOT / "2025" / "06" / "main.py"


def load_day06_module():
    spec = util.spec_from_file_location("aoc2025_day06", DAY06_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {DAY06_PATH}")
    module = util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


day06 = load_day06_module()


def _build_worksheet(problems):
    """Construct worksheet rows from structured data for testing."""

    operand_count = len(problems[0][0])
    if any(len(ops) != operand_count for ops, _ in problems):
        raise ValueError("All problems must have the same number of operands")

    rows = ["" for _ in range(operand_count + 1)]
    for idx, (operands, op) in enumerate(problems):
        width = max(len(str(n)) for n in operands)
        for r, value in enumerate(operands):
            rows[r] += str(value).rjust(width)
        rows[-1] += op.rjust(width)

        if idx != len(problems) - 1:
            for r in range(len(rows)):
                rows[r] += " "

    return rows


def test_sample_grand_total_matches_description():
    worksheet = [
        "123 328  51 64 ",
        " 45 64  387 23 ",
        "  6 98  215 314",
        "*   +   *   +  ",
    ]

    problems = day06.parse_input(worksheet)
    assert len(problems) == 4
    assert day06.part1(problems) == 4_277_556
    assert day06.part2(worksheet) == 3_263_827


def test_parser_handles_extra_spacing_between_problems():
    lines = [
        " 7    81  ",
        "33    2   ",
        " 5    19  ",
        " *    +   ",
    ]
    problems = day06.parse_input(lines)
    assert [p.numbers for p in problems] == [[7, 33, 5], [81, 2, 19]]
    assert [p.op for p in problems] == ["*", "+"]
    assert day06.part1(problems) == (7 * 33 * 5) + (81 + 2 + 19)


def test_column_parsing_reads_right_to_left():
    lines = [
        "12 78",
        "34 56",
        " *  +",
    ]

    problems = day06.parse_input_columns(lines)
    # Columns per problem: rightmost problem first (columns read right-to-left)
    assert [p.numbers for p in problems] == [[86, 75], [24, 13]]
    assert [p.op for p in problems] == ["+", "*"]
    assert day06.part2(lines) == (86 + 75) + (24 * 13)
