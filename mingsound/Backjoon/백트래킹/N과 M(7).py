def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    # 백트래킹 핵심 구조
    for i in range(n):
        s.append(arr[i])
        dfs()
        s.pop()


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = []

for i in range(n):
    s.append(arr[i])
    dfs()
    s.pop()

