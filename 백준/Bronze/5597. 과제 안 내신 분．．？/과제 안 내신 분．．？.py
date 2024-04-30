a = set()
b = set(i for i in range(1, 31))
for i in range(28):
    n = int(input())
    a.add(n)

print(*sorted(list(b-a)), sep='\n')