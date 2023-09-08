import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 각 섬 구분
def color_bfs(x, y, idx):
    deq = deque([(x, y)])
    deq2 = deque([(x, y)]) # 섬의 모든 좌표를 담은 deque
    graph[x][y] = idx

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = idx
                deq.append((nx, ny))
                deq2.append((nx, ny))

    return bfs(deq2, idx)


# 해당 섬에서 다른 섬까지의 가장 짧은 좌표
def bfs(deq2, idx):
    deq = deq2
    x, y = deq2[0]
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    answer = sys.maxsize

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]: # 범위 안에 있고, 아직 방문하지 않았다면
                if graph[nx][ny] == idx: # 같은 섬이라면 visited 1로 처리(방문표시만 하고, 거리는 증가 X)
                    visited[nx][ny] = 1 #
                    deq.append((nx, ny))
                elif graph[nx][ny] == 0: # 물이라면, visited에 거리를 +1한 값을 작성
                    visited[nx][ny] = visited[x][y] + 1
                    deq.append((nx, ny))
                else: # 다른섬을 만났다면, answer 더 작은 값으로 갱신
                    answer = min(answer, visited[x][y]-1)
    return answer

# 섬 구분
idx = 2
answer = sys.maxsize
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer = min(answer, color_bfs(i, j, idx))
            idx += 1

print(answer)


