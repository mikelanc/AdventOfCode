"""AoC 1, 2019: The Tyranny of the Rocket Equation."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [int(line) for line in puzzle_input.split("\n")]


def part1(module_masses):
    """Solve part 1."""
    return sum(mass // 3 - 2 for mass in module_masses)


def all_fuel(mass):
    """Calculate fuel while taking mass of the fuel into account.

    ## Example:

    >>> all_fuel(1969)
    966
    """
    #fuel = mass // 3 - 2
    #if fuel <= 0:
    #   return 0
    #else:
    #    return fuel + all_fuel(mass=fuel)
    return 0 if (fuel := mass // 3 - 2) < 0 else fuel + all_fuel(fuel)

def part2(module_masses):
    """Solve part 2."""
    return sum(all_fuel(mass) for mass in module_masses)


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
