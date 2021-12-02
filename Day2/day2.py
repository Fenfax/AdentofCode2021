from typing import NamedTuple


class Command(NamedTuple):
    command: str
    value: int


def part1(inp: [Command]):
    x = 0
    y = 0
    for c in inp:
        match c.command:
            case "forward":
                x += c.value
            case "down":
                y += c.value
            case "up":
                y -= c.value

    return x * y


def part2(inp: [Command]):
    x = 0
    y = 0
    aim = 0

    for c in inp:
        match c.command:
            case "forward":
                x += c.value
                y += c.value * aim
            case "down":
                aim += c.value
            case "up":
                aim -= c.value

    return x * y


start = [Command(x.split(" ")[0], int(x.split(" ")[1])) for x in open("input.txt")]
print("Part1: ", part1(start))
print("Part2: ", part2(start))
