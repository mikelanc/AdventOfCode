"""AoC 5, 2020: Binary Boarding."""

# Standard library imports
import pathlib
import sys
from typing import Tuple


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.split("\n")


def how_much_to_add(row: int, seed: int, letter: str) -> Tuple[int, int]:
    if letter == "B":
        return row + seed, seed / 2
    else:
        return row, seed / 2


def part1(data):
    """Solve part 1."""
    seeds = [64, 32, 16, 8, 4, 2, 1, 4, 2, 1]
    seatids = []
    ticketcounter = 0
    for ticket in data:
        row = 0
        seat = 0
        counter = 0
        for letter in ticket[:7]:
            if letter == "B":
                row += seeds[counter]
            counter += 1
        for letter in ticket[7:]:
            if letter == "R":
                seat += seeds[counter]
            counter += 1
        seatid = row * 8 + seat
        seatids.append(seatid)
        ticketcounter += 1

    return max(seatids)


def part2(data):
    """Solve part 2."""


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
