n = int(input())
if n==1:
    exit()

root_n = int(n**(1/2))
p_flag = True
c_flag = False
for k in range(1, root_n+1):
    if k==1: continue
    flag = True
    while flag:
        if n % k == 0:
            print(k)
            n = int(n/k)
            p_flag = False
        else:
            flag = False
    if k==root_n and n!=1:
        print(n)
        c_flag = True
if p_flag and not c_flag:
    print(n)        