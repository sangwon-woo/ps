a, b, c,  d, e, f = map(int, input().split())
dt = (a*e) - (b*d)
                        
x = ((c*e) - (b*f)) / dt
y = ((-c*d) + (a*f)) / dt
print(*map(int, [x, y]))