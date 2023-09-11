def dfs():
    if len(s) == m: # m개를 모두 택했다면
        print(' '.join(map(str, s))) # 출력
        return

    # 백트래킹 핵심 구조
    for i in range(1, n+1):
        if visited[i]:# 아직 i가 사용되지 않았다면
            continue # 계속
        visited[i] = True
        s.append(i)
        dfs() # 다음 수를 고르러 한 단계 더 들어감
        s.pop() # 백 트래킹, 다 확인했으니까 마지막꺼
        visited[i] = False

n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

dfs()