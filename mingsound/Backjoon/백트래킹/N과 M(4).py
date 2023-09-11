def dfs():
    if len(s) == m:
        print(" ".join(list(map(str, s))))
        return

    for i in range(1, n+1):
        if len(s) != 0 and s[-1] > i: # s가 비어있지 않은데, 가장 마지막에 있는 것보다 작으면, 오름차순 아님
            continue

        s.append(i)
        dfs()
        s.pop()


n, m = map(int, input().split())
s = []

dfs()