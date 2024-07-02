import sys
n = int(input())
words = list(set((map(str.strip, sys.stdin.readlines()))))
words.sort()
words.sort(key=lambda x: len(x) )
[print(i) for i in words]