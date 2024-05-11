for _ in range(int(input())):
    ans = [0,0,0,0]
    n = int(input())
    if n >= 25:
        ans[0] += n // 25
        n = n % 25
    if n >= 10:
        ans[1] += n // 10
        n = n % 10
    if n >= 5:
        ans[2] += n // 5
        n = n % 5
    ans[3] += n
    print(*ans)