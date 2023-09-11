N, K = map(int, input().split())
arr = list(map(int, input().split()))


# 홀수개수가 K가 되기 전까지 right 이동
# K개를 초과한 경우, max 값 비교
left, right = 0, 0
answer = 0
odd = 0
while right < N:
    if arr[right] % 2 != 0:
        odd += 1
        if odd > K:
            odd -= 1
            right -= 1
            answer = max(answer, right - left + 1 - odd)
            if arr[left] % 2 != 0:
                odd -= 1
            left += 1
    right += 1

if right == N and left == 0:
    print(right - left - odd)
else:
    print(answer)

# 짝수가 연속된 수열에서 k번의 삭제를 할 수 있다 = 최대 k개의 홀수가 담긴 배열의 크기를 찾는다.