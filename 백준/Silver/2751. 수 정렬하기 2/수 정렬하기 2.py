lst = []
for _ in range(int(input())):
    lst.append(int(input()))
lst = sorted(lst)
print(*lst, sep='\n')