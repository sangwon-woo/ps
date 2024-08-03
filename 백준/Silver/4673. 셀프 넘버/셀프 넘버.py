cnt = 1
dee = []

def s(n):
    str_n = str(n)
    ret = 0
    for i in str_n:
        ret += int(i)
    return ret

for n in range(10001):
    d = n + s(n)
    if d > 10000:
        continue
    dee.append(d)

while cnt <=10000:
    if cnt not in dee:
        print(cnt)
    cnt += 1