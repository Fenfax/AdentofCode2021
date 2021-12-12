class Octups:
    def __init__(self, start: int):
        self.energy: int = start

    def increaseEnergy(self):
        self.energy += 1

    def flash(self) -> bool:
        if self.energy > 9:
            self.energy = 0
            return True
        else:
            return False

    def readyToFlash(self) -> bool:
        return self.energy == 9


def getInput():
    return [[Octups(int(y)) for y in x.replace("\n", "")] for x in open("input.txt")]


def checkflash(inp: [[Octups]], row, col):
    maxRow = len(inp)
    maxCol = len(inp[row])
    if inp[row][col].readyToFlash():
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if 0 <= row + x < maxRow and 0 <= col + y < maxCol:
                    inp[row][col].increaseEnergy()
                    checkflash(inp, row + x, col + y)
    else:
        inp[row][col].increaseEnergy()


def amoutOfFlashes(inp: [[Octups]]):
    flashes: int = 0
    maxRow = len(inp)
    for row in range(maxRow):
        maxCol = len(inp[row])
        for col in range(maxCol):
            checkflash(inp, row, col)

    for row in inp:
        for col in row:
            if col.flash():
                flashes += 1
    return flashes


def part1(inp: [[Octups]], steps: int):
    flashes: int = 0
    for _ in range(steps):
        flashes += amoutOfFlashes(inp)

    return flashes


def part2(inp: [[Octups]]):
    allFlash = 1
    cnt = sum([len(x) for x in inp])
    while amoutOfFlashes(inp) != cnt:
        allFlash += 1

    return allFlash


print("Part1:", part1(getInput(), 100))
print("Part2:", part2(getInput()))
