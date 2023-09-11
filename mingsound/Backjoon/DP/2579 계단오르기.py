import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1) # 1. 테이블정의 : dp[i]는 i번째 계단까지의 최대 점수

# 2. 점화식 dp[i] = max(arr[i] + arr[i-1] + dp[i-3], arr[i] + dp[i-2])
# 3. 초기값 정의
# dp[1] = arr[1]
#
# for i in range(2, n+1):
#     dp[i] = max(arr[i] + arr[i-1] + dp[i-3], arr[i] + dp[i-2])
#
# print(dp[n])



