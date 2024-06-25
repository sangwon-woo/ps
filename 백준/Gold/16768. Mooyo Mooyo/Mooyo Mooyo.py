n, k = map(int, input().split())
m = [list(input()) for _ in range(n)]

def new_array(n):
    return [ [False for i in range(10)] for _ in range(n)]

dx, dy = [0,1,0,-1],[1,0,-1,0]

def dfs(x, y):
    ck[x][y] = True
    ret = 1
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if xx < 0 or xx >= n or yy < 0 or yy >= 10: continue
        if ck[xx][yy] or m[x][y] != m[xx][yy]: continue
        ret += dfs(xx, yy)
    return ret

def dfs2(x, y, val):
    ck2[x][y] = True
    m[x][y] = '0'
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if xx <0 or xx >= n or yy <0 or yy >= 10:continue
        if ck2[xx][yy] or m[xx][yy] != val: continue 
        dfs2(xx, yy, val)
    

def down():
    for i in range(10):
        tmp = []
        for j in range(n):
            if m[j][i] != '0':
                tmp.append(m[j][i])
        for j in range(n-len(tmp)):
            m[j][i] = '0'
        for j in range(n-len(tmp), n):
            m[j][i] = tmp[j-(n-len(tmp))]
    pass

while 1:
    exist = False
    ck = new_array(n)
    ck2 = new_array(n)

    for i in range(n):
        for j in range(10):
            if m[i][j] == '0' or ck[i][j]: continue
            res = dfs(i, j)
            if res >= k:
                dfs2(i, j, m[i][j])
                exist = True

    if not exist:
        break
    
    down()

for i in m:
    print("".join(i))