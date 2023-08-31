from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(i, j):
    deq = deque([(i, j)])
    visited[i][j] = True
    size = 0

    while deq:
        x, y = deq.pop()
        size += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                deq.append((nx, ny))

    return size


_max = 0
count = 0
for i in range(n):
    for j in range(m):
        # 만약 아직 방문하지 않았고, 1이라면, bfs 수행 -> 그림 하나 count
        # bfs의 return 값으로 그림의 크기
        if not visited[i][j] and graph[i][j] == 1:
            _max = max(_max, bfs(i, j))
            count += 1
print(count)
print(_max)

