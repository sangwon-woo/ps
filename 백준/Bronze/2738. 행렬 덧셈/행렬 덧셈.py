n, m = map(int, input().split())
N = [list(map(int, input().split())) for i in range(n)]
M = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(m):
        N[i][j] += M[i][j]

[print(*_) for _ in N]