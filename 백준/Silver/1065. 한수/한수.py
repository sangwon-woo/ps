def check(n):
    str_n = str(n)
    a,b,c = str_n[0], str_n[1], str_n[2]
    a,b,c = map(int, [a,b,c])
    if a-b == b-c:
        return True


N = int(input())
ans = 0
for n in range(1,N+1):
    if n < 100:
        ans += 1
    else:
        if check(n):
            ans += 1

print(ans)