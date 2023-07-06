n=int(input())

ans=0
row=[0]*n

# x 자리에 놓을 수 있는지
def check(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i])==abs(x-i):
            return False
    return True

def solution(x):
    global ans
    print(x,':',row)
    if x==n:
        ans+=1
        return
    
    else:
        for i in range(n):
            row[x]=i # [x,i]
            if check(x):
                solution(x+1)

solution(0)
print(ans)