# A 에너지 + B 에너지 = A x B 에너지 슬라임
# 합성시 A x B 만큼의 에너지 필요

# 각 합성 단계마다 필요한 전기 에너지 모두 곱한 값이 최소가 되도록
# 작은 에너지들끼리 먼저 곱해야함
import heapq
import sys
input = sys.stdin.readline

def using_min_heap():
    global slime

    # 최소힙 생성
    heapq.heapify(slime) # O(logN)

    # h에 원소가 1개가 될 때까지 계속해서 작은거 2개 꺼내서 곱하고, answer에 곱하고, 다시 h에 넣음
    answer = 1
    while len(slime) > 1:
        a = heapq.heappop(slime)
        b = heapq.heappop(slime)  # O(logN)
        answer = answer * a * b % 1000000007
        heapq.heappush(slime, a * b)

    print(answer % 1000000007)


for _ in range(int(input())):
    N = int(input())  # 최대 60
    slime = list(map(int, input().split()))  # 슬라임 에너지

    using_min_heap()
