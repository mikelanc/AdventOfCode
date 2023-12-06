"""AoC 03, 2023: Gear_Ratios."""

# Standard library imports
import pathlib
import sys
import pprint

point = complex
pp = pprint.PrettyPrinter(indent=4)

adj = [
    point(-1, -1),
    point(0, -1),
    point(1, -1),
    point(-1, 0),
    point(1, 0),
    point(-1, 1),
    point(0, 1),
    point(1, 1),
]


def getNum(grid: dict, position: point) -> tuple[complex, int]:
    """Return the position and number"""
    if position not in grid:
        return None
    while position - 1 in grid:
        position -= 1
    start = position
    num = grid[position]
    while position + 1 in grid:
        position += 1
        num += grid[position]
    return start, int(num)


def getAdjParts(grid: dict, symbols: dict) -> set:
    """Return adjacent points"""
    parts = set()
    for symbol in symbols:
        for direction in adj:
            parts.add(getNum(grid, symbol + direction))
    return parts - {None}


def getAdjParts2(grid: dict, symbols: dict) -> list:
    """Return adjacent points"""
    parts = []
    for symbol in symbols:
        symbolNumbers = set()
        for direction in adj:
            symbolNumbers.add(getNum(grid, symbol + direction))
        symbolNumbers = symbolNumbers - {None}
        if len(symbolNumbers) > 1:
            parts.append(symbolNumbers.pop()[1] * symbolNumbers.pop()[1])
    return parts


def part1(grid: dict, symbols: dict) -> int:
    """Solve part 1."""
    parts = getAdjParts(grid, symbols)
    sum = 0
    for part in parts:
        sum += part[1]
        print(part)
    return sum


def part2(grid: dict, symbols: dict) -> int:
    """Solve part 2."""
    # Filter dictionary by keeping elements whose values are string of length 6
    symbols = dict(filter(lambda elem: elem[1] == "*", symbols.items()))
    parts = getAdjParts2(grid, symbols)

    sum = 0
    for part in parts:
        sum += part
        print(part)
    return sum


def parse(puzzle_input: str) -> tuple[dict, dict]:
    """Parse input."""
    parsed = puzzle_input.splitlines()

    # create grid and symbols dicts
    grid = {}
    symbols = {}
    for y, line in enumerate(parsed):
        for x, content in enumerate(line):
            if not content.isnumeric():
                if content != ".":
                    symbols[point(x, y)] = content
            else:
                grid[point(x, y)] = content
    print("Grid")
    pp.pprint(grid)
    print("Symbols")
    pp.pprint(symbols)
    print("Parts")
    # parsed = getAdjParts(grid, symbols)
    return grid, symbols


def solve(puzzle_input: str) -> tuple[str, str]:
    """Solve the puzzle for the given input."""
    grid, symbols = parse(puzzle_input)
    solution1 = part1(grid, symbols)
    solution2 = part2(grid, symbols)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
