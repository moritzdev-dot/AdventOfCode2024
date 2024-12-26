content = []

with open("input.txt") as file:
    content = file.read().strip().split("\n")

i = 0
edges = {}

def includes(arr, arr2):
    for i in arr2:
        if i in arr:
            return True
    return False




while content[i] != "":
    tmp = content[i].split("|")
    num1 = int(tmp[0])
    num2 = int(tmp[1])
    try:
        edges[num1].append(num2)
    except:
        edges[num1] = [num2]
    i+=1

content = content[i+1:]
sum = 0
wrongOrder = []
for line in content:
    numbers = [int(i) for i in line.strip().split(",")]
    toAdd = True
    for i in range(len(numbers)):
        try:
            if includes(numbers[:i], edges[numbers[i]]):
                toAdd = False
                break
        except:
            pass
    if toAdd:
        sum += numbers[len(numbers)//2]
    else:
        wrongOrder.append(numbers)

print(sum)

sum = 0
for nums in wrongOrder:
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            # nums[j] > nums[j+1]
            try:
                if nums[j] in edges[nums[j+1]]:
                    tmp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = tmp
            except:
                pass
    sum += nums[len(nums)//2]

print(sum)




