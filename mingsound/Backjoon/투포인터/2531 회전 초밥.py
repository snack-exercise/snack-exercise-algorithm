import sys
from collections import deque

input = sys.stdin.readline

n, d, k, c = map(int, input().split()) # 접시수, 초밥 가짓수, 연속접시수, 쿠폰번호
arr = [int(input()) for _ in range(n)]

deq = deque(arr[0:k])
_max = 0
_max = max(_max, len(set(deq) | set([c])))
for i in range(n):
    _max = max(_max, len(set(deq) | set([c])))
    deq.popleft()
    deq.append(arr[(i+k)%n])

print(_max)


# 투포인터를 사용한 슬라이딩 도어(개수는 k개씩으로 지정됨), set말고, dict를 사용하면 더 편하게 풀 수 이쏙, defaultdict(int)사용시 초기화 코드 필요 없음.
