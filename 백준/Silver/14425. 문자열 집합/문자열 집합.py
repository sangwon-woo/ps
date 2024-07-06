n, m = map(int, input().split())
s, inspection = [input() for i in range(n)], [input() for i in range(m)]

cnt = 0
for w in inspection:
    if w in s:
        cnt += 1

print(cnt)