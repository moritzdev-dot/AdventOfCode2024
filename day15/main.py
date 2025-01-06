import numpy as np
import time 
import os

content = []
with open("input.txt") as file:
    content = file.read().strip().split("\n\n")

field = [list(s) for s in content[0].strip().split("\n")]
moves = list(content[1].replace('\n', ""))
content = field

dirs = {
    ">": np.array((0, 1)),
    "<": np.array((0, -1)),
    "^": np.array((-1, 0)),
    "v": np.array((1, 0)),
}

bot = None

for i in range(len(field)):
    for j in range(len(field[0])):
        if field[i][j] == "@":
            bot = np.array((i, j))
if bot is None:
    exit()

zero = np.array([0, 0]) 
maximum = np.array([len(field), len(field[0])]) 

for move in moves:
    dir = dirs[move]
    nextPos = dir + bot 
    if not (np.less(nextPos, maximum).all() and np.greater_equal(nextPos, zero).all()):
        continue


    if(content[nextPos[0]][nextPos[1]] == "#"):
        continue
    elif(content[nextPos[0]][nextPos[1]] == "."):
        content[bot[0]][bot[1]] = "."
        content[nextPos[0]][nextPos[1]] = "@"
        bot = nextPos
        continue
    else:
        j = 1
        while(content[j * dir[0] +  nextPos[0]][j * dir[1] +  nextPos[1]] == "O"):
            j += 1
        if content[j * dir[0] + nextPos[0]][j * dir[1] + nextPos[1]] == "#":
            continue
        else:
            content[j * dir[0] + nextPos[0]][j * dir[1] + nextPos[1]] = "O"
            content[nextPos[0]][nextPos[1]] = "@"
            content[bot[0]][bot[1]] = "."
            bot = nextPos


sum = 0
for i, line in enumerate(content):
    for j, c in enumerate(line):
        if c == "O":
            sum += 100 * i + j

print(sum)


content = []
with open("input.txt") as file:
    content = (file
        .read()
        .strip()
        .replace(".", "..")
        .replace("#", "##")
        .replace("@", "@.")
        .replace("O", "[]")
        .split("\n\n")
    )

field = [list(s) for s in content[0].strip().split("\n")]
moves = list(content[1].replace('\n', ""))
for line in field:
    print("".join(line))

for i in range(len(field)):
    for j in range(len(field[0])):
        if field[i][j] == "@":
            bot = np.array((i, j))
if bot is None:
    exit()

zero = np.array([0, 0]) 
maximum = np.array([len(field), len(field[0])]) 

content = field


dirs = {
    ">": (np.array((0, 1)), False),
    "<": (np.array((0, -1)), False),
    "^": (np.array((-1, 0)), True),
    "v": (np.array((1, 0)), True),
}

def pushBoxVertTest(dir, content, pos, num):
    if num > 3:
        return False

    if content[pos[0] + dir[0]][pos[1]] == "#":
        return False

    if content[pos[0] + dir[0]][pos[1]] in "[]":
        num += 1
        if not pushBoxVertTest(dir, content, pos + dir, num):
            return False

    if content[pos[0]][pos[1]] == "]":
        if content[pos[0] + dir[0]][pos[1] -1] == "#":
            return False
        if content[pos[0] + dir[0]][pos[1] -1] == "]":
            num += 1
            if not pushBoxVertTest(dir, content, pos + dir - np.array([0, 1]), num):
                return False
    else:
        if content[pos[0] + dir[0]][pos[1] +1] == "#":
            return False
        if content[pos[0] + dir[0]][pos[1] + 1] == "[":
            num += 1
            if not pushBoxVertTest(dir, content, pos + dir + np.array([0, 1]), num):
                return False
    return True

def pushBoxVert(dir, content, pos, num):
    if num > 3:
        return False

    if content[pos[0] + dir[0]][pos[1]] == "#":
        return False

    if content[pos[0] + dir[0]][pos[1]] in "[]":
        num += 1
        if not pushBoxVert(dir, content, pos + dir, num):
            return False

    if content[pos[0]][pos[1]] == "]":
        if content[pos[0] + dir[0]][pos[1] -1] == "#":
            return False
        if content[pos[0] + dir[0]][pos[1] -1] == "]":
            num += 1
            if not pushBoxVert(dir, content, pos + dir - np.array([0, 1]), num):
                return False
        content[pos[0]][pos[1]] = "."
        content[pos[0]][pos[1]-1] = "."
        content[pos[0] + dir[0]][pos[1]] = "]"
        content[pos[0] + dir[0]][pos[1]-1] = "["
    else:
        if content[pos[0] + dir[0]][pos[1] +1] == "#":
            return False
        if content[pos[0] + dir[0]][pos[1] +1] == "[":
            num += 1
            if not pushBoxVert(dir, content, pos + dir + np.array([0, 1]), num):
                return False
        content[pos[0]][pos[1]] = "."
        content[pos[0]][pos[1]+1] = "."
        content[pos[0] + dir[0]][pos[1]] = "["
        content[pos[0] + dir[0]][pos[1]+1] = "]"
    return True
for move in moves:
    dir, vert = dirs[move]
    nextPos = dir + bot 
    if not (np.less(nextPos, maximum).all() and np.greater_equal(nextPos, zero).all()):
        continue

    os.system("clear")
    for line in content:
        print("".join(line))
    print("")
    time.sleep(0.1)


    if(content[nextPos[0]][nextPos[1]] == "#"):
        continue
    elif(content[nextPos[0]][nextPos[1]] == "."):
        content[bot[0]][bot[1]] = "."
        content[nextPos[0]][nextPos[1]] = "@"
        bot = nextPos
        continue
    else:
        if vert:
            if pushBoxVertTest(dir, content, nextPos, 1):
                pushBoxVert(dir, content, nextPos, 1)
                content[bot[0]][bot[1]] = "."
                content[nextPos[0]][nextPos[1]] = "@"
                bot = nextPos
            continue


        j = 1
        pos = j * dir + nextPos
        while(content[pos[0]][pos[1]] == "[" or content[pos[0]][pos[1]] == "]"):
            j += 1
            pos = j * dir + nextPos


        if content[pos[0]][pos[1]] == "#" or j > 6:
            continue
        else:
            for i in range(j, 0, -1):
                pos = i * dir + nextPos
                pos2 = (i - 1) * dir + nextPos
                content[pos[0]][pos[1]] = content[pos2[0]][pos2[1]]
            content[bot[0]][bot[1]] = "."
            content[nextPos[0]][nextPos[1]] = "@"
            bot = nextPos



for line in content:
    print("".join(line))
sum = 0
for i, line in enumerate(content):
    for j, c in enumerate(line):
        if c == "[":
            sum += 100 * i + j

print(sum)
