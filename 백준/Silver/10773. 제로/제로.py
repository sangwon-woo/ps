import sys
k = int(input())
numbers = list(map(int, sys.stdin.readlines()))

num = []
for n in numbers:
    if n == 0 and len(num):
        num.pop(-1)
    else: num.append(n)
print(sum(num))