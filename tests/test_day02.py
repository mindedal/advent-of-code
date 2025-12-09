from days.day02.main import parse_input, part1, part2
from libs.common import read_input_lines


def test_sample_input_sum():
    lines = read_input_lines(2, variant="sample")
    ranges = parse_input(lines)
    assert part1(ranges) == 1227775554
    assert part2(ranges) == 4174379265


def test_two_digit_invalids_sum():
    ranges = parse_input(["10-99"])
    # Invalid IDs are 11, 22, ..., 99 (nine numbers, each 11 * k for k=1..9)
    assert part1(ranges) == 495
    # For part2, same set because no 3+ repeats fit in 2 digits
    assert part2(ranges) == 495


def test_part2_counts_multi_repeats():
    ranges = parse_input(["111-115,999-1005,1010-1010"])
    # part1 only sees two-repeats of same half; here that's 1010.
    assert part1(ranges) == 1010
    # part2 should include 111 ("1" x3), 999 ("9" x3), and 1010 ("10" x2).
    assert part2(ranges) == 111 + 999 + 1010
