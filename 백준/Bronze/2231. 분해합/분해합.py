n = input()
len_n = len(n)
n = int(n)
flag = False
bound = n-(9*len_n) if n-(9*len_n) >= 0 else 0
for k in range(bound, n):
    str_k = list(str(k))
    _sum = k + sum(map(int, str_k))
    if _sum == n:
        print(k)
        flag = True
        break
if not flag:
    print(0)
