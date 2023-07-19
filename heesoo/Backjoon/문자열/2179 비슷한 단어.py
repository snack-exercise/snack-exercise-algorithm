n = int(input())
arr = [input() for _ in range(n)]
arrsort = sorted(list(enumerate(arr)),key = lambda x: x[1])

length = [0] * (n+1)
maxlength = 0

def count(a, arrsort):
    cnt = 0
    for i in range(min(len(a), len(arrsort))):
        if a[i] == arrsort[i]: cnt += 1
        else: break
    return cnt


for i in range(n-1):
    ans = count(arrsort[i][1], arrsort[i+1][1])

    maxlength = max(maxlength, ans)
    length[arrsort[i][0]] = max(length[arrsort[i][0]], ans)
    length[arrsort[i+1][0]] = max(length[arrsort[i+1][0]], ans)

flag = True
for i in range(n):
    if flag and length[i] == max(length):
        flag=False
        print(arr[i])
        pre = arr[i][:maxlength]
    else:
        if length[i] == max(length) and arr[i][:maxlength] == pre:
            print(arr[i])
            break