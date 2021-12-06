def getInput():
    outdict: dict[int, int] = {}
    for r in open("input.txt"):
        for x in map(int, r.split(",")):
            outdict[x] = outdict.get(x, 0) + 1
    return outdict


def solv(indict: dict[int, int], repeat: int):
    tmp_val = 0
    for _ in range(repeat):
        for key in range(0, 9):
            indict[key - 1] = indict.get(key, 0)
        indict[6] += indict.get(-1, 0)
        indict[8] = tmp_val
        tmp_val = indict.get(0, 0)
        indict[-1] = 0
    return sum(indict.values())


def solvSlow(inp: [int], repeat: int):
    for _ in range(repeat):
        print(_)
        for i in range(len(inp)):
            if inp[i] > 0:
                inp[i] = inp[i] - 1
            else:
                inp[i] = 6
                inp.append(8)
    return len(inp)


print("Part1: ", solv(getInput(), 80))
print("Part2: ", solv(getInput(), 256))

print(solvSlow([int(x) for x in open("input.txt").readline().split(",")], 80))
# This takes way to long
# print(solvSlow([int(x) for x in open("input.txt").readline().split(",")], 256))
