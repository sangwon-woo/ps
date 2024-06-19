r, c = map(int, input().split())
M = [list(input()) for i in range(r)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

ck = False

for i in range(r):
    for j in range(c):
        if M[i][j] == 'W':
            for w in range(4):
                ii, jj = i+dx[w], j+dy[w]
                if ii < 0 or ii == r or jj < 0 or jj == c:
                    continue
                if M[ii][jj] == 'S':
                    ck = True

if ck:
    print(0)
else:
    print(1)
    for i in range(r):
        for j in range(c):
            if M[i][j] not in 'SW':
                M[i][j] = "D"
    for i in M:
        print(''.join(i))