from collections import deque 

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs(x,y):
    q=deque()
    q.append((x,y))

    while q:
        a,b=q.popleft()

        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]

            if 0>nx or nx>=n or 0>ny or ny>=m:
                continue

            if board[nx][ny]==1:
                q.append((nx,ny))
                board[nx][ny]=0


t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())

    board=[[0 for _ in range(m)] for _ in range(n)]
    for i in range(k):
        a,b=map(int,input().split())
        board[a][b]=1

    cnt=0
    for i in range(n):
        for j in range(m):
            if board[i][j]==1:
                bfs(i,j)
                cnt+=1

    print(cnt)
