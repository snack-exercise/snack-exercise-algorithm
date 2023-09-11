import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)

answer = arr[0]
for i in range(n):
    answer = max(answer, (i+1)*arr[i])
print(answer)
