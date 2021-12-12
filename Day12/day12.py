from __future__ import annotations


class Cave:
    def __init__(self, name: str):
        self.name = name
        self.big = name.isupper()
        self.connectedCaves: set[Cave] = set()

    def addConnection(self, cave: Cave):
        self.connectedCaves.add(cave)
        return self


def getInput():
    caves: dict[str, Cave] = {}
    for x in open("input.txt"):
        connection = x.replace("\n", "").split("-")
        cA = connection[0]
        cB = connection[1]

        caves[cA] = caves.get(cA, Cave(cA))
        caves[cB] = caves.get(cB, Cave(cB))
        caves.get(cA).addConnection(caves.get(cB))
        caves.get(cB).addConnection(caves.get(cA))

    return caves


def getPath(caves: [Cave], current: Cave, visited: set[Cave], path: [[Cave]], currentPath: [Cave],shouldSecond: bool):
    if shouldSecond and current in visited:
        shouldSecond = False
    fobiddenSecondCave = ["start", "end"]
    if not current.big:
        visited.add(current)
    currentPath.append(current)
    if current.name == "end":
        path.append(currentPath)
        return path
    for cave in current.connectedCaves:
        if not(shouldSecond and cave.name not in fobiddenSecondCave) and cave in visited:
            continue
        newPath = currentPath.copy()
        newVisted = visited.copy()
        getPath(caves, cave, newVisted, path, newPath, shouldSecond)

    return path


def solve(inp: dict[str, Cave], shouldSecond: bool):
    paths = getPath(inp.values(), inp.get("start"), set(), [], [], shouldSecond)
    return len(paths)


print("Part1: ", solve(getInput(), False))
print("Part2: ", solve(getInput(), True))
