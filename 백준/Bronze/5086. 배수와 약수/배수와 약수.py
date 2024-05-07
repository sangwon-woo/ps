while True:
    a, b = map(int, input().split())
    if a==0 and b==0: break
    if a == (a//b) * b:
        print('multiple')
    elif b == (b//a) * a:
        print('factor')
    else:
        print('neither')