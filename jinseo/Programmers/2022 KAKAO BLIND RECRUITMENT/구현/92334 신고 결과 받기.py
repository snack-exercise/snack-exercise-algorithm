def solution(id_list, report, k):
    answer = [0]*len(id_list)
    reports = {x : 0 for x in id_list} 
    
    # 유저별 신고당한 횟수를 reports에 할당
    for s in set(report): # 동일한 유저에 대한 신고 횟수는 1회로 처리하기 위해 set으로 처리
        reports[s.split(" ")[1]] += 1
        
    # report를 순회하며 정지된 유저가 있다면 신고한 사람 +1
    for i in set(report):
        if reports[i.split(" ")[1]] >= k:
            answer[id_list.index(i.split(" ")[0])] += 1
    
    return answer