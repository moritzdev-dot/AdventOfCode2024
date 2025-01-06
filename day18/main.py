import numpy as np
import heapq

with open("input.txt") as file:
    content = file.read().strip().split("\n")

cords = {}
limit = 1024
for i in content[:limit]:
    m = i.strip().split(",")
    cords[(int(m[0]), int(m[1]))] = True

dirs = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

SIDE = 70
goal = (70, 70)
cur = (0, 0)

map = {cur: 0}
def is_valid(pos):
    return not (
        cords.get(pos) or
        pos[0] < 0 or
        pos[0] > SIDE or
        pos[1] < 0 or
        pos[1] > SIDE
    )

class Node:
    def __init__(self, pos, cost, distance, parent):
        self.parent = parent
        self.cost = cost
        self.distance = distance
        self.pos = pos
        self.f = self.distance + self.cost

def distance(cur, goal):
    return np.sqrt(np.power(np.array(cur) - np.array(goal), 2).sum())


def search():
    heap = []
    start = Node(cur, 0, distance(cur, goal), None)
    cells = {
        cur: start
    }
    heapq.heappush(heap, (start.f, cur))
    while heap:
        node = heapq.heappop(heap)[1]
    
        if node == goal:
            return cells[node]
    
        for dir in dirs:
            next = (node[0] + dir[0], node[1] + dir[1])
            if not is_valid(next):
                continue
    
            nextNode = Node(
                next,
                cells[node].cost + 1,
                distance(next, goal),
                cells[node]
            )
            if not cells.get(next):
                cells[next] = nextNode
                heapq.heappush(heap, (nextNode.f, next))
            elif cells[next].cost > nextNode.cost:
                cells[next] = nextNode
                heapq.heappush(heap, (nextNode.f, next))
    return None

node = search()
if node == None:
    exit()
print(node.cost)
path = {}
while node:
    path[node.pos] = True
    node = node.parent


bytesLeft = content[limit:]
for byte in bytesLeft:
    m = byte.strip().split(",")
    cord = (int(m[0]), int(m[1]))
    cords[(int(m[0]), int(m[1]))] = True

    if path.get(cord):
        node = search()
        if node is None:
            print(cord)
        path = {}
        while node:
            path[node.pos] = True
            node = node.parent







