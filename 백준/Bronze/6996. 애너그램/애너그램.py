for _ in  range(int(input())):
    a, b = input().split()
    c, d = map(sorted, [a, b])
    c = ''.join(c)
    d = ''.join(d)

    if c==d:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')