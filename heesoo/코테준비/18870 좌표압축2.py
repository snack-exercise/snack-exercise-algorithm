n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
print(arr2)

dict_val = {arr2[i] : i for i in range(len(arr2))}

for i in arr:
    print(dict_val[i], end = ' ')