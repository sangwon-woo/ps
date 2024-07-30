for _ in range(int(input())):
    x, y = map(int, input().split())
    d = y - x
    if d == 1: 
        print(1)
        continue
    if d == 2: 
        print(2)
        continue
    if d == 3: 
        print(3)
        continue

    sqrt_d = str(d**(1/2)).split('.')
    sqrt_d = int(sqrt_d[0])
    double_sqrt_d = (sqrt_d**2) + sqrt_d

    if d==sqrt_d**2:
        print((sqrt_d*2) - 1)

    elif d > sqrt_d**2 and d <= double_sqrt_d:
        print(sqrt_d*2)
    
    elif d > double_sqrt_d:
        print(sqrt_d*2 + 1)