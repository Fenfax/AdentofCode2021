def part1(ins: [int]):
    old_num: int = None
    cnt: int = 0
    for x in ins:
        if old_num is not None and old_num < x:
            cnt += 1
        old_num = x
    return cnt


def part2(ins: [int]):
    old_num: int = None
    cnt: int = 0
    work_arr: [int] = []
    tmp_arr: [int] = []
    for x in ins:
        tmp_arr.append(x)
        if len(tmp_arr) >= 3:
            work_arr.append(sum(tmp_arr))
            tmp_arr.pop(0)

    for x in work_arr:
        if old_num is not None and old_num < x:
            cnt += 1
        old_num = x

    return cnt


print(part1([int(x) for x in open("input.txt")]))
print(part2([int(x) for x in open("input.txt")]))
