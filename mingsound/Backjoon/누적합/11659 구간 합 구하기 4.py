n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr = [0] + arr
for i in range(2, n+1):
    arr[i] += arr[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(arr[j] - arr[i-1])

# prefix sum으로 시간복잡도는 O(n+m)

