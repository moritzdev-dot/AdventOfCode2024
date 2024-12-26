content = []
with open("input.txt") as file:
    content = [list(c) for c in file.read().strip().split("\n")]

dir = {
    "^": (-1, 0),
    ">": (0, 1),
    "<": (0, -1),
    "v": (1, 0),
}

pos = (0, 0)
currentDir = (0, 0)
for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] != "#" and content[i][j] != ".":
            pos = (i, j)
            currentDir = dir[content[i][j]]
            break

print(currentDir)
content2 = content
pos2 = pos
startPos = pos
dir2 = currentDir
startDir = dir2

sum = 1
xs = []
while (pos[0] + currentDir[0] >= 0 and pos[1] + currentDir[1] >= 0 and pos[0] + currentDir[0] < len(content) and pos[1] + currentDir[1] < len(content[0])):
    x, y = pos[0], pos[1]
    dx, dy = currentDir[0], currentDir[1]
    if content[x + dx][y + dy] == "#":
        currentDir = (currentDir[1], -currentDir[0])
    elif content[x][y] == ".":
        content[x][y] = "X"
        xs.append((x, y))
        sum += 1
        pos = (x + dx, y + dy)
    else:
        pos = (x + dx, y + dy)
xs.append(pos)

print(sum+1)

width= len(content2)
length  = len(content2[0])
map = {}

sum = 0

for (i,j) in xs:
    if (i, j) == startPos:
        continue
    content2[i][j] = "#"
    found = False
    map = {}
    pos2 = startPos
    dir2 = startDir

    while True:
        x, y = pos2
        dx, dy = dir2

        if x + dx >= length or x + dx < 0 or y + dy >= width or y + dy < 0:
            break

        try:
            if map[(x, y)][(dx, dy)]:
                found = True
                break
        except:
            pass


        if map.get((x, y)):
            map[(x, y)][(dx, dy)] = True
        else:
            map[(x,y)] = {
                (dx, dy): True
            }

        if content2[x + dx][y + dy] == "#":
            dir2 = (dy, -dx)
        else:
            pos2 = (x + dx, y + dy)

    content2[i][j] = "."
    if found:
        content2[i][j] = "O"
        sum += 1


print(sum)


