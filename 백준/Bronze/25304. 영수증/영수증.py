total = int(input())
n = int(input())
SUM = 0
for _ in range(n):
    a, b = map(int, input().split())
    SUM += a*b
print('Yes' if SUM == total else 'No')