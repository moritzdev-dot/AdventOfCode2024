import matplotlib.pyplot as plt

content = []
with open("input.txt") as file:
    content = [list(x) for x in file.read().strip().split("\n")]

dirs = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]
visited = {}
polygons: list[tuple[set[tuple[int, int]], str]] = []

def outOfBounds(val, content):
    return val < 0 or val >= len(content)


def tracePoints(edges: set[tuple[tuple[int, int], tuple[int, int]]]):
    map = {}
    for edge in edges:
        if map.get(edge[0]):
            map[edge[0]].append(edge[1])
        else:
            map[edge[0]] = [edge[1]]

        if map.get(edge[1]):
            map[edge[1]].append(edge[0])
        else:
            map[edge[1]] = [edge[0]]


    corners = 0

    for el in map:
        es = map[el]
        if len(es) == 4:
            corners += 2
            continue
        e1, e2 = es[0], es[1]
        if (e1[0] - el[0]) * (e2[0] - el[0]) + (e1[1] - el[1]) * (e2[1] - el[1]) == 0:
            corners += 1

    return corners

def cleanSet(s: set[tuple[int, int]], content, letter):
    toRemove = []
    dirs = [
        (-1, 0),
        (0, -1),
        (-1, -1),
        (0, 0),
    ]

    for v in s:
        if outOfBounds(v[0], content):
            continue
        if outOfBounds(v[1], content[0]):
            continue

        sum = 0
        for dir in dirs:
            if not outOfBounds(v[0]+dir[0], content) and not outOfBounds(v[1] + dir[1], content[0])  and content[v[0]+dir[0]][v[1]+dir[1]] == letter:
                sum += 1

        if sum == 4:
            toRemove.append(v)

    for v in toRemove:
        s.remove(v)
    return s

def cleanEdges(edges: set, shape: set, content, letter):
    toRemove = []
    for edge in edges:
        start = edge[0]
        end = edge[1]

        if start not in shape or end not in shape:
            toRemove.append(edge)
            continue

        if end[1] < start[1]:
            x, y = end
            if outOfBounds(x-1, content) or outOfBounds(y, content) or outOfBounds(x, content) or outOfBounds(y, content):
                continue
            
            if content[x-1][y] == letter and content[x][y] == letter:
                toRemove.append(edge)

        elif end[1] > start[1]:
            x, y = start
            if outOfBounds(x-1, content) or outOfBounds(y, content) or outOfBounds(x, content) or outOfBounds(y, content):
                continue
            
            if content[x-1][y] == letter and content[x][y] == letter:
                toRemove.append(edge)
        elif end[0] < start[0]:
            x, y = end
            if outOfBounds(y-1, content) or outOfBounds(y, content) or outOfBounds(x, content):
                continue
            
            if content[x][y] == letter and content[x][y-1] == letter:
                toRemove.append(edge)
        else:
            x, y = start

            if outOfBounds(y-1, content[0]):
                continue
            if  outOfBounds(y, content[0]):
                continue
            if  outOfBounds(x, content):
                continue

                
            if content[x][y] == letter and content[x][y-1] == letter:
                toRemove.append(edge)


    for x in toRemove:
        edges.remove(x)

    return edges

def getRegion(x: int, y: int, content, visited):
    fenceNum = 0
    stack = [(x, y)]
    plants = 0
    letter = content[x][y]
    shape = set()
    edges = set()

    while len(stack) > 0:
        x, y = stack.pop()
        if visited.get((x, y)):
            continue
        plants += 1
        visited[(x, y)] = True
        fenceNum += 4
        for (dx, dy) in dirs:
            if x + dx < 0 or x + dx >= len(content) or y + dy < 0 or y +dy >= len(content[0]):
                continue

            if content[x + dx][y+dy] == letter:
                fenceNum -= 1
                if not visited.get((x + dx, y + dy)):
                    stack.append((x + dx, y + dy))

        shape.add((x, y))
        shape.add((x+1, y))
        shape.add((x, y+1))
        shape.add((x+1, y+1))

        edges.add(((x, y), (x+1, y)))
        edges.add(((x, y), (x, y+1)))
        edges.add(((x+1, y), (x+1, y+1)))
        edges.add(((x, y+1), (x+1, y+1)))

    shape = cleanSet(shape, content, letter)
    edges = cleanEdges(edges, shape, content, letter)

    corners = tracePoints(edges)
    #print(corners)
    #for edge in edges:
    #    plt.plot([edge[0][1], edge[1][1]], [-edge[0][0], -edge[1][0]])
    #plt.show()



    return fenceNum * plants, corners * plants

def getNextFreePos(content, visited):
    for i in range(len(content)):
        for j in range(len(content[0])):
            if not visited.get((i, j)):
                return (i, j)
    return None


freePos = getNextFreePos(content, visited)
sum = 0
sum2 = 0
while freePos is not None:
    x, y = freePos
    n1, n2  = getRegion(x, y, content, visited)
    sum += n1
    sum2 += n2

    freePos = getNextFreePos(content, visited)

print(sum, sum2)




