# def binary_search(target, data):
#     data.sort()

#     start = 0
#     end = len(data) - 1

#     while start <= end:
#         mid = (start + end) // 2
#         if data[mid] == target:
#             return mid
#         if data[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
    
#     return None

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
answer = 0

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        cur = arr[0]
        cnt = 1

        for i in range(1, len(arr)):
            if arr[i] - cur >= mid:
                cnt += 1
                cur = arr[i]

        if cnt >= c:
            global answer
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

start = 1
end = arr[-1] - arr[0]
binary_search(arr, start, end)
print(answer)





