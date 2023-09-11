import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

left, right = 0, 0
_min = sys.maxsize
while right < n and left < n:
    if arr[right] - arr[left] >= m:
        _min = min(_min, arr[right]-arr[left])
        left += 1
    else:
        right += 1

print(_min)