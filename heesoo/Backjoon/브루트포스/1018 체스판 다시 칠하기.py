n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
cnt = []

for a in range(n-7):
    for b in range(m-7):
        wstart = 0 
        bstart = 0 
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        wstart += 1
                    if board[i][j] != 'B':
                        bstart += 1
                else:
                    if board[i][j] != 'B':
                        wstart += 1
                    if board[i][j] != 'W':
                        bstart += 1
        cnt.append(min(wstart, bstart))
print(min(cnt))