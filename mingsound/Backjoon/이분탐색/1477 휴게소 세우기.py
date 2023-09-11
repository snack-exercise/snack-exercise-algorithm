import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
arr = [0] + list(map(int, input().split())) + [L]


start, end = 1, L-1
result = 0
while start <= end:
    count = 0
    mid = (start + end) // 2 # 가장 멀리 떨어져있는 휴게소 사이 거리
    for i in range(1, len(arr)):
        # 현재 거리 중에서 mid보다 큰 거리를 찾아서
        if arr[i] - arr[i-1] > mid:
            count += (arr[i] - arr[i-1] - 1) // mid

    if count > M: # 목표보다 너무 많이 설치했다면, 멀리 떨어져있는 휴게소 사이 거리 늘리기
        start = mid + 1
    else: # 예비 정답
        end = mid - 1
        result = mid

print(result)

# 이분탐색 - 파라메트릭 서치
# 최적화 문제(문제의 상황을 만족하는 특정 변수의 최소, 최대값을 구하는 문제)를 결정 문제로 바꾸어 푸는것
# 범위 내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제의 경우 전형적인 파라메트릭 서치
# 이분탐색으로 풀 수 있는 문제라는 것을 파악조차 못함
