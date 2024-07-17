# DP: 어떤 지점에 도착할 수 있는 상태
DP = [1, 0, 0, 0, 0, 0, 0, 0]

# 0~8번 순서대로 정보관, 전산관, 미래관, 신영관, 한경직, 진리관, 학생회관, 공학관
# 전체 점화식
def nxt(state):
    tmp = [0 for _ in range(8)]
    tmp[0] = state[1] + state[2]
    tmp[1] = state[0] + state[2] + state[3]
    tmp[2] = state[0] + state[1] + state[3] + state[4]
    tmp[3] = state[1] + state[2] + state[4] + state[5]
    tmp[4] = state[2] + state[3] + state[5] + state[7]
    tmp[5] = state[3] + state[4] + state[6]
    tmp[6] = state[5] + state[7]
    tmp[7] = state[4] + state[6]
    return tmp

for i in range(int(input())):
    DP = nxt(DP)

print(DP[0] % 1000000007)