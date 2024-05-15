n = int(input())

trp = []
for _ in range(n):
    trp.append(int(input()))

cnt = 0
m = 0
for t in trp:
    if t> m:
        cnt += 1
        m = t
print(cnt)
cnt = 0
m = 0
for t in trp[::-1]:
    if t > m:
        cnt += 1
        m = t
print(cnt)