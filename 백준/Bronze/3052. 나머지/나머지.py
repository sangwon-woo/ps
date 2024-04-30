residuals = set()

for _ in range(10):
    n = int(input())
    residuals.add(n%42)

print(len(residuals))