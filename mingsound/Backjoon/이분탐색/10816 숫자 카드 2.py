import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
check_nums = list(map(int, input().split()))


def lower_bound(arr, target):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

def upper_bound(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    return left

cards.sort()

answer = []
for num in check_nums:
    answer.append(upper_bound(cards, num) - lower_bound(cards, num))

print(*answer)
