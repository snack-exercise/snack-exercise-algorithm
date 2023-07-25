# 게임 횟수를 한 개씩 늘려가면서 Z가 변화하는 때를 찾으려고하면 시간초과
# 따라서 이분 탐색 사용

x, y = map(int, input().split())
z = y * 100 // x
start = 0
end = x
ans = x

if z > 98: # 100은 완전한 %라서 99에서 100은 만들 수 없다.
    print(-1)
    exit(0)
else:
    while start <= end:
        mid = (start + end) // 2
        newZ = (y + mid) * 100 // (x + mid)

        if newZ != z:
            end = mid - 1
            ans = mid
        else:
            start = mid + 1
    print(ans)
