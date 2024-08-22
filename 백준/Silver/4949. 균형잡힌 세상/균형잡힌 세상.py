while True:
    s = input()
    if s == ".":
        break

    stack = []
    balanced = True

    for i in range(len(s)):
        if s[i] in ['(', '[']:
            stack.append(s[i])
        
        if s[i] == ')':
            if len(stack) == 0:
                balanced = False
                break
            last = stack.pop(-1)
            if last != '(':
                balanced = False
                break
        elif s[i] == ']':
            if len(stack) == 0:
                balanced = False
                break

            last = stack.pop(-1)
            if last != '[':
                balanced = False
                break

    if len(stack) != 0:
        balanced = False
    
    if balanced:
        print('yes')
    else:
        print('no')