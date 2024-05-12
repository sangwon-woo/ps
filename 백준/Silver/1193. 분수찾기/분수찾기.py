n = int(input())

_sum = 0
plus = 1
while 1:
    _sum += plus
    if _sum >= n:
        ans = plus
        break
    plus += 1

if plus % 2 == 0: # 짝수일때
    # 1/plus 부터 시작
    nominator = ans + n - _sum
    denominator = 1 + (_sum - n)
    print(str(nominator)+'/'+str(denominator))
    
elif plus % 2 == 1:
    nominator = 1 + (_sum - n)
    denominator = ans + n - _sum
    print(str(nominator)+'/'+str(denominator))