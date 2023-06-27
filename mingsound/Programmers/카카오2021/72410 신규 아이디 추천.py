from collections import deque


def solution(new_id):
    # 1. 소문자 치환
    new_id = new_id.lower();

    # 2. 문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    arr = ['-', '_', '.']
    alp = ord('a')
    arr = arr + [chr(alp + i) for i in range(26)] + [str(i) for i in range(10)]

    new_id = deque(new_id)
    answer = ''
    for a in new_id:
        if a in arr:
            answer += a

    # 3. 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    answer2 = deque([])
    flag = False
    for i in range(len(answer)):
        if not flag and answer[i] == '.':  # 처음 온점을 만났을 때
            flag = True
            answer2.append('.')
            continue
        elif flag and answer[i] == '.':  # 이전에 연속 온점이 있었고, 온점이면 pass
            continue
        else:  # 현재 온점이 아니라면
            answer2.append(answer[i])
            flag = False

    # 4. new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if answer2[0] == '.':
        answer2.popleft()
    elif answer2[-1] == '.':
        answer2.pop()

    # 5. new_id가 빈 문자열이라면, new_id에 "a"를 대입
    if len(answer2) == 0:
        answer2 = ['a']

    # 6. 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    #    만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    answer2 = list(answer2)[:15]  # deque는 인덱싱 안됨, TypeError: sequence index must be integer, not 'slice'
    if answer2[-1] == '.':
        answer2.pop()

    # 7. new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(answer2) <= 2:
        last = answer2[-1]
        for i in range(3 - len(answer2)):
            answer2.append(last)

    answer = ''.join(answer2)
    return answer