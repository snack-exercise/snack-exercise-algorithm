def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    # 백트래킹 핵심 구조
    for i in range(n):
        if visited[i]:
            continue

        if len(s) != 0 and s[-1] > arr[i]:  # s가 비어있지 않은데, 가장 마지막에 있는 것보다 작으면, 오름차순 아님
            continue

        visited[i] = True
        s.append(arr[i])
        dfs()
        s.pop()
        visited[i] = False

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = []
visited = [False] * (n)

for i in range(n):
    visited[i] = True
    s.append(arr[i])

    dfs()
    s.pop()
    visited[i] = False
