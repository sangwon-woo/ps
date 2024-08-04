from itertools import combinations

dwarf = []
for _ in range(9):
    dwarf.append(int(input()))

for c in combinations(dwarf, 7):
    if sum(c) == 100:
        c = sorted(list(c))
        [print(i) for i in c]
        break