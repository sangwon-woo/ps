
table = {
    'black':[0,1],
    'brown':[1,10],
    'red':[2,100],
    'orange':[3,1000],
    'yellow':[4,10000],
    'green':[5,100000],
    'blue':[6,10**6],
    'violet':[7,10**7],
    'grey':[8,10**8],
    'white':[9,10**9]
}

ans = ''
for i in range(3):
    a = input()
    if i==2:
        ans = int(ans) * int(table[a][1])
        break
    v = str(table[a][0])

    ans += v
print(ans)