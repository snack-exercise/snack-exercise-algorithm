# 거꾸로 생각
# S -> T로 변경하라고 했을 때, T -> S로 변경하는 것이 더 쉽지 않은지 생각해봐야겠다.
# len(str2) > len(str1)인 동안
# 1. 맨 뒤가 A라면 A제거
# 2. 맨 뒤가 B라면 B제거 후 문자열 뒤집기

# 만약 str1 == str2 라면 1, 아니라면 0

str1 = input()
str2 = input()

while(len(str2) > len(str1)):
    if str2[-1] == 'A':
        str2 = str2[:-1]
    else:
        str2 = str2[-2::-1]

if str1 == str2:
    print(1)
else:
    print(0)