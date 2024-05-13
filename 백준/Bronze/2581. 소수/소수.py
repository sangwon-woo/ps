MAX_NUM = 10001

prime_list = list(range(MAX_NUM+1))
for i in range(2, 110):
    if prime_list[i]:
        prime_list[i+i::i] = [0] * len(prime_list[i+i::i])

prime_list = list(filter(None, prime_list[2:]))

a = int(input())
b = int(input())

ans = []
for k in prime_list:
    if k >= a and k <= b:
        ans.append(k)
if ans:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)