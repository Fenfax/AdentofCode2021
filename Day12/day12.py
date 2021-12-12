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


def getPath(caves: [Cave], current: Cave, visited: [Cave], path: [[Cave]], currentPath: [Cave], secondVisit: [Cave],
            shouldSecond: bool):
    if current in secondVisit and not shouldSecond:
        return path
    fobiddenSecondCave = ["start", "end"]
    if not current.big:
        if shouldSecond and current.name not in fobiddenSecondCave and current not in secondVisit:
            secondVisit.append(current)
        else:
            if current in secondVisit:
                shouldSecond = False
            visited.append(current)
    currentPath.append(current)
    if current.name == "end":
        return path
    for cave in current.connectedCaves:
        if cave in visited:
            continue
        newPath = currentPath.copy()
        path.append(newPath)
        newVisted = visited.copy()
        newSecondVisit = secondVisit.copy()
        getPath(caves, cave, newVisted, path, newPath, newSecondVisit, shouldSecond)

    return path


def solve(inp: dict[str, Cave], shouldSecond: bool):
    paths = getPath(inp.values(), inp.get("start"), [], [], [], [], shouldSecond)
    paths = [x for x in paths if x[len(x) - 1].name == "end"]
    return len(paths)


print("Part1: ", solve(getInput(), False))
print("Part2: ", solve(getInput(), True))
