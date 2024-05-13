n = int(input())

member = []
for i in range(n):
    num, name = input().split()
    num = int(num)
    member.append((num, name))
member.sort(key=lambda x: x[0])
[print(*_) for _ in member]