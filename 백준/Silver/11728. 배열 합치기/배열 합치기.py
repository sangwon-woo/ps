import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []
pos1 = 0
pos2 = 0

while pos1 < n and pos2 < m:
    candidate1 = A[pos1]
    candidate2 = B[pos2]

    if candidate1 < candidate2:
        C.append(candidate1)
        pos1 += 1
    else:
        C.append(candidate2)
        pos2 += 1

if pos1 != n:
    C.extend(A[pos1:n])
if pos2 != m:
    C.extend(B[pos2:m])

for i in range(n+m):
    print(C[i], end=' ')