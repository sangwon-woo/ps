n, b = map(int, input().split())
ans = []
while 1:
    mok, residuals = n // b, n % b
    n = mok
    ans.append(residuals)
    if mok < b:
        if mok:
            ans.append(mok)
        break

for i in ans[::-1]:
    if i <= 9:
        print(i, end='')
    else:
        print(chr(i+55), end='')