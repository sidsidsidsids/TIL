from collections import deque

maze = [[list(map(int,input().split())) for _ in range(5)] for __ in range(5)]

def board_cases(board):
    def spin_90(board):
        change_board = [[0] * 5 for _ in range(5)]
        for j in range(5):
            for i in range(4, -1, -1):
                if board[i][j] == 1:
                    change_board[j][4 - i] = 1
                else:
                    pass
        return change_board

    c_board_1 = spin_90(board)
    c_board_2 = spin_90(c_board_1)
    c_board_3 = spin_90(c_board_2)
    return board, c_board_1, c_board_2, c_board_3

def maze_cases(boards):
    totalCase = [ [] for _ in range(4**5)]
    t_idx = 0
    maze_case = [[] for _ in range(5)]
    for board_1 in boards[0]:
        maze_case[0] = board_1
        for board_2 in boards[1]:
            maze_case[1] = board_2
            for board_3 in boards[2]:
                maze_case[2] = board_3
                for board_4 in boards[3]:
                    maze_case[3] = board_4
                    for board_5 in boards[4]:
                        maze_case[4] = board_5
                        maze_input = maze_case[:]
                        totalCase[t_idx] = maze_input
                        t_idx += 1
    return totalCase

def BFS(mazes):
    min_val = 5*5*5
    for miro in mazes:
        if miro[0][0][0] == miro[4][4][4] == 1:
            Q = deque()
            Q.append([0,0,0])
            V = [[[0] * 5 for _ in range(5)] for __ in range(5)]
            V[0][0][0] = 1
            old = 1
            new = 0
            cnt = 1

            while Q:
                elem = Q.popleft()
                old -= 1
                z,y,x = elem[0],elem[1],elem[2]
                for nz,ny,nx in [[z+1,y,x],[z-1,y,x],[z,y+1,x],[z,y-1,x],[z,y,x+1],[z,y,x-1]]:
                    if 0 <= nz <= 4 and 0 <= ny <= 4 and 0 <= nx <= 4:
                        if nz == ny == nx == 4:
                            print('goal')
                            if min_val > cnt:
                                min_val = cnt
                                break
                        if miro[nz][ny][nx] == 1 and not V[nz][ny][nx]:
                            print('append')
                            Q.append([nz,ny,nx])
                            V[nz][ny][nx] = 1
                            new += 1
                if old == 0:
                    old += new
                    new = 0
                    cnt += 1
                    if cnt >= min_val:
                        break

    if min_val == 5*5*5:
        min_val = -1

    return min_val

answers = [ [] for _ in range(5) ]
for m in range(5):
    a, b, c, d = board_cases(maze[m])
    answers[m] = [a, b, c, d]
print(answers[4])
answers = maze_cases(answers)
answer = BFS(answers)
print(answer)




