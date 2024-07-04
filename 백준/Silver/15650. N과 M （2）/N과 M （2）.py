import itertools
n, m = map(int, input().split())

nums = [i for i in range(1, n+1)]

for i in itertools.combinations(nums, m):
    print(*i)