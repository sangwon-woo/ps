n, l, k = map(int, input().split())
easy, hard = 0, 0
for i in range(n):
    sub1, sub2 = map(int, input().split())
    if sub2 <= l:
        hard += 1

    elif sub1 <= l:
        easy += 1

ans = min(hard, k) * 140

if hard < k:
    ans += min(k-hard, easy) * 100

print(ans)