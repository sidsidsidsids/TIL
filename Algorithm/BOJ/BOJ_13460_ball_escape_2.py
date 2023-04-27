from collections import deque

N, M = map(int,input().split())
board = [ list(input()) for _ in range(N) ]

R_init = []
B_init = []
goal = []
R_goal = False
B_goal = False

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            R_init = [i,j]
        elif board[i][j] == 'B':
            B_init = [i,j]
        elif board[i][j] == 'O':
            goal = [i,j]

def move_left(Ry,Rx,By,Bx):
    global R_goal
    global B_goal
    if Rx <= Bx:
        while board[Ry][Rx-1] != '#':
            Rx -= 1
            if Ry == goal[0] and Rx == goal[1]:
                R_goal = True
                break
        while board[By][Bx - 1] != '#' and Bx - 1 != Rx:
            Bx -= 1
            if By == goal[0] and Bx == goal[1]:
                B_goal = True
                break
    else:
        while board[By][Bx - 1] != '#':
            Bx -= 1
            if By == goal[0] and Bx == goal[1]:
                B_goal = True
                break
        while board[Ry][Rx-1] != '#' and Rx - 1 != Bx:
            Rx -= 1
            if Ry == goal[0] and Rx == goal[1]:
                R_goal = True
                break
    return [Ry,Rx,By,Bx]

def move_right(Ry,Rx,By,Bx):
    global R_goal
    global B_goal
    if Bx <= Rx:
        while board[Ry][Rx+1] != '#':
            Rx += 1
            if Ry == goal[0] and Rx == goal[1]:
                R_goal = True
                break
        while board[By][Bx+1] != '#' and Bx+1 != Rx:
            Bx += 1
            if By == goal[0] and Bx == goal[1]:
                B_goal = True
                break
    else:
        while board[By][Bx+1] != '#':
            Bx += 1
            if By == goal[0] and Bx == goal[1]:
                B_goal = True
                break
        while board[Ry][Rx+1] != '#' and Rx+1 != Bx:
            Rx += 1
            if Ry == goal[0] and Rx == goal[1]:
                R_goal = True
                break
    return [Ry,Rx,By,Bx]

def move_top(Ry,Rx,By,Bx):
    global R_goal
    global B_goal
    if By <= Ry:
        while board[Ry-1][Rx] != '#':
            Ry -= 1
            if Ry == goal[0] and Rx == goal[1]:
                R_goal = True
                break
        while board[By-1][Bx] != '#' and By - 1 != Ry:
            By -= 1
            if By == goal[0] and Bx == goal[1]:
                B_goal = True
                break
    else:
        while board[By-1][Bx] != '#':
            By -= 1
            if By == goal[0] and Bx == goal[1]:
                B_goal = True
                break
        while board[Ry-1][Rx] != '#' and Ry - 1 != By:
            Ry -= 1
            if Ry == goal[0] and Rx == goal[1]:
                R_goal = True
                break
    return [Ry,Rx,By,Bx]

def move_down(Ry,Rx,By,Bx):
    global R_goal
    global B_goal
    if Ry <= By:
        while board[Ry+1][Rx] != '#':
            Ry += 1
            if Ry == goal[0] and Rx == goal[1]:
                R_goal = True
                break
        while board[By+1][Bx] != '#' and By + 1 != Ry:
            By += 1
            if By == goal[0] and Bx == goal[1]:
                B_goal = True
                break
    else:
        while board[By+1][Bx] != '#':
            By += 1
            if By == goal[0] and Bx == goal[1]:
                B_goal = True
                break
        while board[Ry+1][Rx] != '#' and Ry + 1 != By:
            Ry += 1
            if Ry == goal[0] and Rx == goal[1]:
                R_goal = True
                break
    return [Ry,Rx,By,Bx]

def BFS(red_y,red_x,blue_y,blue_x):
    global R_goal
    global B_goal
    Q = deque()
    Q.append([red_y, red_x, blue_y, blue_x])

    visit = [[0] * M for _ in range(N)]
    visit[red_y][red_x] = 1
    visit[blue_y][blue_x] = -1

    cnt = 0
    old = 1
    new = 0

    while Q:
        elem = Q.popleft()
        old -= 1
        r_ny, r_nx, b_ny, b_nx = elem[0], elem[1], elem[2], elem[3]
        for ry, rx, by, bx in [move_down(r_ny,r_nx,b_ny,b_nx),move_top(r_ny,r_nx,b_ny,b_nx),move_left(r_ny,r_nx,b_ny,b_nx),move_right(r_ny,r_nx,b_ny,b_nx)]:
            if B_goal:
                return -1
            if R_goal and not B_goal:
                return cnt + 1
            else:
                if visit[ry][rx] != 1:
                    Q.append([ry, rx, by, bx])
                    new += 1

        if old == 0:
            old += new
            new = 0
            cnt += 1

print(BFS(R_init[0],R_init[1],B_init[0],B_init[1]))
