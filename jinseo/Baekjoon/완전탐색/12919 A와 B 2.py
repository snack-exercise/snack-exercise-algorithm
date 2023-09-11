s = input()
t = input()

ans = 0

# 첫 문자 끝 문자 다양한 경우의 수가 존재하므로 모든 경우의 수를 탐색해야 함

def dfs(s, t):
    if s == t:
        return 1
    
    if len(s) >= len(t):
        return 0
    
    ans = 0
    if t[-1] == 'A':
        ans = dfs(s, t[:-1])
    if ans == 1: return 1

    if t[0] == 'B':
        t = list(t)
        t.reverse()
        t = ''.join(t)
        ans = dfs(s, t[:-1])
    return ans


print(dfs(s,t))