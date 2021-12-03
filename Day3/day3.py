def getGamma(inp: [[str]]):
    return ''.join([mostCommonInArray(x) for x in flip2DArray(inp)])


def getEpsilon(inp: [[str]]):
    return ''.join([minCommonInArray(x) for x in flip2DArray(inp)])


def flip2DArray(inp: [[str]]):
    return [list(x) for x in list(zip(*inp[::-1]))]


def mostCommonInArray(inp: [str]):
    return max(set(inp), key=inp.count)


def minCommonInArray(inp: [str]):
    return min(set(inp), key=inp.count)


def part1(inp: [str]):
    work_arr: [[str]] = [[y for y in x] for x in inp]
    return int(getGamma(work_arr), 2) * int(getEpsilon(work_arr), 2)


dayinp = [x for x in open("input.txt")]

print(part1(dayinp))
