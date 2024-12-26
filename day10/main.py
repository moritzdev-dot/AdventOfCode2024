content = []
with open("input.txt") as file:
    content = file.read().strip().split("\n")

dirs = [
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1)
]
content2 = [list(s) for s in content]

def get_numbers_of_9s(content, i, j, map):
    try:
        val = int(content[i][j])
    except:
        return 0 


    if val == 9 and not map.get((i, j)):
        map[(i, j)] = True
        return 1

    paths = []
    
    for dir in dirs:
        dx, dy = dir
        if i+dx < 0 or i + dx > len(content) -1 or j + dy < 0 or j + dy > len(content[0])-1:
            continue
        if(content[i+dx][j+dy] == str(val + 1)):
            paths.append((i+dx, j+dy))


    if len(paths) == 0:
        return 0

    score = 0
    for path in paths:
        n, m = path
        s = get_numbers_of_9s(content, n, m, map)
        score += s

    return score

def get_unique_paths(content, i, j):
    try:
        val = int(content[i][j])
    except:
        return 0 


    if val == 9:
        return 1

    paths = []
    
    for dir in dirs:
        dx, dy = dir
        if i+dx < 0 or i + dx > len(content) -1 or j + dy < 0 or j + dy > len(content[0])-1:
            continue
        if(content[i+dx][j+dy] == str(val + 1)):
            paths.append((i+dx, j+dy))


    if len(paths) == 0:
        return 0

    score = 0
    for path in paths:
        n, m = path
        s = get_unique_paths(content, n, m)
        score += s

    return score





score = 0
for i in range(len(content)):
    for j in range(len(content[0])):
        if content[i][j] != "0":
            continue
        map = {}
        s = get_numbers_of_9s(content, i, j, map)
        score += s


print(score)


score = 0
for i in range(len(content)):
    for j in range(len(content[0])):
        if content[i][j] != "0":
            continue
        score +=  get_unique_paths(content, i, j)


print(score)

