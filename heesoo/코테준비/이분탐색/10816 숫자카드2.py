n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr_ans = list(map(int, input().split()))

dict_val = {}
for i in arr:
    if i in dict_val:
        dict_val[i] += 1
    else:
        dict_val[i] = 1

print(dict_val)
for i in arr_ans:
    if i in set(dict_val.keys()):
        print(dict_val[i], end= ' ')
    else:
        print(0, end = ' ')

for t in arr_ans:
    r = dict_val.get(t)
    if r == None:
        print(0, end = ' ')
    else:
        print(r, end = ' ')