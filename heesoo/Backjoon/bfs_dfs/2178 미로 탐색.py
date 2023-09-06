from collections import deque

n,m=map(int,input().split())
board=[[int(char) for char in input()] for _ in range(n)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

ans_list=[]

def check(graph, a, b):
    q=deque()
    q.append((a,b))

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0>nx or n<=nx or 0>ny or m<=ny:
                continue

            if graph[nx][ny]==0:
                continue

            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                q.append((nx,ny))
                print(nx,ny,graph)
    
    return graph[n-1][m-1]

ans = check(board, 0, 0)
print(ans)
print(board) 