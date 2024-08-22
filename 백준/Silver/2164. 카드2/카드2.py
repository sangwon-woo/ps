from collections import deque

n = int(input())

d = deque([i for i in range(1, n+1)])
while len(d) > 1:
    d.popleft()
    a = d.popleft()
    d.append(a)
print(d[0])