from days.day01.main import parse_input, part1, part2
from libs.common import read_input_lines


def test_sample_parts():
    lines = read_input_lines(1, variant="sample")
    rotations = parse_input(lines)
    assert part1(rotations) == 3
    # Part 2 currently mirrors Part 1 until unlocked
    assert part2(rotations) == 3
