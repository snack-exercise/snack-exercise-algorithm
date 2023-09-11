from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().split()))

_dict = defaultdict(int)
left , right = 0, 0
_max = 0
_dict[arr[0]] += 1
while right < n-1:
    if _dict[arr[right+1]] + 1 > k:
        _dict[arr[left]] -= 1
        left += 1

    else:
        right += 1
        _max = max(right-left + 1, _max)
        _dict[arr[right]] += 1

print(_max)