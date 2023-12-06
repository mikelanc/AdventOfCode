"""AoC 04, 2023: Scratchcards."""

# Standard library imports
import pathlib
import sys
import pprint


def parse(puzzle_input: str) -> list:
    """Parse input."""
    lines = puzzle_input.splitlines()
    array = []
    for i, line in enumerate(lines):
        splitline = line.split(":")[1].split(" | ")
        innerarray = []
        for part in [0, 1]:
            innerarray.append(splitline[part].strip().split())
        array.append(innerarray)
    return array


def getScore(count: int) -> int:
    score = 0
    # scoring model just follows this pattern - see desmos.com/calculator
    score = 2 ** (count - 1)
    # int rounds to whole numbers which avoid the problem with zero
    score = int(score)

    print("score" + str(score))
    return score


def part1(data: list) -> int:
    """Solve part 1."""
    print("Part 1")
    sum = 0
    for i, line in enumerate(data):
        print("Line " + str(i + 1))
        sum = sum + getScore(getCount(line))
    return sum


def getCount(line: list) -> int:
    a = set(line[0])
    b = set(line[1])
    c = a & b
    # print(a)
    # print(b)
    # print(c)
    return len(c)


def part2(data: list):
    """Solve part 2."""
    print("Part 2")
    # countOfCards = []
    # for _ in range(len(data)):
    #    countOfCards.append(1)
    # smarter way to create the array of 1s
    countOfCards = [1] * len(data)

    # attempt1 takes 10 seconds
    # for i, line in enumerate(data):
    #   for _ in range(countOfCards[i]):
    #       for linenum in range(getCount(line)):
    #           countOfCards[i + linenum + 1] = countOfCards[i + linenum + 1] + 1
    #           # print(                    "linenum " + str(i) + " adding 1 to linenum " + str(i + linenum + 1)                )

    # attempt 2 takes less than a tenth of a second!
    for i, line in enumerate(data):
        # for _ in range(countOfCards[i]):
        for linenum in range(getCount(line)):
            countOfCards[i + linenum + 1] += countOfCards[i]
            # print(                    "linenum " + str(i) + " adding 1 to linenum " + str(i + linenum + 1)                )
    return sum(countOfCards)


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
