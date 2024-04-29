n = int(input())
# mat = [list(input().rstrip()) for i in range(5)]
mat = [list([0]*100) for i in range(100)]
for _ in range(n):
    r, c = map(int, input().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            if mat[i][j] == 0:
                mat[i][j] = 1
ret = 0
for i in range(100):
    for j in range(100):
        if mat[i][j]==1:
            ret += 1
# [print(*_) for _ in mat]
print(ret)