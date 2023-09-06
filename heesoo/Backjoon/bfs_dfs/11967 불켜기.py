#실패
n,m=map(int,input().split())
board=[[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a,b,c,d=map(int,input().split())
    board[a][b]=1
    board[c][d]=1

print(board)