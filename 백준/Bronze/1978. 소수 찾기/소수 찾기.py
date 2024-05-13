MAX_NUM = 1000

prime_list = list(range(MAX_NUM+1))
for i in range(2, 34):
    if prime_list[i]:
        prime_list[i+i::i] = [0] * len(prime_list[i+i::i])

prime_list = list(filter(None, prime_list[2:]))

n = int(input())
lst = list(map(int, input().split()))
s = 0
for i in lst:
    if i in prime_list:
        s += 1

print(s)