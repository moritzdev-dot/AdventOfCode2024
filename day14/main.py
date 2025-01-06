import numpy as np
import time
content = []
with open("input.txt") as file:
    content = file.read().strip().split("\n")


WIDTH = 101
HEIGHT = 103
#WIDTH = 11
#HEIGHT = 7
TIME_STEPS = 100

quads = [0, 0, 0, 0]
quad_limits = [
    ((0, WIDTH//2), (0, HEIGHT//2)),
    ((WIDTH//2 + 1, WIDTH), (0, HEIGHT//2)),
    ((0, WIDTH//2), (HEIGHT//2 + 1, HEIGHT)),
    ((WIDTH//2 + 1, WIDTH), (HEIGHT//2 + 1, HEIGHT))
]

for line in content:
    l = line.strip().split(" ")
    num1 = int(l[0][l[0].find("=")+1:l[0].find(",")])
    num2 = int(l[0][l[0].find(",")+1:])
    p = [num1, num2]
    num1 = int((l[1][l[1].find("=")+1:l[1].find(",")]))
    num2 = int(l[1][l[1].find(",")+1:])
    v = np.array([num1, num2])
    m = (v * TIME_STEPS + p) % np.array([WIDTH, HEIGHT])
    for i, quad in enumerate(quad_limits):
        x, y = m[0], m[1]
        x_lims = quad[0]
        y_lims = quad[1]
        if x_lims[0] <= x and x < x_lims[1] and y_lims[0] <= y and y < y_lims[1]: 
            quads[i] += 1
            break
print(np.prod(quads))

    



