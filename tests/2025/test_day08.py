import sys
from importlib import util
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DAY08_PATH = PROJECT_ROOT / "2025" / "08" / "main.py"


def load_day08_module():
    spec = util.spec_from_file_location("aoc2025_day08", DAY08_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {DAY08_PATH}")
    module = util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


day08 = load_day08_module()


EXAMPLE_INPUT = [
    "162,817,812",
    "57,618,57",
    "906,360,560",
    "592,479,940",
    "352,342,300",
    "466,668,158",
    "542,29,236",
    "431,825,988",
    "739,650,466",
    "52,470,668",
    "216,146,977",
    "819,987,18",
    "117,168,530",
    "805,96,715",
    "346,949,466",
    "970,615,88",
    "941,993,340",
    "862,61,35",
    "984,92,344",
    "425,690,689",
]


def test_example_matches_described_product():
    points = day08.parse_input(EXAMPLE_INPUT)
    assert len(points) == 20
    assert day08.part1(points, pairs_to_connect=10) == 40
    assert day08.part2(points) == 25_272


def test_last_connection_product_simple_triangle():
    points = [
        (0, 0, 0),
        (10, 0, 0),
        (0, 10, 0),
    ]

    # Closest edges are (0,1) and (0,2) both with distance 10; the second of those
    # completes connectivity, producing product 0 * 0 = 0.
    assert day08.part2(points) == 0
