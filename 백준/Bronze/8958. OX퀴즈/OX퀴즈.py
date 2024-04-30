for i in range(int(input())):
    case = input().strip()
    score = 0

    before = 'X'
    num = 0
    for j in range(len(case)):
        if case[j] == 'O':
            if before == 'X':
                num += 1
                score += num
            elif before == 'O':
                num += 1
                score += num
        elif case[j] == 'X':
            before = 'X'
            num = 0
    print(score)