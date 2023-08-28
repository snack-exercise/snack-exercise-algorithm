import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
arr = [0] + arr
for i in range(2, n+1):
    arr[i] += arr[i-1]

left, right = 0, 0
answer = sys.maxsize # 최대 정수값
while left < n:
    if arr[right] - arr[left] < s:
        if right < n: # right의 최대는 n+1이므로
            right += 1
        else: # right이 가능한 최대로 옮겨졌다면, left를 한칸 뒤로 이동
            left += 1
    else:
        answer = min(answer, right-left)
        left += 1

if answer == sys.maxsize:
    print(0)
else:
    print(answer)

# 누적합과 투포인터를 사용해야하는 문제
# 누적합을 구했다고해도, 거기서 완탐으로 구간의 합이 s이상인지 판단하게되면 O(N^2)이 된다.
# 투포인터과 슬라이딩 도어의 차이는 투포인터는 포인터 2개를 사용해서 하나씩 옮겨가는 방식, 슬라이딩 도어는 고정된 길이를 움직이는 방식