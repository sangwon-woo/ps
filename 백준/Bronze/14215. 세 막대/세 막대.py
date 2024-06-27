nums = list(map(int, input().split()))
a, b, c = nums
max_n = max(nums)
sum_of_others = sum(nums) - max_n
if max_n >= sum_of_others:
    sum_of_others = sum(nums) - max_n
    print(2*sum_of_others - 1)
else:
    print(sum(nums))