"""Tests for AoC 07, 2023: CamelCards."""

import pathlib
import pytest
import aoc202307 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def input():
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_checkCardConversion():
    assert aoc.convertCardsToNumbers("Q") == 12
    assert aoc.convertCardsToNumbers("3") == 3


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    # assert example1 == ["32T3K 765", "KTJJT 220", "KK677 28", "T55J5 684", "QQQJA 483"]
    assert example1 == [
        (3, 2, 10, 3, 13),
        (13, 10, 11, 11, 10),
        (13, 13, 6, 7, 7),
        (10, 5, 5, 11, 5),
        (12, 12, 12, 11, 14),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 6440


@pytest.mark.skip(reason="Not implemented")
def test_part1_input(input):
    """Test part 1 on real input."""
    assert aoc.part1(input) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...
