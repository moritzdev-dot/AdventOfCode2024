import numpy as np

with open("input.txt") as file:
    content = file.read().strip()

i = 0
id = 0
s = []
while i < len(content):
    length = int(content[i])
    if i == len(content) -1:
        freeSpace = 0
    else:
        freeSpace = int(content[i+1])
    s.extend(length * [str(id)])
    s.extend(freeSpace * ["."])

    id += 1
    i += 2
start = 0
digit = len(s) - 1
sum = 0
while "." in s:
    digit = len(s) - 1
    while s[digit] == ".":
        digit -= 1

    for i in range(start, len(s)):
        if s[i] == ".":
            start = i
            break

    s[start] = s[digit]
    s = s[:digit]

for i, char in enumerate(s):
    sum += i * int(char)

print(sum)


i = 0
id = 0
s = []
ids = []
freeSpaces = []
idx = 0

while i < len(content):
    length = int(content[i])
    if i == len(content) -1:
        freeSpace = 0
    else:
        freeSpace = int(content[i+1])
    s.extend(length * [str(id)])
    s.extend(freeSpace * ["."])

    if freeSpace > 0:
        freeSpaces.append((idx + length, freeSpace))

    ids.append((length, idx))
    idx += length + freeSpace

    id += 1
    i += 2

start = 0
end = 0
id = len(ids) - 1

for id in range(len(ids) - 1, -1, -1):
    length, pos = ids[id]
    i = None
    spaceIdx, spaceLen  = 0, 0

    for j, t in enumerate(freeSpaces):
        idx, l = t
        if l >= length and idx + l <= pos:
            i = j
            spaceLen = l
            spaceIdx = idx
            break

    if i is None:
        continue

    for j in range(pos, pos+length):
        s[j] = "."
    for j in range(spaceIdx, spaceIdx + length):
        s[j] = str(id)

    if spaceLen - length > 0:
        freeSpaces[i] = (spaceIdx + length, spaceLen - length)
    else:
        freeSpaces.pop(i)

sum = 0

for i, char in enumerate(s):
    if char != ".":
        sum += i * int(char)

print(sum)


