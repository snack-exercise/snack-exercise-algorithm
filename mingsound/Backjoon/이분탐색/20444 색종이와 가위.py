n, k = map(int, input().split())

# 색종이의 개수 = (row_cut + 1) * (col_cut + 1)
# row_cut + col_cut = n

left = 0
right = n // 2 # 최대 일 때는 row_cnt == n//2 일떄

while left <= right:
    mid = (left + right) // 2

    cnt = (mid + 1) * (n - mid + 1)

    if cnt == k:
        print('YES')
        exit(0)
    elif cnt < k:
        left = mid + 1
    else:
        right = mid - 1

print('NO')

