board = [ list(map(int,input().split())) for _ in range(5) ]
order = [ list(map(int,input().split())) for _ in range(5) ]
orders = []
for i in range(5):
    for n in order[i]:
        orders.append(n)

bingo = 0
while bingo < 3:
    for n in orders:
        bingo = 0

        for i in range(5):
            for j in range(5):
                if board[i][j] == n:
                    board[i][j] = 0

        cross1 = 0
        cross2 = 0
        for i in range(5):
            if board[0][i] + board[1][i] + board[2][i] + board[3][i] + board[4][i] == 0:
                bingo += 1
            if sum(board[i]) == 0:
                bingo += 1
            cross1 += board[i][i]
            cross2 += board[i][4-i]
        if cross1 == 0:
            bingo += 1
        if cross2 == 0:
            bingo += 1
        if bingo >= 3:
            final = n
            break

print(orders.index(final) + 1)


