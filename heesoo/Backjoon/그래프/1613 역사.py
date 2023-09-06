import sys
ip = sys.stdin.readline

n, k = map(int, ip().split())
arr=[[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(k):
    a,b=map(int,ip().split())
    arr[a][b]=1 # a -> b

for i in range(n+1):
    for j in range(n+1):
        for t in range(n+1):
            if arr[j][i]+arr[i][t] == 2:
                arr[j][t]=1

s=int(ip())
ans=[]
for _ in range(s):
    a,b=map(int,ip().split())
    if arr[a][b]==1:
        print(1)
        ans.append(1)
    elif arr[b][a]==1:
        print(-1)
        ans.append(-1)
    else:
        print(0)
        ans.append(0)
    
print(ans)