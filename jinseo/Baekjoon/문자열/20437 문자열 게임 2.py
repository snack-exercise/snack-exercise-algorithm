T = int(input())

for _ in range(T):
    w = input()
    k = int(input())
    dict = {}
    min_len = len(w) + 1
    min_word = w[0]

    # 1. 어떤 문자를 k개 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
    for idx, word in enumerate(w):
        tmp = idx + 1
        l = 1
        flag = False

        if l == k:
            flag = True

        while tmp < len(w):
            if w[tmp] == word:
                l += 1
            tmp += 1
            if l == k:
                flag = True
                break

        if flag == True and min_len > tmp - idx:
            min_len = tmp - idx
            min_word = word

    
    # 2. 어떤 문자를 정확히 k개 포함하고, 문자열의 첫번째와 마지막 글자가 min_word와 같은 가장 긴 연속 문자열의 길이를 구한다.
    # w 순회 -> min_word를 만나면 left로 두고, k를 충족할 때까지 다음 min_word를 right로 둔다. -> max_len 갱신

    left = right = 0
    
    for idx, word in enumerate(w):
        if word == min_word:
            right = idx + 1



    
    
