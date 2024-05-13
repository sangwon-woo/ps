import sys
nums = sys.stdin.readlines()[1:]
nums = [tuple(map(int, i.split())) for i in nums]
nums.sort(key=lambda x: (x[0], x[1]))
[print(*_) for _ in nums]