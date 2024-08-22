import sys
from collections import deque

N = int(input())
d = deque([])
for i in range(N):
    command = sys.stdin.readline()
    command = command.split()
    
    if command[0] == 'push':
        d.append(command[1])

    elif command[0] == 'pop':
        if len(d)==0:
            print(-1)
        else:
            print(d.popleft())

    elif command[0] == 'size':
        print(len(d))

    elif command[0] == 'empty':
        if len(d)==0:
            print(1)
        else:
            print(0)

    elif command[0] == 'front':
        if len(d)==0:
            print(-1)
        else:
            print(d[0])

    elif command[0] == 'back':
        if len(d)==0:
            print(-1)
        else:
            print(d[-1])