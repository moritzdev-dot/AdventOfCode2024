content = []


def rules(num: int): 
    if num == 0:
        return [1]
    length = len(str(num))
    if length % 2 == 0:
        return [int(str(num)[:length//2]), int(str(num)[length//2:])]

    return [num * 2024]

with open("input.txt") as file:
    content = [int(n) for n in file.read().strip().split(" ")]

for _ in range(25):
    arr = []
    for i in content:
        arr.extend(rules(i))
    content = arr

print(len(content))


with open("input.txt") as file:
    content = [int(n) for n in file.read().strip().split(" ")]

