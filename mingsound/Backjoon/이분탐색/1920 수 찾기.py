import sys
input = sys.stdin.readline

n = int(input())
arr_n = sorted(list(map(int, input().split())))
m = int(input())
arr_m = list(map(int, input().split()))
def binary_search(x):
    left, right = 0, n-1

    while left <= right:
        mid = (left + right) // 2

        if arr_n[mid] == x:
            return 1

        if arr_n[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for i in range(m):
    print(binary_search(arr_m[i]))

# 이분탐색 안하면, 10^10 = 시간초과
# 이분탐색 하면, 15 * 15 = 시간 OK
# 주의) 이분탐색은 정렬된 배열에 대해서만 가능