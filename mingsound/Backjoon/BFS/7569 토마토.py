import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# deq에 현재 익은 토마토 위치를 전부 담는다.
# bfs를 돌린다. visited에는 일자를 기록한다.
# 이중 for문을 이용해서 모든 위치를 검사하면서 일자의 max 값 혹은 모든 토마토가 익지 못했는지 검사한다.

deq = deque([])
visited = [[[-1] * m for _ in range(n)] for _ in range(h)] # 초기값 -1
def start_tomato():
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if graph[k][i][j] == 1:
                    deq.append((k, i, j))
                    visited[k][i][j] = 0


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
def bfs():
    while deq:
        z, x, y = deq.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and visited[nz][nx][ny] == -1 and graph[nz][nx][ny] == 0: # 아직 방문하지 않았고, 안익은 토마토 위치라면
                graph[nz][nx][ny] = 1
                visited[nz][nx][ny] = visited[z][x][y] + 1
                deq.append((nz, nx, ny))


def check():
    _max = 0
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if graph[k][i][j] == 0:  # 하나라도 안익은 토마토가있다면
                    return -1
                _max = max(_max, visited[k][i][j])

    return _max

start_tomato()
bfs()
print(check())

# BFS - 7576 토마토 (시작점이 여러개인 BFS)의 3차원 버전