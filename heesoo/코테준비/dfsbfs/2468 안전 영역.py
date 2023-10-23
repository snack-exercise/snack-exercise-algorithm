from collections import deque
n = int(input())
board = []
max_val = 0
for i in range(n):
    arr = list(map(int, input().split()))
    board.append(arr)
    arr.append(max_val)
    max_val = max(arr)


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def check_num(x, y, val, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 > nx or n <= nx or 0 > ny or n <= ny:
                continue

            if visited[nx][ny] == 0 and board[nx][ny] - val > 0:
                q.append((nx, ny))
                visited[nx][ny] = 1

def check_all(board):
    max_ans = 0
    for k in range(max_val):
        visited = [[0 for _ in range(n)] for _ in range(n)]
        num = 0
        for i in range(n):
            for j in range(n):
                if board[i][j] - k > 0 and visited[i][j] == 0:
                    check_num(i, j, k, visited)
                    num += 1
        max_ans = max(max_ans, num)
    return max_ans


print(check_all(board))

