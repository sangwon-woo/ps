nums = list(map(int, input().split()))
s = 0

for i in nums:
    s += i**2

print(s%10)