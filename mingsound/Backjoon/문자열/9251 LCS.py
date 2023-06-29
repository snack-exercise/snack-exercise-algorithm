str1 = ' ' + input()
str2 = ' ' + input()

# dp[i][j] = str1[i], str[j]까지의 최장 공통 부분 문자열의 길이

dp = [[0] * len(str2) for _ in range(len(str1))]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1 # str[i-1]과 str2[j-1]의 최장 공통 부분 문자열의 길이 + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            # 이번에 새로 추가된 문자열이 다르다고해서 dp[i-1][j-1]의 값을 가져오면 안됨
            # 각 문자열의 마지막 글자들이 따로 한 글자씩 추가되었을 때의 LCS 중 큰 값을 가져와야함
print(dp[-1][-1])



