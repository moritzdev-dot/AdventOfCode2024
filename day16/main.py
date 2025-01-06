import numpy as np
import heapq

content = []

with open("input.txt") as file:
    content = file.read().strip().split()


goal = None
start = None

for i in range(len(content)):
    for j in range(len(content[0])):
        if content[i][j] == "E":
            goal = (i, j)
        elif content[i][j] == "S":
            start = (i, j)

if goal is None or start is None:
    exit()


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

stack = [(0, start, 0)]

visited = {}
costs = []

heapq.heapify(stack)

while stack:
    cost, pos, dir_idx = heapq.heappop(stack)

    if pos == goal:
        print(cost)
        break

    for new_dir_idx, (dy, dx) in enumerate(dirs):
        new_pos = (pos[0] + dy, pos[1] + dx)

        if content[new_pos[0]][new_pos[1]] == '#':
            continue

        new_cost = cost + 1  
        if dir_idx != new_dir_idx: 
            turns_needed = min((new_dir_idx - dir_idx) % 4, (dir_idx - new_dir_idx) % 4)
            new_cost += turns_needed * 1000

        state = (new_pos, new_dir_idx)
        if state not in visited or visited[state] > new_cost:
            visited[state] = new_cost
            heapq.heappush(stack, (new_cost, new_pos, new_dir_idx))



