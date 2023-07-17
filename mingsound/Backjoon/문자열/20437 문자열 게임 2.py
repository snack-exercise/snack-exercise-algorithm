from collections import defaultdict

def length(dic):
    _min = 10001
    _max = 0

    for i in dic.keys(): # key
        for j in range(len(dic[i])-k+1):
            diff = dic[i][j+k-1] - dic[i][j] + 1
            _min = min(_min, diff)
            _max = max(_max, diff)

    return _min, _max

for _ in range(int(input())):
    dic = defaultdict(list)

    str = input()
    k = int(input())
    for i in range(len(str)): # 시간복잡도 10^8 - count가 O(n)
        if str.count(str[i]) >= k:
            dic[str[i]].append(i)

    if not dic:
        print(-1)
    else:
        print(*length(dic))

