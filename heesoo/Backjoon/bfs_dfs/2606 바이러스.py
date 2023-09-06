from collections import deque
n=int(input())
e=int(input())
board=[[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(e):
    a,b=map(int,input().split())
    board[a][b]=1
    board[b][a]=1

visited=[0 for _ in range(n+1)]
visited2=[0 for _ in range(n+1)]

q=deque()
q.append(1)
cnt=0
cnt2=0

while q:
    v=q.popleft()
    visited[v]=1
    for i in range(1,n+1):
        if board[v][i]==1 and visited[i]==0:
            cnt+=1
            q.append(i)
            visited[i]=1

def dfs(v):
    global cnt2
    visited2[v]=1
    for i in range(1,n+1):
        if board[v][i]==1 and visited2[i]==0:
            cnt2+=1
            visited2[i]=1
            dfs(i)
    
print(cnt)
dfs(1)
print(cnt2)