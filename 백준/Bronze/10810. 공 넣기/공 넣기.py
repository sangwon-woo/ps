n, m = map(int, input().split())
ba = [0 for i in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i-1, j):
        ba[l] = k

print(*ba)
