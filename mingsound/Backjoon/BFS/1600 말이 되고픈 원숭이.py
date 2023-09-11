import sys
input = sys.stdin.readline
from collections import deque


k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
visited = [[[0] * w for _ in range(h)] for _ in range(k+1)]
# print(len(visited), len(visited[0]), len(visited[0][0]))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dx2 = [-1, -1, -2, -2, 1, 1, 2, 2]
dy2 = [-2, 2, -1, 1, -2, 2, -1, 1]

deq = deque([(0, 0, 0)]) # (x, y, cnt)
visited[0][0][0] = 1

while deq:
    x, y, cnt = deq.popleft()

    if x == h-1 and y == w-1:
        print(visited[cnt][x][y]-1)
        exit(0)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and not visited[cnt][nx][ny] and graph[nx][ny] == 0:
            visited[cnt][nx][ny] = visited[cnt][x][y] + 1
            deq.append((nx, ny, cnt))

    if cnt < k:
        for i in range(8):
            nx = x + dx2[i]
            ny = y + dy2[i]
            if 0 <= nx < h and 0 <= ny < w and not visited[cnt+1][nx][ny] and graph[nx][ny] == 0:
                visited[cnt+1][nx][ny] = visited[cnt][x][y] + 1
                deq.append((nx, ny, cnt+1))

print(-1)