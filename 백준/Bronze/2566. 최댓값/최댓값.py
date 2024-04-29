mat = [list(map(int, input().split())) for i in range(9)]
a, b = 0, 0

maxx = 0
for i in range(9):
    for j in range(9):
        if mat[i][j] > maxx:
            maxx = mat[i][j]
            a, b = i, j


# [print(*_) for _ in mat]
print(maxx)
print(a+1, b+1)