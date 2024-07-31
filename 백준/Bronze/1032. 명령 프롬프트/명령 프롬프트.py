ans = ''
lst = []
for i in range(int(input())):
    lst.append(input())
llen = len(lst[0])
for i in range(llen):
    sset = set()
    for w in lst:
        sset.add(w[i])
    if len(sset)==1:
        ans += w[i]
    else:
        ans += '?'
print(ans)