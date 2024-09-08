n, m = map(int, input().split())
A = list(map(int, input().split()))

start = 0
end = 0
sum = A[0]

count = 0

while 1:
    if sum == m:
        count += 1

    if sum >= m:
        start += 1
        sum -= A[start-1]
    else:
        if end == n-1:
            break

        end += 1
        sum += A[end]

print(count)