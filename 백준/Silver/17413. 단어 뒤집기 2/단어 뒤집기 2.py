s = input()

check = False
tmp = ''
ans = '' 
for i in s:
    if i == ' ':
        if not check:
            ans += tmp[::-1] + " "
            tmp = ""
        else:
            ans += ' '
        
    elif i =='<':
        check = True
        ans += tmp[::-1] + "<"
        tmp = ""
    elif i == ">":
        check = False
        ans += ">"
    else:
        if check:
            ans += i
        else:
            tmp += i

ans += tmp[::-1]
print(ans)