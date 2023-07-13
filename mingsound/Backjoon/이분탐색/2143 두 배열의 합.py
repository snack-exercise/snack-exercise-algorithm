import bisect

T = int(input())
n = int(input()) # <= 1000
arrA = list(map(int, input().split()))
m = int(input())
arrB = list(map(int, input().split()))

def calcSubSum(length, subArr):
    for i in range(length-1):
        for j in range(i+2, length+1):
            subArr.append(sum(subArr[i:j]))

subA = [a for a in arrA]
calcSubSum(n, subA)
subA.sort()

subB = [b for b in arrB]
calcSubSum(m, subB)
subB.sort()

answer = 0
for a in subA:
    target = T - a
    left = bisect.bisect_left(subB, target) # target의 가장 왼쪽 인덱스
    right = bisect.bisect_right(subB, target) # target의 가장 오른쪽 인덱스 + 1
    answer += right - left

print(answer)


# 만약에 해당 값이 arr에 없다면, 들어가야 할 자리의 인덱스를 반환
testArr = [1, 2, 3, 3, 6, 6]

print(bisect.bisect_left(testArr, -10)) # 0
print(bisect.bisect_left(testArr, -10)) # 0

print(bisect.bisect_left(testArr, 5)) # 4
print(bisect.bisect_right(testArr, 5)) # 4






