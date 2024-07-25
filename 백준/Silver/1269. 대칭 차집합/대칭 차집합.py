a, b = map(int, input().split())
A = set(list(input().split()))
B = set(list(input().split()))
print(len(A-B)+len(B-A))