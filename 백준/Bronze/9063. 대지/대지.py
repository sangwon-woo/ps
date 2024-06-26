n = int(input())
if n == 1:
    print(0)
    exit()
min_x = float('inf')
min_y = float('inf')
max_x = float('-inf')
max_y = float('-inf')

for _ in range(n):
    a, b = map(int, input().split())
    if a <= min_x:
        min_x = a
    if a >= max_x:
        max_x = a
    if b <= min_y:
        min_y = b
    if b >= max_y:
        max_y = b
print(int((max_x - min_x)*(max_y - min_y)))