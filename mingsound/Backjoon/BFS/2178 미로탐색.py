import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]

deq = deque([(0, 0)])
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while deq:
    x, y = deq.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
            visited[nx][ny] = visited[x][y] + 1
            deq.append((nx, ny))

print(visited[n-1][m-1])

# BFS로 거리를 잴 수 있따.

