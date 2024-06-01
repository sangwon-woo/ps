import sys
input = sys.stdin.readline

n = int(input().strip())

array = []
for _ in range(n):
    array.append(int(input().strip()))

array.sort()

result = 0
for i in range(1, len(array)+1):
    result += abs(i - array[i-1])

print(result)