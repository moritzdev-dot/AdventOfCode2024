from bisect import bisect_left
from itertools import product

content = []
with open("input.txt") as file:
    content = file.read().strip().split("\n")


def create_all_combinations(n) -> list[list[int]]:
    if n == 1:
        return [[1], [0]]
    solution = []
    for i in create_all_combinations(n-1):
        m = [1]
        l = [0]
        m.extend(i)
        l.extend(i)
        solution.append(m)
        solution.append(l)

            
    return solution



numbers = []
sum = 0
removed = []
next_input = []

for line in content:
    l = line.split(":")
    result = int(l[0])
    operands = [int(i) for i in l[1].strip().split(" ")]
    operators = [0] * (len(operands)-1)
    combs = create_all_combinations(len(operators))
    found = False
    for i in range(len(combs)):
        res = 0
        for j in range(len(combs[i])):
            if j == 0:
                res = operands[j]

            if combs[i][j] == 1:
                res *= operands[j+1]
            else:
                res += operands[j+1]


        if res == result:
            sum += result
            found = True
            break
    if not found:
        next_input.append(line)

print(sum)


for line in next_input:
    l = line.split(":")
    result = int(l[0])
    operands = [int(i) for i in l[1].strip().split(" ")]
    operators = [0] * (len(operands)-1)
    combs = list(product([0, 1, 2], repeat=len(operators)))
    for i in range(len(combs)):
        res = 0
        for j in range(len(combs[i])):
            if 2 not in combs[i]:
                break

            if j == 0:
                res = operands[j]

            if res > result:
                break


            if combs[i][j] == 1:
                res *= operands[j+1]
            elif combs[i][j] == 2:
                res = int(str(res) + str(operands[j+1]))
            else:
                res += operands[j+1]


        if res == result:
            sum += result
            break

print(sum)






