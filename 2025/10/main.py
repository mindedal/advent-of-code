from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable

try:  # z3 is required for part 2
    import z3  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover - make requirement explicit
    raise ImportError("z3-solver is required for Day 10 part 2. Install with `uv add z3-solver`.")

from utils.io import read_input_lines

YEAR = 2025
DAY = 10
INF = 10**18


@dataclass(frozen=True)
class Machine:
    lights_mask: int
    button_masks: list[int]
    button_indices: list[list[int]]
    joltage_targets: list[int]


def _diagram_to_mask(diagram: str) -> int:
    mask = 0
    for i, ch in enumerate(diagram):
        if ch == "#":
            mask |= 1 << i
        elif ch != ".":
            raise ValueError(f"Unexpected indicator character: {ch!r}")
    return mask


def _button_to_mask_and_indices(indices: str) -> tuple[int, list[int]]:
    mask = 0
    idxs: list[int] = []
    for part in indices.split(","):
        part = part.strip()
        if not part:
            continue
        idx = int(part)
        if idx < 0:
            raise ValueError("Indicator index cannot be negative")
        mask ^= 1 << idx
        idxs.append(idx)
    return mask, idxs


def _parse_targets(line: str) -> list[int]:
    target_match = re.search(r"\{([^}]*)\}", line)
    if not target_match:
        return []
    return [int(x.strip()) for x in target_match.group(1).split(",") if x.strip()]


def parse_input(lines: Iterable[str]) -> list[Machine]:
    """Parse machines from the raw input lines.

    Each line contains an indicator diagram in ``[]``, one or more button
    definitions in ``()``, and joltage targets in ``{}``.
    """

    machines: list[Machine] = []
    for raw in lines:
        line = raw.strip()
        if not line:
            continue

        diagram_match = re.search(r"\[([^\]]+)\]", line)
        if not diagram_match:
            raise ValueError(f"Missing indicator diagram in line: {line}")
        diagram = diagram_match.group(1)
        target_mask = _diagram_to_mask(diagram)

        button_strs = re.findall(r"\(([^)]*)\)", line)
        if not button_strs:
            raise ValueError(f"No buttons found in line: {line}")

        button_masks: list[int] = []
        button_indices: list[list[int]] = []
        for b in button_strs:
            mask, idxs = _button_to_mask_and_indices(b)
            button_masks.append(mask)
            button_indices.append(idxs)

        targets = _parse_targets(line)
        machines.append(Machine(target_mask, button_masks, button_indices, targets))

    return machines


def _min_presses(target_mask: int, buttons: list[int]) -> int:
    """Return the minimum number of button presses to reach ``target_mask``.

    Uses a subset-DP over the button list. Each button is either pressed or not
    pressed because pressing the same button twice cancels out over GF(2).
    """

    n = len(buttons)
    if target_mask == 0:
        return 0
    if n == 0:
        raise ValueError("No buttons available to toggle lights")

    states = [0] * (1 << n)
    best = float("inf")

    for mask in range(1, 1 << n):
        lsb = mask & -mask
        idx = lsb.bit_length() - 1
        states[mask] = states[mask ^ lsb] ^ buttons[idx]

    for mask, state in enumerate(states):
        if state == target_mask:
            presses = mask.bit_count()
            if presses < best:
                best = presses

    if best == float("inf"):
        raise ValueError("Target configuration is unreachable with given buttons")
    return int(best)


def _compress_vectors(vectors: list[list[int]]) -> list[tuple[int, ...]]:
    """Remove duplicate button vectors; order by descending coverage size."""

    unique: dict[tuple[int, ...], None] = {}
    for vec in vectors:
        t = tuple(vec)
        unique[t] = None
    return sorted(unique.keys(), key=lambda v: sum(v), reverse=True)


def _min_presses_counters(targets: list[int], buttons: list[list[int]]) -> int:
    """Return minimal presses to reach exact joltage targets via ILP (z3)."""

    if not targets:
        return 0

    m = len(targets)

    vectors = []
    for idxs in buttons:
        vec = [0] * m
        for idx in idxs:
            if idx >= m:
                raise ValueError("Button index exceeds number of counters")
            vec[idx] = 1
        if any(vec):
            vectors.append(vec)

    if not vectors:
        raise ValueError("No buttons affect any counters")

    solver = z3.Optimize()
    vars_ = [z3.Int(f"x{j}") for j in range(len(vectors))]
    for v in vars_:
        solver.add(v >= 0)

    for i in range(m):
        contrib = [vars_[j] for j, vec in enumerate(vectors) if vec[i]]
        if not contrib and targets[i] != 0:
            return INF
        solver.add(z3.Sum(contrib) == targets[i])

    solver.minimize(z3.Sum(vars_))
    if solver.check() != z3.sat:
        return INF
    model = solver.model()
    total = 0
    for v in vars_:
        val = model.eval(v, model_completion=True)
        total += int(val.as_long())  # type: ignore[attr-defined]
    return total


def part1(machines: list[Machine]) -> int:
    """Sum the fewest button presses required for every machine."""

    return sum(_min_presses(machine.lights_mask, machine.button_masks) for machine in machines)


def part2(machines: list[Machine]) -> int:
    """Fewest presses to satisfy all joltage requirements."""

    return sum(_min_presses_counters(m.joltage_targets, m.button_indices) for m in machines)


def run(variant: str | None = None) -> None:
    lines = read_input_lines(YEAR, DAY, variant)
    machines = parse_input(lines)
    print(f"Part 1: {part1(machines)}")
    print(f"Part 2: {part2(machines)}")


if __name__ == "__main__":
    run()
