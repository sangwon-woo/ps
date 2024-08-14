n, m = map(int, input().split())
ans = 0
arr = []

for _ in range(m):
    arr.append(list(map(int, input().split())))

pack, piece = min(arr, key=lambda x: x[0])[0], min(arr, key=lambda x: x[1])[1]
q, r = divmod(n, 6)
if 6*piece <= pack:
    ans = n*piece
else:
    if (q * pack) + (r * piece) > (q+1) * pack:
        ans = (q+1) * pack
    else:
        ans = (q * pack) + (r * piece)
print(ans)