# survey : 1 - 비동의 / 2 - 동의
# choices : 1-7까지 중에서 선택한 값, 비동의(1) - 동의(7)


def solution(survey, choices):
    # key = 성격유형, value = 0인 딕셔너리 생성
    dict = {}
    arr = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']

    for a in arr:
        dict[a] = 0

    # 각 설문조사 마다 abs(choices[i]-4)만큼의 점수를 가져감
    for i in range(len(survey)):
        a, b = survey[i]
        if choices[i] < 4:  # 비동의인 경우
            dict[a] += abs(choices[i] - 4)
        else:  # 동의인 경우
            dict[b] += abs(choices[i] - 4)

    # 각 지표(성격유형2개 묶음)마다 점수가 더 높다면 해당 성격유형을, 점수가 같다면 알파벳으로 더 빠른 것을 선택
    answer = ''
    for i in range(0, 8, 2):
        a, b = arr[i], arr[i + 1]
        if dict[a] == dict[b]:  # 점수가 같다면
            answer += sorted([a, b])[0]  # 알파벳으로 점수가 더 빠른 순
        elif dict[a] > dict[b]:  # 점수가 더 높은게 있다면 더 높은 성격유형을 선택
            answer += a
        else:
            answer += b

    return answer