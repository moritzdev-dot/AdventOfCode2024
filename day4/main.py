content = ""

with open("input.txt") as file:
    content = file.read()

lines = content.strip().split("\n")
sum = 0


length = len(lines)
width = len(lines[0])
directions = [
    (-1, -1),
    (-1,  1),
    ( 1, -1),
    ( 1,  1),
    ( 0,  1),
    ( 0, -1),
    ( 1,  0),
    (-1,  0)
]

sum = 0

for row in range(length):
    for col in range(width):
        for x, y in directions:
            f = True
            w = lines[row][col]
            for i in range(1, 4):
                a = row + i * x
                if a < 0 or a >= length:
                    f = False
                    break
                b = col + i * y
                if b < 0 or b >= width:
                    f = False
                    break
                w += lines[a][b]
                if w not in "XMAS" and  w not in "SAMX":
                    f = False
                    break
            if f:
                sum += 1


print(sum//2)


sum = 0
for row in range(1, length-1):
    for col in range(1, width-1):
        if lines[row][col] != "A":
            continue
        word1 = lines[row-1][col-1] + lines[row][col] + lines[row+1][col+1]
        word2 = lines[row-1][col+1] + lines[row][col] + lines[row+1][col-1]
        if (word1 == "MAS" or word1 == "SAM") and (word2 == "MAS" or word2 =="SAM"):
            sum += 1
        
print(sum)


