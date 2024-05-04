x, y = [], []
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

rx, ry = 0, 0
for i in x:
    if x.count(i) == 1:
        rx = i
for j in y:
    if y.count(j) == 1:
        ry = j

print(rx, ry)

