n = int(input())

ret = 1

if n:
    for i in range(n):
        ret *= (i+1)

print(ret)