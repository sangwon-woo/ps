h, m = map(int, input().split())
t = int(input())
m += t
mok = m//60
rest = m%60
m = rest
h += mok
if h>=24:
    h -= 24

print(f'{h} {m}')