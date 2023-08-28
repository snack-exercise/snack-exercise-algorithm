# upper bound 사용

import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def bisect_upper(x, s, arr):
    start = 0
    end = len(arr) - 1

    while(start <= end):
        mid = (start + end) // 2

        if arr[mid] <= x:
            start = mid + 1
        else:
            end = mid - 1
    return start

answer = []
for idx, a in enumerate(A):
    answer.append(bisect_upper(a, idx, B) - idx - 1)
    answer.append(bisect.bisect_right(B, a) - idx - 1)

print(*answer)