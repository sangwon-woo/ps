n, m = map(int, input().split())
ba = [i+1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1

    first = ba[:i]
    partial = list(reversed(ba[i:j+1]))
    second = ba[j+1:]

    ba = first+partial+second
    
print(*ba)