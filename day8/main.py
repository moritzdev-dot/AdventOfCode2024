content = []
from typing import Tuple
from itertools import combinations
import numpy as np

with open("input.txt") as file:
    content = [list(i) for i in file.read().strip().split("\n")]


map: dict[str, list[Tuple[int, int]]] = {}


for i in range(len(content)):
    for j in range(len(content[0])):
        if content[i][j] != '.':
            if map.get(content[i][j]) is None:
                map[content[i][j]] = [(i, j)]
            else:
                map[content[i][j]].append((i, j))


width = len(content[0])
height = len(content)
content2 = content
sum = 0

for antenna, coords in map.items():
    combs = list(combinations(coords, 2))
    for comb in combs:
        dir = np.array([comb[0][0] - comb[1][0], comb[0][1] - comb[1][1]])
        loc = np.array(comb[1])
        i = 0
        l1 = loc + 2 * dir
        if l1[0] < height and l1[0] >= 0 and l1[1] < width and l1[1] >=0:
            if content[l1[0]][l1[1]] != "#":
                content[l1[0]][l1[1]] = "#"
                sum += 1

        l1 = loc - 1 * dir
        if l1[0] < height and l1[0] >= 0 and l1[1] < width and l1[1] >=0:
            if content[l1[0]][l1[1]] != "#":
                content[l1[0]][l1[1]] = "#"
                sum += 1

print(sum)
sum = 0
with open("input.txt") as file:
    content = [list(i) for i in file.read().strip().split("\n")]



for antenna, coords in map.items():
    combs = list(combinations(coords, 2))
    for comb in combs:
        dir = np.array([comb[0][0] - comb[1][0], comb[0][1] - comb[1][1]])
        loc = np.array(comb[1])
        i = 0
        l1 = loc + i * dir
        while l1[0] < height and l1[0] >= 0 and l1[1] < width and l1[1] >=0:
            if content[l1[0]][l1[1]] != "#":
                content[l1[0]][l1[1]] = "#"
                sum += 1
            i += 1
            l1 = loc + i * dir

        i = 0
        l1 = loc - i * dir
        while l1[0] < height and l1[0] >= 0 and l1[1] < width and l1[1] >=0:
            if content[l1[0]][l1[1]] != "#":
                content[l1[0]][l1[1]] = "#"
                sum += 1
            i += 1
            l1 = loc - i * dir

for i in content:
    print(" ".join(i))
print(sum)
