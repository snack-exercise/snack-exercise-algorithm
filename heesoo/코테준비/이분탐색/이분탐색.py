import bisect

def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return None

arr = [100, 100, 200, 300]

print(bisect.bisect_left(arr, 0))
print(bisect.bisect_left(arr, 150))
print(bisect.bisect_left(arr, 350))
print(bisect.bisect_left(arr, 100))
print(bisect.bisect_right(arr, 100))
print(bisect.bisect_right(arr, 0))
print(bisect.bisect_right(arr, 150))
print(bisect.bisect_right(arr, 350))
