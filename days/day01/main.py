from __future__ import annotations

from dataclasses import dataclass

from libs.common import read_input_lines


@dataclass(frozen=True)
class Rotation:
    direction: str  # "L" or "R"
    steps: int


def parse_input(lines: list[str]) -> list[Rotation]:
    """Parse lines like `L68` into Rotation objects."""

    rotations: list[Rotation] = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        if direction not in {"L", "R"}:
            raise ValueError(f"Unexpected direction in line: {line}")
        steps = int(line[1:])
        rotations.append(Rotation(direction, steps))
    return rotations


def apply_rotation(position: int, rotation: Rotation) -> int:
    """Apply one rotation on a 0-99 dial returning the new position."""

    if rotation.direction == "L":
        return (position - rotation.steps) % 100
    return (position + rotation.steps) % 100


def part1(rotations: list[Rotation], start: int = 50) -> int:
    """Count how many times the dial lands on 0 after a rotation."""

    position = start
    zeros = 0
    for rotation in rotations:
        position = apply_rotation(position, rotation)
        if position == 0:
            zeros += 1
    return zeros


def part2(rotations: list[Rotation], start: int = 50) -> int:
    """Placeholder until Part Two unlocks; return Part One result for now."""

    return part1(rotations, start)


def run(variant: str | None = None) -> None:
    """Run day01 solution and print results."""

    lines = read_input_lines(1, variant)
    rotations = parse_input(lines)
    print(f"Part 1: {part1(rotations)}")
    print(f"Part 2: {part2(rotations)}")


if __name__ == "__main__":
    run()
