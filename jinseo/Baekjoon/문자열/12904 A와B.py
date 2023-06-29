S = input()
T = input()

result = 0

while(1):
    if len(S) == len(T):
        if S == T:
            result = 1
        break

    
    if T[-1] == 'A':
        T = T[:-1]
        continue
    
    T = T[:-1]
    T = T[::-1]

print(result)
        
