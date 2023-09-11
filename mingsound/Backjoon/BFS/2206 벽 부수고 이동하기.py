import sys
input = sys.stdin.readline
from collections import deque

# 그냥 단순 생각으로는 벽이 있는 모든 곳에 대해서 하나하나 벽을 제거하고 bfs를 돌린뒤에 최소 값을 출력하고 싶은데,, 그러면 10^9가 될 수도 있다.
n, m = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]

visited = [[[0] * m for _ in range(n)] for _ in range(2)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(crush, x, y):
    queue = deque()
    queue.append(([crush, x, y])) # 큐에 이전에 벽 부순적이 있는지 여부도 같이 담는다. -> 이유는 벽을 부순적이 있는 경우와 없는 경우를 별도로 세기 위해서
    visited[crush][x][y] = 1

    while queue:
        crush, x, y = queue.popleft()

        if x == n-1 and y == m-1:
            return visited[crush][x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[crush][nx][ny]: # bfs에서 이미지 방문한 곳이라는 것은 더 빨리 도착할 수 있는 경우가 있었다는 것
                if crush == 0 and graph[nx][ny] == 1: # 벽을 부순적이 없고, 다음 좌표가 벽이라면
                    queue.append((1, nx, ny)) # 벽을 부순경우로 체크하고
                    visited[1][nx][ny] = visited[crush][x][y] + 1 # 현재위치까지의 최솟값 + 1 을 벽을 부순 visited의 현재 좌표에 저장
                elif graph[nx][ny] == 0: # 다음 좌표가 벽이 아니라면
                    queue.append((crush, nx, ny))
                    visited[crush][nx][ny] = visited[crush][x][y] + 1 # 현재 위치까지의 최솟값 + 1을 crush 여부의 visited의 현재 좌표에 저장
    return -1

print(bfs(0, 0, 0))