n = int(input())
cards = list(map(int, input().split()))
_cards = set(cards)
dd = {}
for i in _cards:
    dd[i] = 0

for i in cards:
    dd[i] += 1

m = int(input())
cards = list(map(int, input().split()))
for i in cards:
    if i in _cards:
        print(dd[i], end=' ')
    else:
        print(0, end=' ')