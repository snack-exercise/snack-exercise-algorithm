import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
val = list(map(int, input().split()))
arr = [0] * 6

# 우, 좌, 상, 하
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for v in val:
    nx = x + dx[v]
    ny = y + dy[v]

    if not 0 <= nx < n or not 0 <= ny < m: 
        continue

    rd, ld, sd, nd, ud, bd = arr[0],  arr[1], arr[2], arr[3], arr[4], arr[5]

    if v == 1:
        arr[0], arr[1], arr[4], arr[5] = bd, ud, rd, ld
    elif v == 2:
        arr[0], arr[1], arr[4], arr[5] = ud, bd, ld, rd
    elif v == 3:
        arr[2], arr[3], arr[4], arr[5] = ud, bd, nd, sd
    elif v == 4:
        arr[2], arr[3], arr[4], arr[5] = bd, ud, sd, nd

    if maps[nx][ny] == 0:
        maps[nx][ny] = arr[5] # 0이면 bottom
    else:
        arr[5] = maps[nx][ny]
        maps[nx][ny] = 0

    x, y = nx, ny
    print(arr[4]) # 위방향
