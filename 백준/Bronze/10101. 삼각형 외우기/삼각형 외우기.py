angles = []
for i in range(3):
    angles.append(int(input()))

if sum(angles) != 180:
    print("Error")
    exit()

a, b, c = angles
if a==b and b==c and c==60:
    print("Equilateral")
elif a!=b and b!=c and a!=c:
    print("Scalene")
else:
    print("Isosceles")