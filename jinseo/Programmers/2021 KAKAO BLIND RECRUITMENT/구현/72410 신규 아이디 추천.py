import re

def solution(new_id):
    answer = ''
    
    # 1단계
    new_id = new_id.lower()
    print('1단계 : ', new_id)
    
    # 2단계
    for idx, s in enumerate(new_id):
        if new_id[idx].isalnum() or new_id[idx] in '-_.':
            answer += new_id[idx]
    print('2단계 : ', answer)
    
    # 3단계
    answer = re.sub(r'\.{2,}', '.', answer)
    print('3단계 : ', answer)
    
    # 4단계 
    if len(answer) >= 1 and answer[0] == '.':
        answer = answer[1:] # 첫 번째 문자 제거
    if len(answer) >= 1 and answer[-1] == '.':
        answer = answer[:-1] # 마지막 문자 제거
    print('4단계 : ', answer)
    
    # 5단계
    if len(answer) == 0:
        answer = 'a'
    print('5단계 : ', answer)
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    print('6단계 : ', answer)
    
    # 7단계
    if len(answer) <= 2:
        mar = answer[-1]
        answer = answer + mar * (3-len(answer))
    print('7단계 : ', answer)
        
    
    return answer