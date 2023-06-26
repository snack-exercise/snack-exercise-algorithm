def solution(id_list, report, k):
    answer = [ 0 for _ in range(len(id_list))]
    dict = {} # 회원 : 신고한 회원들
    dict_cnt = {} # 회원 : 신고받은 횟수
    
    for id in id_list:
        dict[id]=[]
        dict_cnt[id]=0
    
    for val in report:
        a,b=val.split()
        dict[a].append(b)
    
    # 신고한 회원들 중복 제거
    for key in dict.keys():
        dict[key]=set(dict[key])
        
    for val in dict.values():
        for v in val:
            dict_cnt[v]+=1
    
    # 신고한 회원들마다 해당 신고 횟수가 k이상인 경우 +=1
    idx=0
    for id in id_list:
        if id in dict.keys():
            for v in dict[id]:
                if dict_cnt[v]>=k:
                    answer[idx]+=1
            idx+=1
            
    return answer