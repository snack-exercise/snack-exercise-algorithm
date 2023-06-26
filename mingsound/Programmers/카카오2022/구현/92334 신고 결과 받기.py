def solution(id_list, report, k):
    # 1. id_list를 돌면서, 각 유저의 이름을 key, (신고당한횟수, [신고를 누구로 부터 당했는지], 메일 받는 횟수)를 value로 가지도록 딕셔너리를 생성
    _dict = {}
    for id in id_list:
        _dict[id] = [0, [], 0]  # (신고당한횟수, [신고를 누구로 부터 당했는지], 메일 받는 횟수)

    # 2. report를 돌면서 자기가 신고당한 횟수, 누구한테서 신고당했는지 추가
    for i in range(len(report)):
        a, b = report[i].split()  # 띄어쓰기 기준 분리
        if a not in _dict[b][1]:  # 한 유저가 같은 유저를 여러번 신고해도 1번 신고로 침
            _dict[b][1].append(a)  # 본인이 신고당한 횟수 + 1
            _dict[b][0] += 1  # 본인이 누구로부터 신고당했는지 추가
    # 파이썬 개념 "포함여부" : list -  not in, 문자열 - contains

    # 3. _dict를 돌면서 신고대상의 block이 k이상이면 메일 받는 횟수 추가
    for a in _dict.keys():
        if _dict[a][0] >= k:  # 본인이 k번 이상 신고당했다면
            for name in _dict[a][1]:  # 자신을 신고한 사람들의 메일 받는 횟수 + 1
                _dict[name][2] += 1
    # 파이썬 개념 dict.keys(), dict.values()

    # 4. 메일 받는 횟수 answer에 옮기기
    answer = []
    for a in _dict.keys():
        answer.append(_dict[a][2])

    return answer