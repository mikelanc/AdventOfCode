"""AoC 5, 2020: Binary Boarding."""

# Standard library imports
import pathlib
import sys
from typing import Tuple
import re

def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.split("\n")


def string_to_seat_original(ticket: str) -> int:
    row = 0
    seat = 0
    seeds = [64, 32, 16, 8, 4, 2, 1, 4, 2, 1]
    counter = 0
    for letter in ticket[:7]:
        if letter == "B":
            row += seeds[counter]
        counter += 1
    for letter in ticket[7:]:
        if letter == "R":
            seat += seeds[counter]
        counter += 1
    return row * 8 + seat

def string_to_seat(ticket: str) -> int:
    return binary_to_dec(string_to_binary(ticket))

def string_to_binary(ticket: str) -> str:
    mapping = str.maketrans({"F": "0", "L": "0", "B": "1", "R": "1"})
    return ticket.translate(mapping)

def binary_to_dec(binarystr: str) -> int:
    return int(binarystr, base=2)

def part1(data):
    """Solve part 1."""
    seatids = []
    for ticket in data:
        seatids.append(string_to_seat(ticket=ticket))

    return seatids, max(seatids)


def part2(data):
    """Solve part 2."""
    seatids = []
    for ticket in data:
        seatids.append(string_to_seat(ticket=ticket))
    next = int(sorted(seatids)[0]) + 1
    for i in sorted(seatids)[1:]:
        if i != next:
            return next
        next += 1 

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)[1]
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
