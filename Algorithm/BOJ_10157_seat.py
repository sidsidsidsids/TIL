'''
왼쪽 아래서 부터 시계방향으로
'''
J, I = map(int,input().split())
N = int(input())

if N > J*I:
    print(0)
else:
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    board = [ [0]*J for _ in range(I) ]

    x = 0 ; y = I-1 ; number = 1 ; idx = 0
    while number <= J*I:
        board[y][x] = number
        if number == N:
            break
        number += 1
        x += dj[idx]; y += di[idx]

        if y < 0 or y >= I or x < 0 or x >= J or board[y][x] != 0:
            x -= dj[idx]; y -= di[idx]
            idx += 1
            if idx == 4:
                idx -= 4
            x += dj[idx]; y += di[idx]

    print(x+1, I-y)
