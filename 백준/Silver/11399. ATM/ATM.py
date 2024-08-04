n = int(input())
lst = list(map(int, input().split()))
lst.sort()

ans = 0
cum = 0
for i in lst:
    cum += i
    ans += cum
print(ans)