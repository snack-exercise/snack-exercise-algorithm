import bisect
t=int(input())
n=int(input())
arrA=list(map(int,input().split()))
m=int(input())
arrB=list(map(int,input().split()))

sumA=[]
sumB=[]

# 각 배열의 합 나올 수 있는 것 다 넣음
for i in range(n):
    num=arrA[i]
    sumA.append(num)
    for j in range(i+1,n):
        num+=arrA[j]
        sumA.append(num)

for i in range(m):
    num=arrB[i]
    sumB.append(num)
    for j in range(i+1,m):
        num+=arrB[j]
        sumB.append(num)


sumA.sort()
sumB.sort()
ans=0
# sumB + sumA = t
# sumB = t - sumA
for i in range(len(sumA)):
    l=bisect.bisect_left(sumB,t-sumA[i])
    r=bisect.bisect_right(sumB,t-sumA[i])
    ans+=(r-l)

print(ans)