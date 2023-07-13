s=input()

# 팰린드롬인 문자열 제외하고 나머지 문자열 길이 더하기
for i in range(len(s)):
    if s[i:]==s[i:][::-1]: 
        print(len(s)+i)
        break