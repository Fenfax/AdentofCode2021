from typing import NamedTuple

from aoc_utils.profiler import profiler


class Cord(NamedTuple):
    x: int
    y: int


class Fold(NamedTuple):
    axes: str
    pos: int


def getInput(filename: str):
    cords = set(Cord(*map(int, x.replace("\n", "").split(","))) for x in open(filename) if "," in x)
    folds = [Fold(x.replace("fold along ", "").replace("\n", "").split("=")[0],
                  int(x.replace("fold along ", "").replace("\n", "").split("=")[1])) for x in
             open(filename) if "=" in x]

    return cords, folds


def printCords(cords: set[Cord]):
    max_x = max(cord.x for cord in cords)
    max_y = max(cord.y for cord in cords)
    area = ['  ' * (max_x + 1) for _ in range(max_y + 1)]
    for cord in cords:
        area[cord.y] = area[cord.y][:cord.x * 2] + "#" + area[cord.y][cord.x * 2 + 1:]
    for x in area:
        print(x)


@profiler
def part1(cords, folds):
    toFold: Fold = folds[0]
    newCords = set()
    for cord in cords:
        if toFold.axes == 'x':
            if cord.x >= toFold.pos:
                cord = Cord(toFold.pos - (cord.x - toFold.pos), cord.y)
            newCords.add(cord)
        else:
            if cord.y >= toFold.pos:
                cord = Cord(cord.x, toFold.pos - (cord.y - toFold.pos))
            newCords.add(cord)

    return len(newCords)


@profiler
def part2(cords, folds):
    newCords = cords
    for toFold in folds:
        cords = newCords
        newCords = set()
        for cord in cords:
            if toFold.axes == 'x':
                if cord.x >= toFold.pos:
                    cord = Cord(toFold.pos - (cord.x - toFold.pos), cord.y)
                newCords.add(cord)
            else:
                if cord.y >= toFold.pos:
                    cord = Cord(cord.x, toFold.pos - (cord.y - toFold.pos))
                newCords.add(cord)

    printCords(newCords)


print("Part1: ", part1(*getInput("input.txt")))
print("Part2:")
part2(*getInput("input.txt"))
print("--")
#https://www.reddit.com/r/adventofcode/comments/rfeuic/2021_day_13_part_25_what_if_it_would_be_more/
part2(*getInput("inputReddit.txt"))
