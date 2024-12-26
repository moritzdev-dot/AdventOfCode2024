import heapq

list1 = []
list2 = []
with open("input.txt") as file:
    l = file.read()
    l = l.split("\n")
    l.pop()
    for line in l:
        chars = line.split(" ")
        i = 0
        num = ""
        while True:
            try:
                int(chars[i])
                num += chars[i]
                i += 1
            except:
                break
        heapq.heappush(list1, int(num))
        while chars[i] == '':
            i += 1

        num = ""
        while True:
            try:
                int(chars[i])
                num += chars[i]
                i += 1
            except:
                break
        heapq.heappush(list2, int(num))




map = {}
for el in list2:
    try:
        map[el] += 1
    except:
        map[el] = 1

sum2 = 0
for el in list1:
    try:
        sum2 += map[el] * el
    except:
        pass


sum = 0
for i in range(len(list1)):
    el1 = heapq.heappop(list1)
    el2 = heapq.heappop(list2)
    sum += abs(el1 - el2)

print("One: ", sum)
print("Two: ", sum2)

