"""Tests for AoC 04, 2023: Scratchcards."""

import pathlib
import pytest
import aoc202304 as aoc

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


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 13


def test_part1_input(input):
    """Test part 1 on real input."""
    assert aoc.part1(input) == 26346


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 30


def test_part2_input(input):
    """Test part 2 on example input."""
    assert aoc.part2(input) == 8467762
