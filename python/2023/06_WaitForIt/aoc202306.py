"""AoC 06, 2023: WaitForIt."""

# Standard library imports
import pathlib
import sys
import pprint
import numpy as np


def parse(puzzle_input: str) -> list:
    """Parse input."""
    lines = puzzle_input.splitlines()
    # return puzzle_input.splitlines()
    lines = [line.split()[1:] for line in lines]
    for i, line in enumerate(lines):
        lines[i] = [int(entry) for entry in line]
    races = np.array(lines).T.tolist()
    # for i in range(len(lines[0])):
    #    races.append([lines[i][0], lines[i][1]])
    print(races)
    return races


def parse2(puzzle_input: str) -> list:
    """Parse input."""
    lines = puzzle_input.splitlines()
    print(lines)
    lines = [line.replace(" ", "") for line in lines]
    print(lines)
    lines = [int(line.split(":")[1]) for line in lines]
    print(lines)
    # return puzzle_input.splitlines()
    # lines = [line.split()[1:] for line in lines]
    # print(lines)
    # for i, line in enumerate(lines):
    #    lines[i] = [int(entry) for entry in line]
    # races = np.array(lines).T.tolist()
    # for i in range(len(lines[0])):
    #    races.append([lines[i][0], lines[i][1]])
    # print(races)
    return lines


def part1(data: list) -> int:
    """Solve part 1."""
    p1 = 1
    for race in data:
        count = 0
        length, record = race
        for guess in range(length + 1):
            distance = (length - guess) * guess
            if (distance) > record:
                count += 1

        # each race times together
        p1 *= count
    return p1


def part2(data: list) -> int:
    """Solve part 2."""
    count = 0
    length = int(data[0])
    record = int(data[1])
    for guess in range(length + 1):
        distance = (length - guess) * guess
        if (distance) > record:
            count += 1

    return count


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    data = parse2(puzzle_input)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
