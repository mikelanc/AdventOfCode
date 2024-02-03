"""AoC 07, 2023: CamelCards."""

# Standard library imports
import pathlib
import sys
import pprint
import numpy as np

from collections import Counter
from enum import Enum


def convertCardsToNumbers(card: str) -> int:
    sortOrder = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    sortOrder.reverse()
    return sortOrder.index(card) + 2


# def sortHands(lines: list) -> list:
#    # numberOrder = {key: i for i, key in enumerate(sortOrder)}
#    sortedList = sorted(lines, key=lambda d: numberOrder[d[1]])
#    return sortedList


class HandType:
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


class Hand:
    def __init__(self, line):
        hand, bid = line.split()
        self.bid = int(bid)
        print("Hand" + str(hand))
        self.cards = tuple(convertCardsToNumbers(card) for card in hand)
        self.type = self.getType()
        print("Cards " + str(self.cards))
        print("Type " + str(self.type))

    def __repr__(self):
        return str(self.cards)

    def __lt__(self, comparisonHand):
        return self.type < comparisonHand.type or (
            self.type == comparisonHand.type and self.cards < comparisonHand.cards
        )
        # or (
        #    self.type == comparisonHand.type and self.cards < comparisonHand.cards
        # )

    def getType(self):
        counter = Counter(self.cards)
        print(counter)
        print("Length of counter" + str(len(counter)))
        print(counter.values())
        print("Higest count" + str(max(counter.values())))
        highest = max(counter.values())
        match highest:
            case 5:
                return HandType.FIVE_OF_A_KIND
            case 4:
                return HandType.FOUR_OF_A_KIND
            case 3:
                if len(counter) == 2:
                    return HandType.FULL_HOUSE
                else:
                    return HandType.THREE_OF_A_KIND
            case 2:
                if len(counter) == 3:
                    return HandType.TWO_PAIR
                else:
                    return HandType.ONE_PAIR
            case 1:
                return HandType.HIGH_CARD


def parse(puzzle_input: str) -> list:
    """Parse input."""
    # lines = puzzle_input.split("\n")
    hands = [Hand(l) for l in puzzle_input.splitlines()]
    print(type(hands))
    sorted(hands)
    print(hands)
    print(sorted(hands))
    # return sortHands(puzzle_input.splitlines())
    # print(lines)
    return sorted(hands)


def part1(data: list) -> int:
    """Solve part 1."""
    total = 0
    i = 1
    for hand in list:
        total += hand.bid * i
        i += 1

    # temp = [h.bid * 1 for h in enumerate(list)]
    return total


def part2(data: list) -> int:
    """Solve part 2."""
    p2 = 0
    return p2


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
