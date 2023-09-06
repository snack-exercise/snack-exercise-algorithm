from collections import deque

n,m,v=map(int,input().split())

board=[[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    board[a][b]=1
    board[b][a]=1

visited1=[False] * (n+1)
visited2=[False] * (n+1)

def dfs(v):
    visited1[v]=True
    print(v, end=" ")
    for i in range(1,n+1):
        if not visited1[i] and board[v][i]==1:
            dfs(i)

def bfs(v):
    visited2[v]=True
    q=deque()
    q.append(v)
    while q:
        a=q.popleft()
        print(a, end=" ")
        for i in range(1,n+1):
            if not visited2[i] and board[a][i]==1:
                q.append(i)
                visited2[i]=True

dfs(v)
print()
bfs(v)