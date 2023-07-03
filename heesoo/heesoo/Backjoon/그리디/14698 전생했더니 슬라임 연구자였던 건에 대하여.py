# 시간초과
# 문풀참고
import heapq

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int, input().split()))

    ans=1
    if n==1:
        print(1)
        continue 

    hq=[]
    for val in arr:
        heapq.heappush(hq,val)

    while len(hq)>1:
        nextval = heapq.heappop(hq)*heapq.heappop(hq)
        ans*=nextval
        heapq.heappush(hq,nextval)

    print(ans%1000000007)