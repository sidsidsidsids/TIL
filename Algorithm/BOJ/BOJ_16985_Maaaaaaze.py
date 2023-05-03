from collections import deque

maze = [[list(map(int,input().split())) for _ in range(5)] for __ in range(5)]

'''
구현할 거
- 판 돌리기
- 돌은 판에 따른 구현 가능 미로 4**5개
- 각 판에 대한 BFS
'''

# 왼쪽 맨 아래에서 부터 읽기
def spin_90(board):
    change_board = [[0]*5 for _ in range(5)]
    for j in range(5):
        for i in range(4,-1,-1):
            if board[i][j] == 1:
                change_board[j][4-i] = 1
            else:
                pass
    return change_board

def board_cases(board):
    c_board_1 = spin_90(board)
    c_board_2 = spin_90(c_board_1)
    c_board_3 = spin_90(c_board_2)
    return board, c_board_1, c_board_2, c_board_3

def maze_cases(boards):
    totalCase = [ [] for _ in range(4**5)]
    t_idx = 0
    maze_case = [ [] for _ in range(5) ]
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
                        totalCase[t_idx] = maze_case
                        t_idx += 1
    return totalCase

def BFS(mazes):
    for miro in mazes:
        if miro[0][0][0] == 1:
            Q = deque()
            Q.append([0,0,0])
            V = [[[0] * 5 for _ in range(5)] for __ in range(5)]
            V[0][0][0] = 1




