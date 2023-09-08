import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
MAX = 100001
visited = [False] * MAX
dist = [-1] * MAX

q = deque()
q.append(n)
visited[n] = True
dist[n] = 0

dx = [-1, 1]
while q:
    now = q.popleft()
    if now == k: # 목표 도달
        break

    next = now * 2
    if 0 <= next < MAX and not visited[next]:
        q.appendleft(next) # 우선순위가 높으니까 왼쪽
        visited[next] = True
        dist[next] = dist[now]

    for i in range(2):
        next = now + dx[i]
        if 0 <= next < MAX and not visited[next]:
            q.append(next)
            visited[next] = True
            dist[next] = dist[now] + 1

print(dist[k])

# 우선순위에 따라서 왼쪽에 넣을수가 있군