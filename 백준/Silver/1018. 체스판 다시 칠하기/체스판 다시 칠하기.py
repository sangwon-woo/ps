n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

wfirst = ['W','B','W','B','W','B','W','B']
bfirst = ['B','W','B','W','B','W','B','W']

board1 = [
    wfirst,bfirst,wfirst,bfirst,
    wfirst,bfirst,wfirst,bfirst
]
board2 = [
    bfirst,wfirst,bfirst,wfirst,
    bfirst,wfirst,bfirst,wfirst
]

def get_num(n_board, new_board):
    num = 0
    for i in range(8):
        for j in range(8):
            if n_board[i][j] == new_board[i][j]:continue
            num += 1
    return num

ans = 64

for i in range(n-7):
    for j in range(m-7):
        new_board = [row[j:j+8] for row in board[i:i+8]]
        num1 = get_num(board1, new_board)
        num2 = get_num(board2, new_board)
        ans = min([ans, num1, num2])
print(ans)
        