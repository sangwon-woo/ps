nums = []
for i in range(9):
    n = int(input())
    nums.append(n)
    maxx = max(nums)

maxx_idx = nums.index(maxx)
print(maxx, maxx_idx+1, sep='\n')