n, k = map(int, input().split())

denominator = 1
cnt = 0
while True:
    if (n // denominator) * denominator == n:
        cnt += 1
        if cnt == k:
            print(denominator)
            break
    if denominator > n:
        print(0)
        break
    denominator += 1