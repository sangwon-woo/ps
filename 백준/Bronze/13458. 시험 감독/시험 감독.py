N = int(input()) # 시험장의 갯수
a_list = list(map(int, input().split()))
B, C = map(int, input().split())

total = 0
total += len(a_list)
a_list = [i-B if i-B>0 else 0 for i in a_list ]


for n in a_list:
    mok, namuzi = n // C, n % C
    if namuzi == 0:
        total += mok
    else:
        total += mok + 1

print(total)