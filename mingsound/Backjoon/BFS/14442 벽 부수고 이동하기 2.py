import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[[0] * m for _ in range(n)] for _ in range(k+1)]
# print(len(visited), len(visited[0]), len(visited[0][0]))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    deq = deque([(0, 0, 0)]) # (x, y, cnt)
    visited[0][0][0] = 1

    while deq:
        x, y, cnt = deq.popleft()

        if x == n-1 and y == m-1: # 원하는 위치에 도달
            return visited[cnt][x][y]


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m: # 격자 범위 안에 들어오는 경우에 대해서만
                # 다음 이동 칸이 벽이 아닌 경우
                if graph[nx][ny] == 0:

                    if not visited[cnt][nx][ny]:
                        visited[cnt][nx][ny] = visited[cnt][x][y] + 1
                        deq.append((nx, ny, cnt))
                # 다음 이동 칸이 벽인 경우
                else:
                    if cnt < k and not visited[cnt+1][nx][ny]: # 아직 벽을 부술 수 있는 경우
                        visited[cnt+1][nx][ny] = visited[cnt][x][y] + 1
                        deq.append((nx, ny, cnt+1))

    return -1

print(bfs())