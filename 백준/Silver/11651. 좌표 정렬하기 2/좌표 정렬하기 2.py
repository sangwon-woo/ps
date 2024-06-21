import sys
n = int(input())
d = sys.stdin.readlines()
d = [list(map(int, i.split(' '))) for i in d]
d.sort(key=lambda x: (x[1], x[0]))
[print(*_) for _ in d]