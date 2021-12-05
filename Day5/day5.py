from typing import NamedTuple


class Cord(NamedTuple):
    x: int
    y: int


class Vents(NamedTuple):
    cordFrom: Cord
    cordTo: Cord

    def getVertical(self) -> bool:
        return self.cordTo.x == self.cordFrom.x

    def getVerticalDistance(self) -> int:
        return abs(self.cordTo.y - self.cordFrom.y)

    def getSmallestVertical(self) -> int:
        return self.cordTo.y if self.cordTo.y < self.cordFrom.y else self.cordFrom.y

    def getHorizontal(self) -> bool:
        return self.cordTo.y == self.cordFrom.y

    def getHorizontalDistance(self) -> int:
        return abs(self.cordFrom.x - self.cordTo.x)

    def getSmallestHorizonzal(self) -> int:
        return self.cordTo.x if self.cordTo.x < self.cordFrom.x else self.cordFrom.x


def getInput():
    return [Vents(*(Cord(*map(int, y.split(","))) for y in x.split("->"))) for x in open("input.txt")]


def solv(inp: [Vents], doDiag: bool) -> int:
    ventcount: dict[Cord, int] = {}
    for x in inp:
        if x.getHorizontal():
            for pos in [Cord(horz, x.cordFrom.y)
                        for horz in range(x.getSmallestHorizonzal(),
                                          x.getSmallestHorizonzal() + x.getHorizontalDistance() + 1)]:
                ventcount[pos] = ventcount.get(pos, 0) + 1
        elif x.getVertical():
            for pos in [Cord(x.cordFrom.x, vert)
                        for vert in range(x.getSmallestVertical(),
                                          x.getSmallestVertical() + x.getVerticalDistance() + 1)]:
                ventcount[pos] = ventcount.get(pos, 0) + 1
        elif doDiag:
            for pos in [Cord(
                    x.cordFrom.x + dist if x.cordFrom.x == x.getSmallestHorizonzal() else x.cordFrom.x - dist,
                    x.cordFrom.y + dist if x.cordFrom.y == x.getSmallestVertical() else x.cordFrom.y - dist
            ) for dist in range(0, x.getHorizontalDistance() + 1)]:
                ventcount[pos] = ventcount.get(pos, 0) + 1
    return sum([1 for x in ventcount.values() if x > 1])


print("Part1: ", solv(getInput(), False))
print("Parr2: ", solv(getInput(), True))
