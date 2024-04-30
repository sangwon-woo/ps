word = map(ord, input().lower())

charac = {
    i+97:0 for i in range(26)
}
for k in word:
    charac[k] += 1
maxx = max(charac.values())

cnt = 0
ret = ''

for k, v in charac.items():
    if v == maxx:
        ret = chr(k).upper()
        cnt += 1
        if cnt > 1:
            ret  = '?'

print(ret)