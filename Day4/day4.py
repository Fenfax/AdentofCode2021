class BoardPos:
    def __init__(self, value: int, drawn: bool):
        self.value = value;
        self.drawn = drawn;


def rotate2dArray(inp: [[BoardPos]]):
    return [list(x) for x in list(zip(*inp))]


def hasWon(inp: [[BoardPos]]) -> bool:
    for x in inp:
        if len(x) == len([y for y in x if y.drawn is True]):
            return True
    for x in rotate2dArray(inp):
        if len(x) == len([y for y in x if y.drawn is True]):
            return True
    return False


def setDrawn(inp: [[BoardPos]], number: int) -> [[BoardPos]]:
    for i, x in enumerate(inp):
        for i2, y in enumerate(x):
            if y.value == number:
                inp[i][i2].drawn = True
    return inp


def calcScore(winBoard: [[BoardPos]], winNum: int) -> int:
    return sum([sum([y.value for y in x if y.drawn is False]) for x in winBoard]) * winNum


def readInp():
    tmp = [x.replace("\n", "") for x in open("input.txt")]

    drawnumbers: [int] = [int(x) for x in tmp[0].split(",")]
    tmp.pop(0)
    tmp.pop(0)
    boards: [[[BoardPos]]] = []
    board: [[BoardPos]] = []
    for x in tmp:
        if len(x) == 0:
            boards.append(board) if len(board) > 0 else None
            board = []
        else:
            board.append([BoardPos(int(y), False) for y in x.split(" ") if len(y) > 0])
    else:
        boards.append(board) if len(board) > 0 else None

    return drawnumbers, boards


def part1(drawnumbers, boards):
    for number in drawnumbers:
        for i, board in enumerate(boards):
            boards[i] = setDrawn(board, number)

        for board in boards:
            if hasWon(board):
                return calcScore(board, number)


def part2(drawnumbers, boards):
    wonBoards: [[[BoardPos]]] = []
    for number in drawnumbers:
        for i, board in enumerate(boards):
            boards[i] = setDrawn(board, number)

        for board in boards:
            if hasWon(board) and board not in wonBoards:
                wonBoards.append(board)
                if len(wonBoards) == len(boards):
                    return calcScore(board, number)


print(part1(*readInp()))
print(part2(*readInp()))
