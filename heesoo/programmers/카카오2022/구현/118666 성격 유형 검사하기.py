# 1번 지표	라이언형(R), 튜브형(T)
# 2번 지표	콘형(C), 프로도형(F)
# 3번 지표	제이지형(J), 무지형(M)
# 4번 지표	어피치형(A), 네오형(N)

def solution(survey, choices):
    answer = ''
    
    dict = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for i in range(len(survey)):
        if choices[i]>=4:
            dict[survey[i][1]]+=(choices[i]-4)
        else:
            dict[survey[i][0]]+=(4-choices[i])
    
    for i in range(0,8,2):
        if dict[list(dict.keys())[i]] >= dict[list(dict.keys())[i+1]]:
            answer+=list(dict.keys())[i]
        else:
            answer+=list(dict.keys())[i+1]
    
    return answer