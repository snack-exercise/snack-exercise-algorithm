import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [tuple(list(map(int, input().split()))) for _ in range(n)]

# 현재 시점으로부터 가장 먼저 회의가 끝나는 것을 선택하는 것이 회의실을 가장 많이 사용하게 하는 방법이다.
arr.sort(key= lambda x : (x[1], x[0]))
deq = deque(arr)

end = deq[0][1]
answer = 1
for i in range(1, n):
    if arr[i][0] >= end:
        answer += 1
        end = arr[i][1]

print(answer)


