# 뒤에 글자를 추가해서 앞 뒤 대칭되는 문자열 만들기

# 맨 뒤에 문자열을 추가하니까, 대칭되는 문자열의 가장 늦은 시작 위치 앞에 있는 것들만큼 뒤에 붙여야한다.

answer = 0
str = input()


def check(start):
    idx = -1
    for i in range(start, len(str)):
        if str[i] != str[idx]:
            return False
        idx -= 1

    return True


for i in range(len(str)):
    if check(i):
        answer = len(str) + i
        break

print(answer)

### 인터넷에서 찾은 정답

# 부분 문자열이 펠린드롬(대칭 문자열)이 되기까지의 왼쪽 문자열 개수 만큼의 길이를 원래 길이에 더해주면 됨
s = input()

for i in range(len(s)):
    if s[i:] == s[i:][::-1]: # s[i:]를 하나의 새로운 문자열로 생성, [::-1] 거꾸로배열
        print(len(s) + i)
        break

### 문자열 skill
# 1. 문자열 슬라이싱으로 부분 문자열 만들기
# 2. [::-1] 거꾸로 배열