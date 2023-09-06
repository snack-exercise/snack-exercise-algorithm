n,k=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))

idx=len(arr)-1
ans=0
while k>0 :
    if arr[idx]<=k:
        val=k//arr[idx]
        k-=(val * arr[idx])
        ans+=val
        idx-=1
    else:
        idx-=1
print(ans)