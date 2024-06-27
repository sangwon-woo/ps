while sum(nums := list(map(int, input().split()))) != 0 :
    a, b, c = nums

    if max(nums) >= sum(nums) - max(nums):
        print("Invalid")
        continue

    if a==b and b==c and c==a:
        print("Equilateral")
    elif a!=b and b!=c and c!=a:
        print("Scalene")
    elif a==b or b==c or c==a:
        print("Isosceles")