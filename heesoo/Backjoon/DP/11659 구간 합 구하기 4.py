import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int,input().split()))
    
for i in range(1, len(arr)):
    arr[i] += arr[i - 1]
arr = [0] + arr
for _ in range(m):
    a, b = map(int, input().split())
    print(arr[b] - arr[a - 1])