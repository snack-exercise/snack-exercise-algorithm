import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

visited = [-1] * 100001


def bfs():

    deq = deque([(n, 0)])
    visited[n] = n

    while deq:
        now, cnt = deq.popleft()

        if now == k:
            return cnt

        next = now * 2
        if 0 <= next < 100001 and visited[next] == -1 and next != 0:
            visited[next] = now # 방문처리 대신, 이전에 방문한 위치를 저장
            deq.append((next, cnt + 1))

        for dx in [-1, 1]:
            next = now + dx
            if 0 <= next < 100001 and visited[next] == -1:
                visited[next] = now
                deq.append((next, cnt + 1))


print(bfs())

route = [k]
while k != n:
    route.append(visited[k])
    k = visited[k]
print(*route[::-1])

# https://www.acmicpc.net/board/view/125156 <- 메모리 초과 해결...
