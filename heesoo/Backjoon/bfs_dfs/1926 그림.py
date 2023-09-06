from collections import deque

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(graph,a,b):
    print(graph,a,b)
    q=deque()
    q.append((a,b))
    graph[a][b]=0
    cnt=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1:
                    graph[nx][ny]=0
                    q.append((nx,ny))
                    cnt+=1
    return cnt

paint=[]
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            paint.append(bfs(arr,i,j))

print(len(paint))
if len(paint)==0:
    print(0)
else:
    print(max(paint))