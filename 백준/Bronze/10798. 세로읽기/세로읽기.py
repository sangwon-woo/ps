mat = [list(input().rstrip()) for i in range(5)]
ret = ''

row_len = []
for i in range(5):
    row_len.append(len(mat[i]))

max_len = max(row_len)
for i in range(5):
    J = len(mat[i])
    if  J < max_len:
        rest = max_len - J
        for j in range(rest):
            mat[i].append(-1)

for j in range(max_len):
    for i in range(5):
        if mat[i][j] == -1:
            continue
        ret += mat[i][j]

print(ret)