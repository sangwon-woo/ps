from copy import deepcopy

n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
Q = [tuple(map(int, input().split())) for _ in range(k)]
ans = 10000
dx, dy = [1,0,-1,0],[0, -1,0,1]


def value(arr):
    return min([sum(i) for i in arr])

def convert(arr, query):
    (r, c, s) = query
    r, c,  = r-1, c-1
    new_arr = deepcopy(arr)
    for i in range(1, s+1):
        rr, cc = r-i, c+i
        for w in range(4):
            for d in range(i*2):
                rrr, ccc = rr+dx[w], cc+dy[w]
                new_arr[rrr][ccc] = arr[rr][cc]
                rr, cc = rrr, ccc 
    return new_arr

def dfs(arr, query):
    global ans
    if sum(query) == k:
        ans = min(ans, value(arr))
        return
    for i in range(k):
        if query[i]: continue
        new_arr = convert(arr, Q[i])
        query[i] = 1
        dfs(new_arr, query)
        query[i] = 0

dfs(A, [0 for i in range(k)])
print(ans)