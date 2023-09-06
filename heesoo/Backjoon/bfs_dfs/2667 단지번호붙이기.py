from collections import deque
n=int(input())
board=[[int(char) for char in input()] for _ in range(n)]

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs(a,b,board):
    cnt=0
    q=deque()
    q.append((a,b))
    board[a][b]=0
    
    while q:
        x,y=q.popleft()
        cnt+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0>nx or nx>=n or 0>ny or ny>=n:
                continue

            if board[nx][ny]==1:
                board[nx][ny]=0
                q.append((nx,ny))
    return cnt


ans=[]
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            ans.append(bfs(i,j,board))

print(len(ans))
ans.sort()
for i in ans:
    print(i)