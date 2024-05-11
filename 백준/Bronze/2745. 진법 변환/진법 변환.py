n, b = input().split()
b = int(b)
ans = 0
nums = [str(i) for i in range(10)]
z = len(n)
for i, v in enumerate(n):
    if v in nums:
        ans += int(v) * (b**(z-i-1))
    else:
        ans += (b**(z-i-1)) * (ord(v)-55)

print(ans)
