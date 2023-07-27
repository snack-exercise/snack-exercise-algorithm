# 25개 위치에 n개 놓을 수 있는 경우의 수 다 구함
# 위 경우의 수에서 다 연결되어 있는 상태인지 구함
# 연결되어 있으면 현재 위치에서 해당 경우 만들 수 있는 최솟값 구함

from collections import deque
from itertools import combinations, permutations
board = [list(map(str, input().strip()))for _ in range(5)]

# * 개수, 위치
starcnt = 0
starpos = []
for i in range(5):
    for j in range(5):
        if board[i][j] == '*':
            starcnt += 1
            starpos.append((i, j))

# * 넣을 수 있는 보드의 모든 위치 조합
allarr = []
for i in range(5):
    for j in range(5):
        allarr.append((i, j))
stararr = list(combinations(allarr, starcnt))

# 인접한 좌표 확인 방향
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def isConnected(x, y, arr, size):
    global cnt
    q = deque()
    q.append((x, y))
    visit = [[True for _ in range(5)] for _ in range(5)]
    visit[x][y] = False
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            kx = dx[i] + cx
            ky = dy[i] + cy
            if 0 <= kx < 5 and 0 <= ky < 5 and visit[kx][ky] and (kx, ky) in arr:
                visit[kx][ky] = False
                cnt += 1
                q.append((kx, ky))
    # 모든 * 인접하면
    if cnt == size:
        return True
    else:
        False

P = list(permutations(starpos, starcnt))
res = 25

for arr in stararr:
    cnt = 1
    if isConnected(arr[0][0], arr[0][1], arr, len(arr)):
        for canstar in P:
            tmp = 0
            # 모든 * 위치로 이동할 때 최소 움직임 횟수 구함
            for idx, data in enumerate(canstar):
                x, y = data
                x1, y1 = arr[idx]
                tmp += abs(x1-x) + abs(y1-y)
            res = min(res, tmp)
    else:
        continue

print(res)