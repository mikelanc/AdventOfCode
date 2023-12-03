"""AoC 01, 2023: Trebuchet?!."""

# Standard library imports
import pathlib
import sys
import re


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.split("\n")


def part1(data):
    """Solve part 1."""
    count = 0
    for line in data:
        first = re.search("\d", line)
        last = re.search("\d", line[::-1])
        count += int(first.group() + last.group())
    return count


def part2(data):
    """Solve part 2."""
    count = 0
    for line in data:
        first = re.search("\d|one|two|three|four|five|six|seven|eight|nine", line)
        last = re.search("\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin", line[::-1])
        print(line)
        print(first.group())
        print(last.group())
        if len(first.group()) == 1:
            first = first.group()
        else:
            match first.group():
                case "one":
                    first = "1"
                case "two":
                    first = "2"
                case "three":
                    first = "3"
                case "four":
                    first = "4"
                case "five":
                    first = "5"
                case "six":
                    first = "6"
                case "seven":
                    first = "7"
                case "eight":
                    first = "8"
                case "nine":
                    first = "9"
        if len(last.group()) == 1:
            last = last.group()
        else:
            match last.group():
                case "eno":
                    last = "1"
                case "owt":
                    last = "2"
                case "eerht":
                    last = "3"
                case "ruof":
                    last = "4"
                case "evif":
                    last = "5"
                case "xis":
                    last = "6"
                case "neves":
                    last = "7"
                case "thgie":
                    last = "8"
                case "enin":
                    last = "9"
        count += int(first + last)

    return count


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
