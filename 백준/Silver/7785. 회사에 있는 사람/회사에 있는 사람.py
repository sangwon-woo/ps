import sys
n = int(input())
lst = [i.split() for i in sys.stdin.readlines()]

db = {}
for log in lst:
    name, _log = log
    if _log == 'enter':
        db[name] = 1
    elif _log == 'leave':
        db[name] -=1

ans = sorted( [name for name, i in db.items() if i % 2 == 1], reverse=True)
print('\n'.join(ans))