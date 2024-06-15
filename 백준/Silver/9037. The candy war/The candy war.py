def check(n, candy):
    for i in range(n):
        if candy[i] % 2 ==1:
            candy[i] += 1
    return len(set(candy)) == 1

def teacher(n, candy):
    tmp_lst = [0 for i in range(n)]
    for idx in range(n):
        if candy[idx] % 2:
            candy [idx] += 1
        candy[idx] //= 2
        tmp_lst[(idx+1)% n] = candy[idx]

    for idx in range(n):
        candy[idx] += tmp_lst[idx]

    return candy



def process():
    n, candy = int(input()), list(map(int, input().split()))
    cnt = 0
    while not check(n, candy):
        cnt += 1
        candy = teacher(n, candy)
    print(cnt)

    
for _ in range(int(input())):
    process()