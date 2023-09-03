import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

# 처음 지훈 위치와 불의 위치 파악
person = deque([])
fires = deque([])
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            person.append((i, j))
        elif graph[i][j] == 'F':
            fires.append((i, j))


# 1초마다 불 먼저 번지고, 지훈이 이동 가능한 위치 모두 탐색, 만약 가장자리에 하나라도 도달했다면 시간 출력, 큐에 아무것도 없다면 불가능 출력
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * c for _ in range(r)]
sx, sy = person[0]
visited[sx][sy] = 1

answer = 0

# 처음에 가장자리에 지훈이 위치한 경우
if sx in [0, r - 1] or sy in [0, c - 1]:
    print(1)
    exit(0)

while True:
    temp_fires = deque([])

    while fires:
        x, y = fires.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in ['#', 'F']:
                graph[nx][ny] = 'F'
                temp_fires.append((nx, ny))

    fires = temp_fires

    temp_person = deque([])
    while person:
        x, y = person.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                temp_person.append((nx, ny))
                if nx in [0, r-1] or ny in [0, c-1]:
                    answer = visited[nx][ny]

    if answer != 0:
        break

    person = temp_person
    if not person:
        break

if answer == 0:
    print("IMPOSSIBLE")
else:
    print(answer)


# 다만, 이 문제는 지훈이의 이동은 불의 전파에 영향을 받지만, 불은 지훈이의 이동에 영향을 받지 않기에, 불만 전파를 쫙 먼저 할 수 있었다.
# 하지만, A의 전파가 B에 영향을 주고, B의 전파가 A의 영향을 주는 상황이라면? ex. 불과 물이 만나면 어떤 새로운 상황이 된다.
# -> 백준 18809 (BFS + 백트래킹)
# 그런 경우에는 시간 순으로 A와 B를 동시에 진행시켜야한다.