import sys
input = sys.stdin.readline

N = input()
S = input().strip()

score, bonus = 0,0

for idx, OX in enumerate(S):
    if OX == 'O':
        score, bonus = score+ idx+1+bonus, bonus + 1
    else:
        bonus = 0
print(score)