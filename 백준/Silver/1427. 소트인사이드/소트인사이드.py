import sys
input = sys.stdin.readline
n = list(input())
n.sort()
print(''.join(n[::-1]))
