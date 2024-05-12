n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort(reverse=True)
_max = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if cards[i] + cards[j] >= m:
                break
            _sum = cards[i] + cards[j] + cards[k]
            if _sum > _max and _sum <= m:
                _max = _sum
print(_max)