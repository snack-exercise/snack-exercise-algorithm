N, M, x, y, K = map(int, input().split()) # 세로, 가로, 좌표, 명령 개수

graph = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split())) # 명령어

# 위쪽, 뒤쪽, 오른쪽, 왼쪽, 앞쪽, 바닥
dice = [0,0,0,0,0,0] # [1, 2, 3, 4, 5, 6]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def turn(dir):기
    global dice
    a, b, c, d, e, f = dice

    if dir == 1: # 동
        dice = [d, b, a, f, e, c] # [4, 2, 1, 6, 5, 3]
    elif dir == 2: # 서
        dice = [c, b, f, a, e, d] # [3, 2, 6, 1, 5, 4]
    elif dir == 3: # 북
        dice = [e, a, c, d, f, b] # [5, 1, 3, 4, 6, 2]
    elif dir == 4: # 남
        dice = [b, f, c, d, a, e] # [2, 6, 3, 4, 1, 5]


nx, ny = x, y
for c in cmd:
    nx += dx[c-1]
    ny += dy[c-1]

    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        nx -= dx[c-1]
        ny -= dy[c-1]
        continue

    turn(c)

    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[-1]
    else:
        dice[-1] = graph[nx][ny]
        graph[nx][ny] = 0
    print(dice[0])


# 이동한 칸이 0이면, 주사위의 바닥면의 숫자가 칸에 적힘
# 이동한 칸이 0이 아니면, 칸의 숫자가 주사위의 바닥면에 적힘, 바닥은 0으로 변경

# 주사위가 이동했을때 마다 상단에 쓰여있는 값을 구하기


# key point : 주사위의 모습을 리스트에 저장
# 방향 dx, dy 제대로 설정