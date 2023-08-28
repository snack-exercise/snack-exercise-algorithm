n,m=map(int,input().split())
arrn=[list(map(int,input().split())) for _ in range(n)]
arrm=[list(map(int,input().split())) for _ in range(m)]

# 누적합 배열 만들기
sumarr=[[0 for _ in range(n)] for _ in range(n)]
sumarr[0][0]=arrn[0][0]
for i in range(1,n):
    sumarr[0][i]=sumarr[0][i-1]+arrn[0][i]
    sumarr[i][0]=sumarr[i-1][0]+arrn[i][0]
for i in range(1,n):
    for j in range(1,n):
        sumarr[i][j]= sumarr[i-1][j]+sumarr[i][j-1]-sumarr[i-1][j-1]+arrn[i][j]

def calsum(x1,y1,x2,y2):
    ans=sumarr[x2][y2]
    if x1>0 and y1>0:
        ans = ans - sumarr[x2][y1-1] - sumarr[x1-1][y2] + sumarr[x1-1][y1-1]
    elif x1>0 and y1<=0:
        ans = ans - sumarr[x1-1][y2] 
    elif x1<=0 and y1>0:
        ans = ans - sumarr[x2][y1-1]
    return ans

for  i in range(m):
    a,b,c,d,=arrm[i]
    print(calsum(a-1,b-1,c-1,d-1))




# for i in range(m):
#     a,b,c,d = arrm[i]
#     sum=0
#     k,j = a,b
#     while True:
#         sum+=arrn[k-1][j-1]
#         if j<d:
#             j+=1
#         elif j>=d and k<c:
#             k+=1
#             j=b
#         elif j>=d and k>=c:
#             break
#     print(sum)
