"""Tests for AoC 05, 2023: IfYouGiveASeedAFertilizer."""

import pathlib
import pytest
import aoc202305 as aoc

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


@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ...


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1[0], example1[1]) == 35


def test_part1_input(input):
    """Test part 1 on input."""
    assert aoc.part1(input[0], input[1]) == 318728750


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1[0], example1[1]) == 46


def test_part2_input(input):
    """Test part 2 on input."""
    assert aoc.part2(input[0], input[1]) == 37384986
