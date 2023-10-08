'''
큰 거 먼저 찾기
'''
from collections import deque

grid = [ list(map(int,input().split())) for _ in range(10) ]

s_board = [0, 0, 0, 0, 0]
V = [ [0]*10 for _ in range(10) ]
tmp_min = 0
tmp_board = []
tmp_paper = []

def attach(cnt,board,gridd):
    for i in range(10):
        for j in range(10):
            if gridd[i][j] == 1:
                DFS(i,j,board,gridd)
                cnt += tmp_min
                board = tmp_board
                gridd = tmp_paper
    return cnt

def DFS(i,j,score,gride):
    global tmp_min
    global tmp_board
    global tmp_paper

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
                if not V[ny][nx] and grid[ny][nx] == 1:
                    D.append([ny,nx])
                    V[ny][nx] = 1
                    field_1.append([ny,nx])

    tmp_min = 26
    tmp_board = []
    tmp_paper = []

    target_len = len(field_1)
    init_len = 0
    way_cnt = 0
    size = 1
    attaching(field_1, init_len, target_len, size, way_cnt, score, gride)
    return
'''
p_list 말고 len으로 받기 -> 거기에 따른 인덱스로 구하기
'''
def attaching(dotlist,s,e,k,cnt,scoreboard,paper):
    global tmp_min
    global tmp_board
    global tmp_paper
    if k > 5:
        return
    if cnt > tmp_min:
        return
    if s==e:
        if cnt < tmp_min:
            tmp_min = cnt
            tmp_board = scoreboard
            tmp_paper = paper
            return
        return
    else:
        y, x = dotlist[s][0], dotlist[s][1]
        print(y,x)
        if paper[y][x] == 1:
            able = True
            for ky in range(k):
                if y+ky > 9 or not able:
                    break
                for kx in range(k):
                    if x+kx > 9 or paper[y+ky][x+kx] == 0:
                        able = False
                        break
            if able:
                for ny in range(k):
                    for nx in range(k):
                        paper[y+ny][x+nx] = 0
                scoreboard[k-1] += 1
                cnt += 1
                if scoreboard[k-1] > 5:
                    return
                else:
                    attaching(dotlist,s+1,e,k+1,cnt,scoreboard,paper)
                    for ny in range(k):
                        for nx in range(k):
                            paper[y + ny][x + nx] = 0
                    scoreboard[k - 1] -= 1
                    cnt -= 1
            else:
                return
        else:
            attaching(dotlist,s+1,e,1,cnt,scoreboard,paper)

ans = attach(0,s_board,grid)
print(ans)











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
