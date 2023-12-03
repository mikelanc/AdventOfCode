"""AoC 03, 2023: Gear_Ratios."""

# Standard library imports
import pathlib
import sys
import pprint
import complex


def parse(puzzle_input):
    """Parse input."""
    parsed = puzzle_input.splitlines()
    point = complex

    # create grid
    grid = {}  # dict
    for y, line in enumerate(parsed):
        for x, content in enumerate(line):
            grid[point(x, y)] = content
    pprint.pprint(grid)

    return parsed


def part1(data):
    """Solve part 1."""


def part2(data):
    """Solve part 2."""


def solve(puzzle_input):
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
