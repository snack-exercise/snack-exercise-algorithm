n = int(input())
arr = list(map(int, input().split()))

temp_list = []
for i in range(len(arr)):
    temp_list.append([i, arr[i]])

temp_list = sorted(temp_list, key = lambda x:x[1])

temp_list[0].append(0)
num = temp_list[0][1]
pos = 0

for i in range(1, len(temp_list)):
    a, b = temp_list[i]
    if temp_list[i - 1][1] < b:
        pos += 1
        temp_list[i].append(pos)
    else:
        temp_list[i].append(pos)

temp_list = sorted(temp_list, key = lambda x : x[0])

for c in temp_list:
    print(c[2], end = ' ')