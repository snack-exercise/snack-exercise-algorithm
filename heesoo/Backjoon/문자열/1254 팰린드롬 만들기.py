s=input()

for i in range(len(s)):
    if s[i:]==s[i:][::-1]:
        print('!:',s[i:],s[i:][::-1])
        print(len(s)+i)
        break
    else:
        print(s[i:],s[i:][::-1])