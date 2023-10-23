from collections import deque
from collections import defaultdict

n, m, p = map(int, input().split())
s_arr = [0] + list(map(int, input().split()))
board = []
cnt = [0 for _ in range(p + 1)]
cas_pos = defaultdict(list)

for i in range(n):
    input_list = list(input().rstrip())
    board.append(input_list)
    for j in range(m):
        if input_list[j] != '.' and input_list[j] != '#':
            input_list[j] = int(input_list[j])
            cnt[input_list[j]] += 1
            cas_pos[input_list[j]].append([i, j])

# s_arr[i]번 만큼 돌면서 bfs 수행

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
    while True:
        flag = False
        for arr in cas_pos.values():
            if len(arr) > 0:
                flag = True
                break
        if flag == False:
            break
        
        for i in range(1, p + 1):
            for _ in range(s_arr[i]):
                q = deque(cas_pos[i])
                cas_pos.clear()

                while q:
                    x, y = q.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 > nx or n <= nx or 0 > ny or m <= ny:
                            continue
                        if board[nx][ny] == '.':
                            # cnt[i] += 1
                            board[nx][ny] = str(i)
                            cas_pos[i].append([nx, ny])


bfs()
print(cnt)