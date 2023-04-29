from collections import deque

N, M = map(int,input().split())
board = [ list(input()) for _ in range(N) ]

R_init = []
B_init = []
goal = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            R_init = [i,j]
        elif board[i][j] == 'B':
            B_init = [i,j]
        elif board[i][j] == 'O':
            goal = [i,j]

def move_left(Ry,Rx,By,Bx,fail,success,memo):
    if Rx <= Bx:
        while board[Ry][Rx-1] != '#':
            Rx -= 1
            if Ry == goal[0] and Rx == goal[1]:
                Rx = 0;
                Ry = 0
                success = True
                break
        while board[By][Bx - 1] != '#' and not (Bx - 1 == Rx and By == Ry):
            Bx -= 1
            if By == goal[0] and Bx == goal[1]:
                Bx = 0
                By = 0
                fail = True
                break
    else:
        while board[By][Bx - 1] != '#':
            Bx -= 1
            if By == goal[0] and Bx == goal[1]:
                Bx = 0
                By = 0
                fail = True
                break
        while board[Ry][Rx-1] != '#' and not (Rx - 1 == Bx and By == Ry):
            Rx -= 1
            if Ry == goal[0] and Rx == goal[1]:
                Rx = 0;
                Ry = 0
                success = True
                break
    return [Ry,Rx,By,Bx,fail,success,memo+'L']

def move_right(Ry,Rx,By,Bx,fail,success,memo):
    if Bx <= Rx:
        while board[Ry][Rx+1] != '#':
            Rx += 1
            if Ry == goal[0] and Rx == goal[1]:
                Rx = 0;
                Ry = 0
                success = True
                break
        while board[By][Bx+1] != '#' and not (Bx+1 == Rx and By == Ry):
            Bx += 1
            if By == goal[0] and Bx == goal[1]:
                Bx = 0
                By = 0
                fail = True
                break
    else:
        while board[By][Bx+1] != '#':
            Bx += 1
            if By == goal[0] and Bx == goal[1]:
                Bx = 0
                By = 0
                fail = True
                break
        while board[Ry][Rx+1] != '#' and not (Rx+1 == Bx and By == Ry):
            Rx += 1
            if Ry == goal[0] and Rx == goal[1]:
                Rx = 0;
                Ry = 0
                success = True
                break
    return [Ry,Rx,By,Bx,fail,success,memo+'R']

def move_top(Ry,Rx,By,Bx,fail,success,memo):
    if By >= Ry:
        while board[Ry-1][Rx] != '#':
            Ry -= 1
            if Ry == goal[0] and Rx == goal[1]:
                Rx = 0; Ry = 0
                success = True
                break
        while board[By-1][Bx] != '#' and not (By - 1 == Ry and Bx == Rx):
            By -= 1
            if By == goal[0] and Bx == goal[1]:
                Bx = 0
                By = 0
                fail = True
                break
    else:
        while board[By-1][Bx] != '#':
            By -= 1
            if By == goal[0] and Bx == goal[1]:
                Bx = 0
                By = 0
                fail = True
                break
        while board[Ry-1][Rx] != '#' and not (Ry - 1 == By and Bx == Rx):
            Ry -= 1
            if Ry == goal[0] and Rx == goal[1]:
                Rx = 0;
                Ry = 0
                success = True
                break
    return [Ry,Rx,By,Bx,fail,success,memo+'U']

def move_down(Ry,Rx,By,Bx,fail,success,memo):
    if Ry >= By:
        while board[Ry+1][Rx] != '#':
            Ry += 1
            if Ry == goal[0] and Rx == goal[1]:
                Rx = 0;
                Ry = 0
                success = True
                break
        while board[By+1][Bx] != '#' and not (By + 1 == Ry and Bx == Rx):
            By += 1
            if By == goal[0] and Bx == goal[1]:
                Bx = 0
                By = 0
                fail = True
                break
    else:
        while board[By+1][Bx] != '#':
            By += 1
            if By == goal[0] and Bx == goal[1]:
                Bx = 0
                By = 0
                fail = True
                break
        while board[Ry+1][Rx] != '#' and not (Ry + 1 == By and Bx == Rx):
            Ry += 1
            if Ry == goal[0] and Rx == goal[1]:
                Rx = 0;
                Ry = 0
                success = True
                break
    return [Ry,Rx,By,Bx,fail,success,memo+'D']

def BFS(red_y,red_x,blue_y,blue_x,failure,succession,memory):
    Q = deque()
    Q.append([red_y, red_x, blue_y, blue_x, False, False, memory])

    visit = [[0] * M for _ in range(N)]
    visit[red_y][red_x] = 1
    # visit[blue_y][blue_x] = -1

    cnt = 0
    old = 1
    new = 0

    while Q:
        elem = Q.popleft()
        r_ny, r_nx, b_ny, b_nx, nf, ns, m = elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6]
        old -= 1
        for ry, rx, by, bx, nfail, nsuccess, nm in [move_down(r_ny,r_nx,b_ny,b_nx, nf, ns, m),move_top(r_ny,r_nx,b_ny,b_nx, nf, ns, m),move_left(r_ny,r_nx,b_ny,b_nx, nf, ns, m),move_right(r_ny,r_nx,b_ny,b_nx, nf, ns, m)]:
            # print('elem: ', [ry, rx, by, bx, nfail, nsuccess], cnt)
            if nsuccess and not nfail:
                # print('finish: ', [ry, rx, by, bx, nfail, nsuccess])
                return [cnt + 1, nm]
            else:
                if visit[ry][rx] < 1000 and not nfail:
                    # print('appendQ: ', [ry, rx, by, bx, nfail, nsuccess], cnt+1)
                    Q.append([ry, rx, by, bx, nfail, nsuccess, nm])
                    visit[ry][rx] += 1
                    new += 1

        if old == 0:
            old += new
            new = 0
            cnt += 1
            if cnt == 10:
                # print('cntover10')
                return -1
    # print('emptyQ')
    return -1

result = BFS(R_init[0],R_init[1],B_init[0],B_init[1],False,False,'')

if result == -1:
    print(result)
else:
    print(result[0])
    print(result[1])
