"""Tests for AoC 06, 2023: WaitForIt."""

import pathlib
import pytest
import aoc202306 as aoc

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
def inputb():
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc.parse2(puzzle_input)


@pytest.fixture
def example1b():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse2(puzzle_input)


@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ...


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 288


def test_part1_input(input):
    """Test part 1 on real input."""
    assert aoc.part1(input) == 170000


def test_part2_example1b(example1b):
    """Test part 2 on example input."""
    assert aoc.part2(example1b) == 71503


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...


def test_part2_inputb(inputb):
    """Test part 2 on real input."""
    assert aoc.part2(inputb) == 20537782
