# 완탐 -> 시간 초과

import sys
input=sys.stdin.readline

sstr=input()
tstr=input()

if len(sstr)>=len(tstr) and sstr!=tstr:
    print(0)
    exit()

def solution(str):
    if len(str)==len(tstr):
        if str==tstr:
            print(1)
            exit()
    else:
        str1=str+'A'
        solution(str1)
        
        str2=''
        for s in str:
            if s=='A':
                str2+='B'
            else:
                str2+='A'
        str2+='B'
        solution(str2)
        
        
solution(sstr)
print(0) 