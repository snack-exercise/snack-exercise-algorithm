import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

# 처음 지훈 위치와 불의 위치 파악
person = deque([])
fires = deque([])
visited_person = [[False] * c for _ in range(r)]
visited_fire = [[False] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            person.append((i, j))
            visited_person[i][j] = 1
        elif graph[i][j] == 'F':
            fires.append((i, j))
            visited_fire[i][j] = 1



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



# 처음에 가장자리에 지훈이 위치한 경우
sx, sy = person[0]
if sx in [0, r - 1] or sy in [0, c - 1]:
    print(1)
    exit(0)

# 불에 대해서 bfs
while fires:
    x, y = fires.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in ['#', 'F'] and not visited_fire[nx][ny]:
            visited_fire[nx][ny] = visited_fire[x][y] + 1
            fires.append((nx, ny))


# 사람에 대해서 bfs
answer = 0
while person:
    x, y = person.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.' and (visited_person[x][y] + 1 < visited_fire[nx][ny] or visited_fire[nx][ny] == 0) and not visited_person[nx][ny]: # or visited_fire[nx][ny] == 0 <- 처음에 이거 고려 안해서 틀림
            visited_person[nx][ny] = visited_person[x][y] + 1
            person.append((nx, ny))
            if nx in [0, r - 1] or ny in [0, c - 1]:
                print(visited_person[nx][ny])
                exit(0)


print("IMPOSSIBLE")


