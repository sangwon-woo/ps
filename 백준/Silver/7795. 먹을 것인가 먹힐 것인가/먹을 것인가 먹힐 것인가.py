for _ in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A = sorted(A)
    B = sorted(B)

    main, sub, count = 0, 0, 0

    while main < N:
        if sub == M:
            count += sub
            main += 1
        else:
            if A[main] > B[sub]:
                sub += 1
            else:
                count += sub
                main +=1

    print(count)