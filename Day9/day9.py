from typing import NamedTuple

import math


class Point(NamedTuple):
    x: int
    y: int


def getInput():
    return [[int(y) for y in x.replace("\n", "")] for x in open("input.txt")]


def part1(inp: [[int]]):
    lowPoints: [Point] = []
    max_x = len(inp)
    for x in range(max_x):
        max_y = len(inp[x])
        for y in range(max_y):
            numToCompare = inp[x][y]
            lower = True
            if x > 0:
                if numToCompare >= inp[x - 1][y]:
                    lower = False
            if x < max_x - 1:
                if numToCompare >= inp[x + 1][y]:
                    lower = False
            if y > 0:
                if numToCompare >= inp[x][y - 1]:
                    lower = False
            if y < max_y - 1:
                if numToCompare >= inp[x][y + 1]:
                    lower = False
            if lower:
                lowPoints.append(Point(x, y))

    return sum([inp[p.x][p.y] + 1 for p in lowPoints]), lowPoints


def findNonNine(inp: [[int]], p: Point, checkedPoints: [Point]) -> int:
    checkedPoints.append(p)
    num = 0
    max_x = len(inp)
    max_y = len(inp[p.x])
    if p.x > 0 and inp[p.x - 1][p.y] != 9 and Point(p.x - 1, p.y) not in checkedPoints:
        num += 1 + findNonNine(inp, Point(p.x - 1, p.y), checkedPoints)
    if p.x < max_x - 1 and inp[p.x + 1][p.y] != 9 and Point(p.x + 1, p.y) not in checkedPoints:
        num += 1 + findNonNine(inp, Point(p.x + 1, p.y), checkedPoints)
    if p.y > 0 and inp[p.x][p.y - 1] != 9 and Point(p.x, p.y - 1) not in checkedPoints:
        num += 1 + findNonNine(inp, Point(p.x, p.y - 1), checkedPoints)
    if p.y < max_y - 1 and inp[p.x][p.y + 1] != 9 and Point(p.x, p.y + 1) not in checkedPoints:
        num += 1 + findNonNine(inp, Point(p.x, p.y + 1), checkedPoints)

    return num


def part2(inp: [[int]]):
    lowPoints = part1(inp)[1]

    return math.prod(sorted([findNonNine(inp, p, []) + 1 for p in lowPoints])[::-1][:3])


print("Part1: ", part1(getInput())[0])

print("Part2: ", part2(getInput()))
