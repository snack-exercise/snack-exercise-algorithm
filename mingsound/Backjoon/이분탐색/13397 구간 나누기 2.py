# 이분탐색의 기준을 구간의 점수의 최댓값으로 설정!!
# 파라메트릭 서치 : 특정 범위안에서 원하는 조건에 부합하는 값 찾기
# 이분탐색 : 특정 범위안에서 특정 값 찾기
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))


def check(answer):
    cnt = 1
    _min = arr[0]
    _max = arr[0]

    for i in range(n):
        _min = min(_min, arr[i])
        _max = max(_max, arr[i])

        if _max - _min > answer:
            cnt += 1
            _min = _max = arr[i]
    return m >= cnt


left = 0
right = max(arr)
answer = max(arr)

while left <= right:
    mid = (left + right) // 2 # mid = 배열에서 구간의 점수의 최댓값
    # mid 값이 커질수록, 구간의 개수가 줄어든다. mid를 최소로 만들어야함.

    if check(mid): # 현재의 mid 값으로는 구간이 충분히 적다면, mid 값을 줄여도 m이하의 구간으로 나눌 수 있는지 판단
        answer = min(mid, answer)
        right = mid - 1
    else: # 현재의 mid 값으로는 m이하의 구간의 개수를 맞출 수 없다면, mid의 값을 키우기
        left = mid + 1

print(answer)