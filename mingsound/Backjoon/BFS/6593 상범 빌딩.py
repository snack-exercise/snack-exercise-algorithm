import sys
input = sys.stdin.readline
from collections import deque



dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while deq:
        x, y, z = deq.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < R and 0 <= ny < C and 0 <= nz < L and not visited[nz][nx][ny] and graph[nz][nx][ny] != '#':
                visited[nz][nx][ny] = visited[z][x][y] + 1
                deq.append((nx, ny, nz))
                if graph[nz][nx][ny] == 'E':
                    return visited[z][x][y]
    return 0

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    graph = []
    for j in range(L):
        graph.append([list(input().rstrip()) for i in range(R)])
        input()

    visited = [[[0] * C for _ in range(R)] for _ in range(L)]

    deq = deque([])
    for k in range(L):
        for i in range(R):
            for j in range(C):
                if graph[k][i][j] == 'S':
                    deq.append((i, j , k))
                    visited[k][i][j] = 1

    answer = bfs()

    if answer == 0:
        print('Trapped!')
    else:
        print('Escaped in %d minute(s).' %(answer)) # minutes(s). 라고 해서 해맸다.... 이런 단순 문자열 실수가 있을 수 있군...

# 3차원 문제
# BFS를 수행해, visited에 해당 위치에 도달한 시각을 기록, E에 도달할 수 있다면, 시간 출력
# 도달할 수 없다면 trapped를 출력

# 주의 입력받을 때 중간에 한줄 띄어쓰기가 있어, 입력 받을 때 신경을 써야했다.
