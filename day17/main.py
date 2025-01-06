program = []
A, B, C = 0, 0, 0
with open("input.txt") as file:
    c = file.read().strip().split("\n\n")
    program = ([int(i) for i in c
        .pop()
        .strip()
        .split(" ")
        .pop()
        .split(",")
    ])
    lines = c.pop().strip().split("\n")
    arr = [int(n.split(" ").pop()) for n in lines]
    A = arr[0]
    B = arr[1]
    C = arr[2]


outputs = []
def getOperandValue(code):
    if code < 4:
        return code
    elif code == 4:
        return A
    elif code == 5:
        return B

    return C


ops = []
outs = []
tmp = A

p = 0
while p < len(program) - 1:
    if p >= len(program):
        p = p // 2
    opcode = program[p]
    if opcode == 0:
        val = getOperandValue(program[p+1])
        A = int(A / (2**val))

    elif opcode == 1:
        B = B ^ program[p+1]

    elif opcode == 2:
        val = getOperandValue(program[p+1])
        B = val % 8

    elif opcode == 3:
        if A != 0:
            val = program[p+1]
            p = val
            continue

    elif opcode == 4:
        B = B ^ C
    elif opcode == 5:
        ops = []
        val = getOperandValue(program[p+1])
        outputs.append(val % 8)


    elif opcode == 6:
        val = getOperandValue(program[p+1])
        B = int(A / (2**val))

    else:
        val = getOperandValue(program[p+1])
        C = int(A / (2**val))
    p += 2




print(",".join([str(s) for s in outputs]))

def calcB(A):
    return (((A% 8) ^ 3) ^ 5) ^ (A >> ((A % 8) ^ 3))

def decProg(A):
    out = []
    while A != 0:
        B = (((A% 8) ^ 3) ^ 5) ^ (A >> ((A % 8) ^ 3))
        A >>= 3
        out.append(B % 8)
    return out


AMin = 8 **(len(program)-1)
AMax = 8 **(len(program)) - 1


possibleAs = [0]
n = 1
while possibleAs and decProg(possibleAs[0]) != program:
    A = possibleAs.pop(0)
    A <<= 3
    for i in range(8):
        valA = A + i
        p = decProg(valA)
        if p  and p == program[-(len(p)):]:
            possibleAs.append(valA)

print(min(possibleAs))











