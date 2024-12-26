import numpy as np

content = []
with open("input.txt") as file:
    content = file.read().strip().split("\n\n")

machines = [] 

for i in range(len(content)):
    t = content[i].split("\n")
    a = t[0].strip()
    b = t[1].strip()
    c = t[2].strip()

    num1 = int(a[a.find("X")+1:a.find(",")])
    num2 = int(a[a.find("Y")+1:])
    A = (num1, num2)

    num1 = int(b[b.find("X")+1:b.find(",")])
    num2 = int(b[b.find("Y")+1:])
    B = (num1, num2)

    num1 = int(c[c.find("X")+2:c.find(",")])
    num2 = int(c[c.find("Y")+2:])
    C = (num1, num2)
    machines.append((A, B, C))

priceA = 3
priceB = 1

# a * A_x + b * B_x = X
# a * A_y + b * B_y = Y
# min(3 * a + b)
#
sum = 0

for machine in machines:
    A, B, C = machine
    A = np.array([A, B]).astype(np.int64).T
    B = np.array(C).astype(np.int64)
    sol = np.linalg.solve(A, B).round().astype(np.int64)
    if not np.array_equal(A @ sol.T,B):
        continue
    sum += 3 * sol[0] + sol[1]
print(sum)

sum = 0
X = np.array([10000000000000, 10000000000000])
for machine in machines:
    A, B, C = machine
    A = np.array([A, B]).astype(np.int64).T
    B = np.array(C).astype(np.int64) + X
    sol = np.linalg.solve(A, B).round().astype(np.int64)

    if not np.array_equal(A @ sol.T,B):
        continue

    sum += 3 * sol[0] + sol[1]

print(sum)




