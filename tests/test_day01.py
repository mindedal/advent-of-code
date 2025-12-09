from days.day01.main import parse_input, part1, part2
from libs.common import read_input_lines


def test_sample_parts():
    lines = read_input_lines(1, variant="sample")
    rotations = parse_input(lines)
    assert part1(rotations) == 3
    assert part2(rotations) == 6


def test_large_rotation_hits_zero_multiple_times():
    rotations = parse_input(["R1000"])
    assert part2(rotations, start=50) == 10
