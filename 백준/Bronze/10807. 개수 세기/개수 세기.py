n = int(input())
lst = list(map(int, input().split()))
target = int(input())
ret=0
for i in lst:
    if i==target:
        ret +=1

print(ret)