def getInput():
    tmp = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]"""

    # return [x for x in tmp.split("\n")]
    return [x.replace("\n", "") for x in open("input.txt")]


def calcScorePart1(inp: [str]):
    for y in inp:
        match y:
            case ")":
                return 3
            case "]":
                return 57
            case "}":
                return 1197
            case ">":
                return 25137

    return 0


def calcScorePart2(inp: [str], closeings: [str]):
    score: int = 0
    for x in inp:
        score *= 5
        score += y + 1 if (y := closeings.index(x)) >= -1 else 0
    return score


def returnRmaining(inp: str, pair: dict[str, str]):
    while True:
        indexToRemove: [int] = []
        for x in range(len(inp) - 1):
            if pair.get(inp[x]) == inp[x + 1]:
                indexToRemove.append(x)
                indexToRemove.append(x + 1)

        if len(indexToRemove) == 0:
            break

        for x in sorted(indexToRemove)[::-1]:
            inp = inp[0:x] + inp[x + 1:]

    return inp


def isCorrupted(inp: str, pair: dict[str, str]):
    remaining = returnRmaining(inp, pair)
    return any(x in pair.values() for x in remaining), \
           [x for x in remaining if x in pair.values()], \
           [x for x in remaining if x in pair.keys()]


def solve(inp: [str]):
    validLines: [str] = []
    openings: [str] = ["(", "[", "{", "<"]
    closeings: [str] = [")", "]", "}", ">"]
    pair: dict[str, str] = dict(zip(openings, closeings))
    scorep1: int = 0
    scorep2: [int] = []
    for x in inp:
        isCurr, closeing, openings = isCorrupted(x, pair)
        if isCurr:
            scorep1 += calcScorePart1(closeing)
        else:
            scorep2.append(calcScorePart2([pair.get(x) for x in openings[::-1]], closeings))

    print(scorep1)
    print(sorted(scorep2)[int(len(scorep2) / 2)])


solve(getInput())
