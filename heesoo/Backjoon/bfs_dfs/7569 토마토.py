from collections import deque
m,n,h=map(int,input().split())
answer=0
dx=[0,0,1,-1,0,0]
dy=[1,-1,0,0,0,0]
dz=[0,0,0,0,-1,1]

graph=[[] for _ in range(h)]
visited=[[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]

for i in range(n*h):
    listm=list(map(int,input().split()))
    graph[i//n].append(listm)

dq=deque()

def bfs(x,y,z,graph):
    dq=deque()
    dq.append((x,y,z))

    while dq:
        a,b,c=dq.popleft()

        for i in range(6):
            nx=a+dx[i]
            ny=b+dy[i]
            nz=c+dz[i]

            if nx<0 or nx>=h or ny<0 or ny>=n or nz<0 or nz>=m:
                continue

            if graph[nx][ny][nz]==0 and visited[nx][ny][nz]==0:
                dq.append([nx,ny,nz])
                visited[nx][ny][nz]==1
                graph[nx][ny][nz]=graph[a][b][c]+1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==1 and visited[i][j][k]==0:
                bfs(i,j,k,graph)
                visited[i][j][k]=1

for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        answer=max(answer,max(j))


print(answer-1)