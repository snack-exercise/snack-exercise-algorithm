import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 물건 수, 버틸 수 있는 무게
arr = [(0, 0)] + [tuple(list(map(int, input().split()))) for _ in range(n)] # (무게, 가치)

dp = [[0] * (k+1) for _ in range(n+1)] # dp[i][j]는 i번째 물건까지 봤을때, 견딜 수 있는 무게가 j인 경우 최대 value

for i in range(1, n+1):
    weight, value = arr[i]
    for j in range(1, k+1):
        # 새로 추가될 물건의 무게가, 견딜 수 있는 무게보다 크다면, 이전 물건까지의 값을 이어 받는다.
        if weight > j:
            dp[i][j] = dp[i-1][j]
        else:
            # 새로운 물건을 담아 value를 얻는 것과 이전 물건까지 계산했던 value 중에서 더 큰 것을 택함
            dp[i][j] = max(dp[i-1][j-weight] + value, dp[i-1][j])

print(dp[n][k])

