n, m = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
answer = 0
sum = 0
while right < n:
    if sum + arr[right] > m:
        sum -= arr[left]
        left += 1
    elif sum + arr[right] == m:
        answer += 1
        sum -= arr[left]
        left += 1
    else:
        sum += arr[right]
        right += 1


print(answer)

