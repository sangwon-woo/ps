n, m = map(int, input().split())
nl, ml = [],[]
for _ in range(n):
    nl.append(input())
for _ in range(m):
    ml.append(input())
ans = sorted(list(set(nl) & set(ml)))
print(len(ans))
print('\n'.join(ans))