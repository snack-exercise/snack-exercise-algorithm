n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = 0

def getValue(arr, target):
    value = 0
    for a in arr:
        if a > target:
            value += (a - target)
    return value


def binary_search(arr, start, end):
    global answer
    while start <= end:
        mid = (start + end) // 2

        if getValue(arr, mid) >= m:
            answer = max(answer, mid)
            start = mid + 1
        else:
            end = mid - 1
    

binary_search(arr, 0, max(arr))
print(answer)