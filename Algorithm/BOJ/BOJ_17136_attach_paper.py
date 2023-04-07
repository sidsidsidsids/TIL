'''
큰 거 먼저 찾기
'''
from collections import deque

grid = [ list(map(int,input().split())) for _ in range(10) ]

board = [0, 0, 0, 0, 0]
ans = 26
V = [ [0]*10 for _ in range(10) ]

def attach(cnt):
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 1:
                able = DFS(i,j)
                cnt += able

    return cnt

def DFS(i,j,board):
    field_1 = [[i,j]]
    D = deque()
    D.append([i,j])
    V = [ [0] * 10 for _ in range(10) ]
    V[i][j] = 1

    while D:
        elem = D.pop()
        y, x = elem[0], elem[1]
        for ny, nx in [[y-1,x],[y,x+1],[y+1,x],[y,x-1]]:
            if 0 <= ny < 9 and 0 <= nx < 9:
                if not V[nx][ny] and grid[nx][ny] == 1:
                    D.append([ny,nx])
                    V[ny][nx] = 1
                    field_1.append([ny,nx])
'''
p_list 말고 len으로 받기 -> 거기에 따른 인덱스로 구하기
'''
def attaching(p_list, paper, p_board, cnt):
    for [y, x] in p_list:
        for k in range(4,-1,-1):
            able = True
            for ky in range(k):
                if not able:
                    break
                for kx in range(k):
                    if y + ky > 9 or x + kx > 9:
                        able = False
                        break
                    if paper[y+ky][x+kx] == 0:
                        able = False
                        break
            if able:
                for kky in range(y,y+k):
                    for kkx in range(x, x+k):
                        paper[kky][kkx] = 0
                p_board[k] += 1
                cnt += 1
                attaching()









'''
def attach(paper, stat, cnt, visit):
    global ans
    #print(cnt)

    if cnt >= ans:
        return

    for stat_n in range(5):
        if stat[stat_n] > 5:
            return

    check = 0
    for y in range(10):
        for x in range(10):
            check += paper[y][x]

    if check == 0:
        print(cnt)
        if ans > cnt:
            ans = cnt
            return

    elif check == 100:
        ans = 4
        return



    else:
        #print(stat, cnt)
        for i in range(10):
            for j in range(10):
                if paper[i][j] == 1 and not visit[i][j]:
                    # stat[0] += 1
                    # cnt += 1
                    # paper[i][j] = 0
                    # visit[i][j] = 1
                    # attach(paper, stat, cnt, visit)
                    # stat[0] -= 1
                    # cnt -= 1
                    # paper[i][j] = 1
                    # visit[i][j] = 0

                    for k in range(5,0,-1):
                        able = True
                        for ni in range(k):
                            if not able or i+ni > 9:
                                able = False
                                break
                            for nj in range(k):
                                if j+nj > 9 or paper[i+ni][j+nj] == 0:
                                    able = False
                                    break
                        if able:
                            stat[k-1] += 1
                            cnt += 1
                            for ki in range(k):
                                for kj in range(k):
                                    paper[i+ki][j+kj] = 0
                                    visit[i+ki][j+kj] = 1
                            attach(paper, stat, cnt, visit)
                            stat[k-1] -= 1
                            cnt -= 1
                            for ki in range(k):
                                for kj in range(k):
                                    paper[i+ki][j+kj] = 1
                                    visit[i + ki][j + kj] = 0
                        else:
                            continue
                else:
                    visit[i][j] = 1


attach(grid,board,0,V)

if ans == 26:
    print(-1)
else:
    print(ans)
'''

'''
def attach(board):
    global ans

    k = 10
    while True:
        for i in range(10-(k-1)):
            for j in range(10-(k-1)):
                if grid[i][j] == 1:
                    promising = True
                    for t in range(k):
                        if grid[i+t][j+t] == 0:
                            promising = False
                            break
                        else:
                            pass
                    if promising:
                        able = True
                        for ni in range(k):
                            if not able:
                                break
                            for nj in range(k):
                                if grid[i+ni][j+nj] == 0:
                                    able = False
                                    break
                        if able:
                            board[k-1] += 1
                            if board[k-1] > 5:
                                board[k-1] -= 1
                                continue
                            else:
                                for ai in range(k):
                                    for aj in range(k):
                                        grid[i+ai][j+aj] = 0
                                ans += 1
                        else:
                            continue
                    else:
                        continue
        k -= 1
        if k < 1:
            break

    for y in range(10):
        for x in range(10):
            if grid[y][x] == 1:
                return -1
    print(board)
    return ans

print(attach(board))
'''

'''
def attach(i,j):
    global board
    global ans

    k = 2
    s = 1
    # 붙일 종이 크기 판정
    while True:
        for i_k in range(k):
            if s == 0 :
                break
            for j_k in range(k):
                if grid[i+i_k][j+j_k] == 0:
                    s = 0
                    break
        if s == 0:
            break
        k += 1
        if k > 5:
            break
    # 붙일 종이 정했으면 리스트 반영
    k = k-1
    board[k-1] += 1
    # 붙인 곳 0으로
    for ik in range(k):
        for jk in range(k):
            grid[i+ik][j+jk] = 0
    # board 판정
    for b in range(5):
        if board[b] > 5:
            ans = -1
            return ans
    ans += 1
    return ans



ss = 1
for y in range(10):
    if ss == 0:
        break
    for x in range(10):
        if grid[y][x]:
            attach(y,x)
            if ans == -1:
                ss = 0
                break

if ss:
    print(ans)
else:
    print(-1)
'''
