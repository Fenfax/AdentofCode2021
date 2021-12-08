from typing import NamedTuple


class DigitRow(NamedTuple):
    allNum: str
    realNum: str


def getInput1():
    return [[y for y in x.replace("\n", '').split("|")[1].split(" ") if len(y) > 0] for x in open("input.txt")]


def getInput2() -> [DigitRow]:
    return [DigitRow(*([z for z in y.split(" ") if len(z) > 0] for y in x.replace("\n", "").split("|")))
            for x in open("input.txt")]


def part1(inp: [[str]]) -> int:
    numSum: int = 0
    for l in inp:
        for p in l:
            if len(p) in [2, 3, 4, 7]:
                numSum += 1

    return numSum


def asignNumber(inp: [str]) -> dict[int, str]:
    out_dict: dict[int, str] = {}
    fivelength: [str] = []
    sixlength: [str] = []
    for x in inp:
        match len(x):
            case 2:
                out_dict[1] = x
            case 3:
                out_dict[7] = x
            case 4:
                out_dict[4] = x
            case 7:
                out_dict[8] = x
            case 6:
                sixlength.append(x)
            case 5:
                fivelength.append(x)

    for y in sixlength:
        tmp_char = y
        for x in out_dict.get(1):
            tmp_char = tmp_char.replace(x, '')
        if len(tmp_char) == 5:
            out_dict[6] = y

    sixlength.remove(out_dict.get(6))

    for y in sixlength:
        tmp_char = y
        for x in out_dict.get(4):
            tmp_char = tmp_char.replace(x, '')
        match len(tmp_char):
            case 2:
                out_dict[9] = y
            case 3:
                out_dict[0] = y

    for x in fivelength:
        tmp_char = x
        for y in out_dict.get(1):
            tmp_char = tmp_char.replace(y, '')
        if len(tmp_char) == 3:
            out_dict[3] = x

    fivelength.remove(out_dict.get(3))

    for x in fivelength:
        tmp_char = x
        for y in out_dict.get(6):
            tmp_char = tmp_char.replace(y, "")
        if len(tmp_char) == 0:
            out_dict[5] = x
        elif len(tmp_char) == 1:
            out_dict[2] = x

    return out_dict


def part2(inp: [DigitRow]):
    numSum: int = 0
    for x in inp:
        rowNum: str = ""
        for y in x.realNum:
            rowNum += str([key for key, val in asignNumber(x.allNum).items() if sorted(val) == sorted(y)][0])
        numSum += int(rowNum)

    return numSum


print(part1(getInput1()))

print(part2(getInput2()))
