'''
입력 : 가로와 세로 길이/ 자르는 횟수/ 0(가로) 1(세로) 위치
출력 : 가장 큰 사각형 넓이
10 8
3
0 3
1 4
0 2 
30

10 8 에서 3에 하나 2에 하나
8 + 1 후 3에 투입 = 10
'''
garo, sero = map(int,input().split())
board = [ [0] * garo for _ in range(sero) ]

n = int(input())
garo_list = [] ; sero_list = []
for i in range(n):
    direction, location = map(int,input().split())
    if direction == 0:
        garo_list.append(location)
    else:    
        sero_list.append(location)

garo_list.sort()
sero_list.sort()

garo_a = 0; sero_a=0
for l in garo_list:
    board.insert(l+garo_a, [1] * len(board[i]))
    garo_a += 1
for l in sero_list:
    for j in range(len(board)):
        board[j].insert(l+sero_a, 1)
    sero_a += 1


y = 0; x = 0
l_garo = 0; l_sero = 0
max_square = 0
for y in range(len(board)):
    for x in range(len(board[y])):
        if (board[y][x] == 0 and y-1 < 0 and x - 1 < 0) or (board[y][x] == 0 and board[y-1][x] == 1 and x - 1 < 0) or (board[y][x] == 0 and y-1 < 0 and board[y][x - 1] == 1) or (board[y][x] == 0 and board[y-1][x] == 1 and board[y][x - 1] == 1):
            while board[y][x+l_garo] == 0:
                l_garo += 1
                if x+l_garo >= len(board[y]):
                    break
            while board[y+l_sero][x] == 0:
                l_sero += 1
                if y+l_sero >= len(board):
                    break
            if l_garo * l_sero > max_square:
                max_square = l_garo * l_sero
            l_garo = 0; l_sero = 0

print(max_square)
