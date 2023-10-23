n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = int(1e9)

def dfs(start, now, value, cnt):
    print(start, now, value, cnt)
    global ans
    if cnt == n:
        if a[now][start]:
            value += a[now][start]
            if ans > value:
                ans = value
            
        return

    if value > ans:
        return

    for i in range(n):
        if not visited[i] and a[now][i]:
            visited[i] = 1
            dfs(start, i, value + a[now][i], cnt + 1)
            visited[i] = 0

visited = [0] * n
for i in range(n):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0
print(ans)
