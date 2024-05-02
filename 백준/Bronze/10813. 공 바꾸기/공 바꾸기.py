n, m = map(int, input().split())
ba = [i+1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    i, j = i-1, j-1
    ba[i], ba[j] = ba[j], ba[i]

print(*ba)