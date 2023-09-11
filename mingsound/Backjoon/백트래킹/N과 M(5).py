def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    # 백트래킹 핵심 구조
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        s.append(arr[i])
        dfs()
        s.pop()
        visited[i] = False

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = []
visited = [False] * (n+1)

dfs()