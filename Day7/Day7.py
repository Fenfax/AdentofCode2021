def getInput():
    outdict: dict[int, int] = {}
    for r in open("input.txt"):
        for x in sorted(map(int, r.split(","))):
            outdict[x] = outdict.get(x, 0) + 1
    return outdict


def part1(inp: dict[int, int]):
    return min([sum([abs(num1 - num2) * cnt for num2, cnt in inp.items()]) for num1 in inp.keys()])


def part2(inp: dict[int, int]):
    return min(
        [sum([sum(range(abs(num1 - num2) + 1)) * cnt for num2, cnt in inp.items()]) for num1 in
         range(1, int((max(inp.keys()) + 1) / 2))])


print("Part1: ", part1(getInput()))
print("Part2: ", part2(getInput()))
