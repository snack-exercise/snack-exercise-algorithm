import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# deq에 현재 익은 토마토 위치를 전부 담는다.
# bfs를 돌린다. visited에는 일자를 기록한다.
# 이중 for문을 이용해서 모든 위치를 검사하면서 일자의 max 값 혹은 모든 토마토가 익지 못했는지 검사한다.

deq = deque([])
visited = [[-1] * m for _ in range(n)] # 초기값 -1
def start_tomato():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                deq.append((i, j))
                visited[i][j] = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and graph[nx][ny] == 0: # 아직 방문하지 않았고, 안익은 토마토 위치라면
                graph[nx][ny] = 1
                visited[nx][ny] = visited[x][y] + 1
                deq.append((nx, ny))


def check():
    _max = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0: # 하나라도 안익은 토마토가있다면
                return -1
            _max = max(_max, visited[i][j])

    return _max

start_tomato()
bfs()
print(check())

# BFS - 시작점이 여러개인 문제