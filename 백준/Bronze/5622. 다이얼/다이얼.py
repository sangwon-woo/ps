word = input()

num_alphabet = {
    ('A', 'B', 'C') : 3,
    ('D', 'E', 'F') : 4,
    ('G', 'H', 'I') : 5,
    ('J', 'K', 'L') : 6, 
    ('M', 'N', 'O') : 7,
    ('P', 'Q', 'R', 'S') : 8,
    ('T', 'U', 'V') : 9,
    ('W', 'X', 'Y', 'Z') : 10
}

SUM = 0

for w in word:
    for k, v in num_alphabet.items():
        k = list(k)
        if w in k:
            SUM += v

print(SUM)
