"""AoC 02, 2023: Cube_Conundrum."""

# Standard library imports
import pathlib
import sys
import pprint


def parse(puzzle_input):
    """Parse input."""
    games = puzzle_input.split("\n")
    listOfGames = []
    listOfGamesWithCubes = []
    for game in games:
        listOfShows = []
        shows = game.split(":")[1].split(";")
        cubesInGame = {}
        for show in shows:
            colourAndCounts = show.split(",")
            listOfCubesInShow = {}
            for colourAndCount in colourAndCounts:
                cube = colourAndCount.strip().split(" ")
                listOfCubesInShow[cube[1]] = int(cube[0])
                if cube[1] not in cubesInGame:
                    cubesInGame[cube[1]] = [int(cube[0])]
                else:
                    cubesInGame[cube[1]].append(int(cube[0]))
            listOfShows.append(listOfCubesInShow)
        listOfGames.append(listOfShows)
        listOfGamesWithCubes.append(cubesInGame)
    return listOfGames, listOfGamesWithCubes


def part1(data):
    """Solve part 1."""
    pprint.pprint(data)
    sum = 0
    for idx, game in enumerate(data):
        if (
            (max(game["red"]) <= 12)
            and (max(game["green"]) <= 13)
            and (max(game["blue"]) <= 14)
        ):
            print("good game" + str(idx + 1))
            sum += idx + 1
    return sum


def part2(data):
    """Solve part 2."""
    sum = 0
    for idx, game in enumerate(data):
        power = max(game["red"]) * max(game["green"]) * max(game["blue"])
        sum += power
    return sum


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data, data2 = parse(puzzle_input)
    solution1 = part1(data2)
    solution2 = part2(data2)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
