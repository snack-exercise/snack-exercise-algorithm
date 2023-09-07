import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

coin.reverse()

answer = 0
for c in coin:
    if k >= c:
        answer += k // c
        k %= c
    if k == 0:
        break

print(answer)