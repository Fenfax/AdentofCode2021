from collections import Counter


def getGamma(inp: [[str]]):
    return ''.join([mostCommonInArray(x) for x in flip2DArray(inp)])


def getEpsilon(inp: [[str]]):
    return ''.join([minCommonInArray(x) for x in flip2DArray(inp)])


def getO2Rating(inp: [[str]]):
    out = ""
    rem = [[z for z in y] for y in [x for x in inp if ''.join(x).startswith(out)]]
    cnt = 0
    while len(rem) > 1:
        out += mostCommonInArray(flip2DArray(rem)[cnt])
        cnt += 1
        rem = [[z for z in y] for y in [x for x in inp if ''.join(x).startswith(out)]]

    return ''.join([''.join(x) for x in rem])


def getCO2Scrubber(inp: [[str]]):
    out = ""
    rem = [[z for z in y] for y in [x for x in inp if ''.join(x).startswith(out)]]
    cnt = 0
    while len(rem) > 1:
        out += minCommonInArray(flip2DArray(rem)[cnt])
        cnt += 1
        rem = [[z for z in y] for y in [x for x in inp if ''.join(x).startswith(out)]]

    return ''.join([''.join(x) for x in rem])


def flip2DArray(inp: [[str]]):
    return [list(x) for x in list(zip(*inp))]


def mostCommonInArray(inp: [str]):
    def comp_comm_max(comp: [(str, int)]):
        return comp[0][0] if len(comp) == 1 or comp[0][1] > comp[1][1] else "1"

    return comp_comm_max(Counter(inp).most_common(2))


def minCommonInArray(inp: [str]):
    def comp_comm_min(comp: [(str, int)]):
        return comp[0][0] if len(comp) == 1 or comp[0][1] < comp[1][1] else "0"

    return comp_comm_min(Counter(inp).most_common()[:-2-1:-1])


def part1(inp: [str]):
    work_arr: [[str]] = [[y for y in x] for x in inp]
    return int(getGamma(work_arr), 2) * int(getEpsilon(work_arr), 2)


def part2(inp: [str]):
    work_arr: [[str]] = [[y for y in x] for x in inp]
    return int(getO2Rating(work_arr),2) * int(getCO2Scrubber(work_arr), 2)


dayinp = [x.replace("\n", "") for x in open("input.txt")]

print("Part1: ", part1(dayinp))

print("Part2: ", part2(dayinp))
