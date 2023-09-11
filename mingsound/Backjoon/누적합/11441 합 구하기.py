import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr = [0] + arr
for i in range(2, n+1):
    arr[i] += arr[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(arr[j]-arr[i-1])

# sys.stdin.readline과 sys.stdout.write를 사용하면 빠른 입출력이 가능하다.
# 특히, 반복문으로 여러줄 입력을 받아야하는 경우, input으로 데이터를 받으면 시간초과 가능성이 있다.
# sys.stdin.readline은 한줄단위로 입력받아서, 개행문자('\n')까지 같이 받아짐. rstrip()을 사용해서 개행문자, 공백문자 제거 필요.