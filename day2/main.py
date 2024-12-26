import numpy as np

def isSafe(arr: list[int]):
    sign = np.sign(arr[0] - arr[1])
    for i in range(len(arr) - 1):
        sum = arr[i] - arr[i+1]
        if criterion(sum, sign):
            return 0
    return 1

def criterion(sum, sign):
    if(np.sign(sum) != sign) or abs(sum) < 1 or abs(sum) > 3:
        return True
    return False


def isSafeWithDamp(arr: list[int]):
    for i in range(len(arr)):
        if isSafe(arr[:i] + arr[i+1:]):
            return 1
    return 0


score = 0
score2 = 0
with open("input.txt") as file:
    content = file.read()
    lines = content.split("\n")
    for line in lines[:-1]:
        l = line.split(" ")
        try:
            l.remove("")
        except:
            pass
        nums = [int(x) for x in l]
        score += isSafe(nums)
        score2 += isSafeWithDamp(nums)
                
print(score)
print(score2)

