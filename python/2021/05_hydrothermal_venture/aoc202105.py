"""AoC 5, 2021: Hydrothermal Venture."""

# Standard library imports
import pathlib
import sys
import collections


def parse_data(puzzle_input):
    """Parse input."""
    return [
        tuple(
            int(xy)
            for points in line.split(" -> ")
            for xy in points.split(",")
        )
        for line in puzzle_input.split("\n")
    ]


def points(line):
    """List all points making up a line.

    ## Examples:

    >>> points((0, 3, 3, 3))  # Horizontal line
    [(0, 3), (1, 3), (2, 3), (3, 3)]
    >>> points((3, 4, 3, 0))  # Vertical line
    [(3, 4), (3, 3), (3, 2), (3, 1), (3, 0)]
    """
    match line:
        case (x1, y1, x2, y2) if x1 == x2:
            return [(x1, y) for y in coords(y1, y2)]
        case (x1, y1, x2, y2) if y1 == y2:
            return [(x, y1) for x in coords(x1, x2)]

def coords(start, stop):
    """List coordinates between start and stop, inclusive."""
    step = 1 if start <= stop else -1
    return range(start, stop + step, step)

def count_overlaps(lines):
    """Count overlapping points between a list of lines.

    ## Example:

    >>> count_overlaps(
    ...     [(3, 3, 3, 5), (3, 3, 6, 3), (6, 6, 6, 3), (4, 5, 6, 5)]
    ... )
    3
    """
    overlaps = collections.Counter(
        point for line in lines for point in points(line)
    )
    return sum(num_points >= 2 for num_points in overlaps.values())

def part1(lines):
    """Solve part 1."""
    vertical = [(x1, y1, x2, y2) for x1, y1, x2, y2 in lines if x1 == x2]
    horizontal = [(x1, y1, x2, y2) for x1, y1, x2, y2 in lines if y1 == y2]
    return count_overlaps(vertical + horizontal)

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
