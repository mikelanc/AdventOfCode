"""AoC <DD>, <YYYY>: <Name>."""

# Standard library imports
import pathlib
import sys
import pprint


def parse(puzzle_input: str):
    """Parse input."""
    lines = puzzle_input.split("\n")
    # return puzzle_input.splitlines()
    return lines


def part1(data: list):
    """Solve part 1."""


def part2(data: list):
    """Solve part 2."""


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
