from __future__ import annotations

from collections import deque

from utils.io import read_input_lines

YEAR = 2025
DAY = 4

# A roll of paper is represented by "@"; empty space by ".".
# A roll is accessible if fewer than four of its eight neighbours are also rolls.


def parse_input(lines: list[str]) -> list[str]:
    """Return the trimmed, non-empty grid rows.

    Preserves row order and assumes all meaningful characters are `@` or `.`.
    Empty or whitespace-only lines are ignored.
    """

    rows = [line.strip() for line in lines if line.strip()]
    if not rows:
        return []

    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise ValueError("All rows must be the same length")

    return rows


def _adjacent_ats(grid: list[str], r: int, c: int) -> int:
    """Count `@` neighbours in the 8 surrounding cells of (r, c)."""

    h = len(grid)
    w = len(grid[0]) if h else 0
    total = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == "@":
                total += 1
    return total


def part1(grid: list[str]) -> int:
    """Return the count of rolls accessible by a forklift.

    A roll is accessible if it has < 4 neighbouring rolls among the 8
    adjacent positions.
    """

    if not grid:
        return 0

    h = len(grid)
    w = len(grid[0])
    accessible = 0

    for r in range(h):
        for c in range(w):
            if grid[r][c] != "@":
                continue
            if _adjacent_ats(grid, r, c) < 4:
                accessible += 1
    return accessible


def part2(grid: list[str]) -> int:
    """Return total rolls removable via repeated accessibility.

    Iteratively remove any roll with < 4 neighbouring rolls; each removal can
    unlock more accessible rolls. Uses a neighbour-count queue to avoid
    rescanning the whole grid each round.
    """

    if not grid:
        return 0

    h = len(grid)
    w = len(grid[0])
    chars = [list(row) for row in grid]

    counts = [[0] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if chars[r][c] != "@":
                continue
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < h and 0 <= nc < w and chars[nr][nc] == "@":
                        counts[r][c] += 1

    queue: deque[tuple[int, int]] = deque()
    for r in range(h):
        for c in range(w):
            if chars[r][c] == "@" and counts[r][c] < 4:
                queue.append((r, c))

    removed = 0
    while queue:
        r, c = queue.popleft()
        if chars[r][c] != "@":
            continue  # already removed earlier
        if counts[r][c] >= 4:
            continue  # no longer accessible after prior updates

        chars[r][c] = "."
        removed += 1

        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w and chars[nr][nc] == "@":
                    counts[nr][nc] -= 1
                    if counts[nr][nc] < 4:
                        queue.append((nr, nc))

    return removed


def run(variant: str | None = None) -> None:
    """Run day04 solution and print results."""

    lines = read_input_lines(YEAR, DAY, variant)
    grid = parse_input(lines)
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")


if __name__ == "__main__":
    run()
