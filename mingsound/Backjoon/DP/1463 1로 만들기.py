# DP는 1. 테이블 정의하기, 2. 점화식 찾기 3. 초기값 정의하기
x = int(input())
dp = [0] * (x+1) # 1. 테이블 정의 : dp[x] 는 x로 만들기 위한 최소 계산 횟수

dp[0] = dp[1] = 0 # 3. 초기값 정의하기
for i in range(2, x+1):
    # 2. 점화식 dp[x] = min(dp[x-1], dp[x // 2] , dp[x // 3]) + 1
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[x])