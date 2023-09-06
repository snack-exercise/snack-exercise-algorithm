import heapq
import sys
n=int(input())

heap=[]

for _ in range(n):
    num=int(sys.stdin.readline().rstrip())
    if num!=0:
        heapq.heappush(heap,(abs(num),num))
        print(heap)
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
