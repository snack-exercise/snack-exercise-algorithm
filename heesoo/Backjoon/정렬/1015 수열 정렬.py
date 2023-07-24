import sys
import math

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))

sortA = [i for i in a]
sortA.sort()

p=[]
for i in a:
    p.append(sortA.index(i))
    sortA[sortA.index(i)]=-1

for i in p:
    print(i, end=" ")