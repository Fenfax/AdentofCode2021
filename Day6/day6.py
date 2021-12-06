def getInput():
    outdict: dict[int, int] = {}
    for r in open("input.txt"):
        for x in map(int, r.split(",")):
            outdict[x] = outdict.get(x, 0) + 1
    return outdict


def part1(indict: dict[int, int], repeat: int):
    tmp_val = 0
    for _ in range(repeat):
        for key in range(0, 9):
            indict[key - 1] = indict.get(key, 0)
        indict[6] += indict.get(-1, 0)
        indict[8] = tmp_val
        tmp_val = indict.get(0, 0)
        indict[-1] = 0
    return sum(indict.values())


print("Part1: ", part1(getInput(), 80))
print("Part2: ", part1(getInput(), 256))
