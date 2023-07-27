def palindrome(n,str):
  a = [0] * 70
  b = [0] * 70

  for i in range(2, n+1):
    l = 0
    r = l + i - 1
    c = []
    while r < n:
      # 1번, 2번, 3번 중 가장 작은 값
      c.append(min(b[l]+1, b[l+1]+1, a[l+1] + (str[l] != str[r])))
      l += 1
      r += 1
    a,b = b,c
  return b[0] # 전체 문자열 str를 팰린드롬으로 만들기 위한 최소 동작 횟수
  
str = input()
sarr = list(str)
n = len(sarr)
result = palindrome(n,sarr)

# 문자열의 각 문자를 서로 교환하면서 최소 동작 횟수 구함
for i in range(n):
  for j in range(i+1,n):
    sarr[i],sarr[j] = sarr[j],sarr[i]
    result = min(result, palindrome(n,sarr) +1)
    sarr[i],sarr[j] = sarr[j],sarr[i]

print(result)

