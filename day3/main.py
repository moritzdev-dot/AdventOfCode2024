def isNumber(c):
    return ord('0') <= ord(c) and ord(c) <= ord('9')


with open("input.txt") as file:
    content = file.read()
    start = 0
    sum = 0
    while content.find("mul(", start) != -1:
        idx = content.find("mul(", start) + 4
        end = idx
        while isNumber(content[end]):
            end += 1
        if content[end] != ',':
            start = end + 1
            continue

        num1 = int(content[idx:end])
        idx = end + 1
        end = idx
        while isNumber(content[end]):
            end += 1

        if content[end] != ')':
            start = end + 1
            continue

        num2 = int(content[idx:end])
        sum += num1 * num2
        start = end + 1

    print(sum)

with open("input.txt") as file:
    content = file.read()
    sum = 0
    start = 0
    sum = 0
    enabled = True
    while content.find("mul(", start) != -1:
        idx = content.find("mul(",start)

        last = start
        while content.find("do()", last, idx) != -1:
            last  = content.find("do()", last, idx) + 1
            enabled = True


        while content.find("don't()", last, idx) != -1:
            last  = content.find("don't()", last, idx) + 1
            enabled = False
        
        idx = idx + 4
        end = idx
        if not enabled:
            start = idx
            continue 

        while isNumber(content[end]):
            end += 1
        if content[end] != ',':
            start = end + 1
            continue

        num1 = int(content[idx:end])
        idx = end + 1
        end = idx
        while isNumber(content[end]):
            end += 1

        if content[end] != ')':
            start = end + 1
            continue

        num2 = int(content[idx:end])
        sum += num1 * num2
        start = end + 1
    print(sum)





