from collections import deque

n, k = map(int, input().split())
if n == k:
    print(0)
    exit(0)

visited = [0] * 100001
visited[n] = 1
deq = deque([n])

while deq:
    x = deq.popleft()

    for nx in [x*2, x-1, x+1]:
        if nx == k:
            print(visited[x])
            exit(0)
        if 0 <= nx < 100001 and not visited[nx]: # 0 <= nx < 100000 이라고 해서 틀림...
            visited[nx] = visited[x] + 1
            deq.append(nx)

# 주의할 점
# 100000 이상으로 나갔다가 들어오는게 가장 빠른 루트 일 수 있다는 생각을 해야한다.
# 아무리 멀리가도 200000 이상을 넘어가지는 않을 것이다.
# 지금 문제는 운좋게 0과 100000 사이에서만 움직여도 되는 경우였지만, 다른 문제에서는 멋대로 100000 이상은 나가지 않을 것이다라고 가정해서 틀릴 수 있다.

