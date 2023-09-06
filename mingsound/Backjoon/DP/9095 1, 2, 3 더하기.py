arr = []
for _ in range(int(input())):
    arr.append(int(input()))

dp = [0] * (max(arr) + 1) # 1. 테이블 정의 : dp[i]는 i를 1, 2, 3의 합으로 나타내는 방법의 수

# 2. 점화식 dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
# 3. 초기값
dp[1] = 1
dp[2] = dp[1] + 1
dp[3] = dp[2] + dp[1] + 1

for i in range(4, max(arr)+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for a in arr:
    print(dp[a])