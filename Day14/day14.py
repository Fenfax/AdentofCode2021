import re
from collections import Counter

from aoc_utils.profiler import profiler


def getInput():
    start = open("input.txt").readlines()[0].replace("\n", "")
    insert = {x.split(" -> ")[0]: x.split(" -> ")[1].replace("\n", "") for x in open("input.txt") if "->" in x}
    return start, insert


@profiler
def solv(start: str, inp: dict[str, str], steps: int):
    for _ in range(steps):
        reMatch = "(?=(" + '|'.join(inp.keys()) + "))"
        result = re.finditer(reMatch, start)
        pos = {f.start(): inp.get(f.group(1)) for f in result}

        start = ''.join((str(c) + pos.get(cnt, "")) for cnt, c in enumerate(start))

    c = Counter(start)
    return c.most_common()[0][1] - c.most_common()[-1][1]


@profiler
def solv_fast(start: str, inp: dict[str, str], steps: int):
    fast_start: dict[str, int] = {}
    for f in re.finditer("(?=(" + '|'.join(inp.keys()) + "))", start):
        fast_start[f.group(1)] = fast_start.get(f.group(1), 0) + 1

    char_cnt: dict[str, int] = {}
    for x in start:
        char_cnt[x] = char_cnt.get(x, 0) + 1

    for _ in range(steps):
        tmp_start: dict[str, int] = {}
        for x, z in [(key, val) for key, val in fast_start.items()]:
            if x in inp.keys():
                tmp_start[x[0] + inp.get(x)] = tmp_start.get(x[0] + inp.get(x), 0) + z
                tmp_start[inp.get(x) + x[1]] = tmp_start.get(inp.get(x) + x[1], 0) + z
                char_cnt[inp.get(x)] = char_cnt.get(inp.get(x), 0) + z
        fast_start = tmp_start.copy()

    return max(char_cnt.values()) - min(char_cnt.values())


print("Part1: ", solv(*getInput(), 10))
print("Part2: ", solv_fast(*getInput(), 40))
