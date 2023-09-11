def dfs():
    if len(s) == m:
        print(" ".join(list(map(str, s))))
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
        if len(s) != 0 and s[-1] > i: # s가 비어있지 않은데, 가장 마지막에 있는 것보다 작으면, 오름차순 아님
            continue

        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False


n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

dfs()