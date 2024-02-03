"""AoC 05, 2023: IfYouGiveASeedAFertilizer."""

# Standard library imports
import pathlib
import sys
import pprint


class Range:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def __repr__(self):
        return f"[{self.lower}, {self.upper})"

    def intersection(self, other):
        tmp = Range(max(self.lower, other.lower), min(self.upper, other.upper))
        return tmp if tmp.lower < tmp.upper else None

    def subtract(self, other):
        ins = self.intersection(other)
        if ins == None:
            # ----------
            #    			---
            return [Range(self.lower, self.upper)]
        elif (ins.lower, ins.upper) == (self.lower, self.upper):
            #    -----		intersect
            #    -----		self
            return []
        elif ins.lower == self.lower:
            #    --			intersect
            #    -----		self
            return [Range(ins.upper, self.upper)]
        elif ins.upper == self.upper:
            #       --		intersect
            #    -----		self
            return [Range(self.lower, ins.lower)]
        else:
            #      --		intersect
            #    ------		self
            return [Range(self.lower, ins.lower), Range(ins.upper, self.upper)]

    def add(self, offset):
        return Range(self.lower + offset, self.upper + offset)


class Map:
    def __init__(self, map_str):
        self.rules = []
        for line in map_str.splitlines()[1:]:
            dest, source, size = map(int, line.split())
            self.rules.append((dest, source, size))

    def convert(self, input: int):
        for dest, source, size in self.rules:
            if source <= input < source + size:
                return dest + input - source
        return input


def getLocation(seed, maps):
    for map in maps:
        seed = map.convert(seed)
    return seed


def parse(puzzle_input: str) -> tuple[list, list]:
    """Parse input."""
    seeds, *map_strs = puzzle_input.split("\n\n")
    # return puzzle_input.splitlines()
    # print(list(seeds))
    seeds = list(map(int, seeds.split()[1:]))
    maps = [Map(map_str) for map_str in map_strs]

    return seeds, maps


def part1(seeds: list, maps: list) -> int:
    """Solve part 1."""

    locations = [getLocation(seed, maps) for seed in seeds]
    p1 = min(locations)
    print(locations)
    print(p1)
    print(type(p1))
    return p1


def part2(seeds: list, maps: list) -> int:
    """Solve part 2."""
    p2 = p2solver(maps)
    for i in range(0, len(seeds), 2):
        p2.propagate(Range(seeds[i], seeds[i] + seeds[i + 1]), 0)
    return p2.answer


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input."""
    seeds, maps = parse(puzzle_input)
    solution1 = part1(seeds, maps)
    solution2 = part2(seeds, maps)

    return solution1, solution2


class p2solver:
    def __init__(self, maps):
        self.maps = maps
        self.answer = float("inf")

    def propagate(self, r: Range, layer: int):
        if layer == len(self.maps):
            self.answer = min(self.answer, r.lower)
            return
        for dest, source, size in self.maps[layer].rules:
            map_r = Range(source, source + size)
            ins = r.intersection(map_r)
            if ins is not None:
                self.propagate(ins.add(dest - source), layer + 1)
                sub = r.subtract(map_r)
                if len(sub) == 0:
                    return
                r = sub[0]
                if len(sub) == 2:
                    self.propagate(sub[1], layer)
        self.propagate(r, layer + 1)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
