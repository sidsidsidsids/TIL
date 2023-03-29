'''
1 : ㄴ
2 : 『
3 : ㄱ
4 : 』
5 : ㅁ
6~10 : 웜홀 (같은 숫자로 이동, 기존 방향 유지)
-1, 시작 지점 : 종료
'''

def pinball(i,j,idx):
    cnt = 0
    start_i = 0
    start_i += i
    start_j = 0
    start_j += j

    while True:
        ni,nj = move(i,j,idx)
        if 0 <= ni < N and 0 <= nj < N: # 다음 좌표가 grid 안일 때
            if ni == start_i and nj == start_j:
                break
            if grid[ni][nj] != 0:
                if 0 < grid[ni][nj] < 6: # 블록
                    if grid[ni][nj] == 1:
                        idx = block_1(idx)
                        cnt += 1
                    elif grid[ni][nj] == 2:
                        idx = block_2(idx)
                        cnt += 1
                    elif grid[ni][nj] == 3:
                        idx = block_3(idx)
                        cnt += 1
                    elif grid[ni][nj] == 4:
                        idx = block_4(idx)
                        cnt += 1
                    elif grid[ni][nj] == 5:
                        idx = block_5(idx)
                        cnt += 1

                elif grid[ni][nj] >= 6: # 웜홀
                    if grid[ni][nj] == 6:
                        inhole_idx = w_hole6.index([ni,nj])
                        if inhole_idx: # 인덱스가 1일 때
                            ni, nj = w_hole6[0][0], w_hole6[0][1]
                        else:
                            ni, nj = w_hole6[1][0], w_hole6[1][1]
                    elif grid[ni][nj] == 7:
                        inhole_idx = w_hole7.index([ni,nj])
                        if inhole_idx: # 인덱스가 1일 때
                            ni, nj = w_hole7[0][0], w_hole7[0][1]
                        else:
                            ni, nj = w_hole7[1][0], w_hole7[1][1]
                    elif grid[ni][nj] == 8:
                        inhole_idx = w_hole8.index([ni,nj])
                        if inhole_idx: # 인덱스가 1일 때
                            ni, nj = w_hole8[0][0], w_hole8[0][1]
                        else:
                            ni, nj = w_hole8[1][0], w_hole8[1][1]
                    elif grid[ni][nj] == 9:
                        inhole_idx = w_hole9.index([ni,nj])
                        if inhole_idx: # 인덱스가 1일 때
                            ni, nj = w_hole9[0][0], w_hole9[0][1]
                        else:
                            ni, nj = w_hole9[1][0], w_hole9[1][1]
                    elif grid[ni][nj] == 10:
                        inhole_idx = w_hole10.index([ni,nj])
                        if inhole_idx: # 인덱스가 1일 때
                            ni, nj = w_hole10[0][0], w_hole10[0][1]
                        else:
                            ni, nj = w_hole10[1][0], w_hole10[1][1]
                else: #블랙홀
                    break
            i = 0; j = 0
            i += ni; j += nj
        else: # 다음 좌표가 grid 밖일 때
            cnt += 1
            idx -= 2
            if idx < 0:
                idx += 4
            if i == start_i and j == start_j:
                break
            if grid[i][j] != 0:
                if 0 < grid[i][j] < 6: # 블록
                    if grid[i][j] == 1:
                        idx = block_1(idx)
                        cnt += 1
                    elif grid[i][j] == 2:
                        idx = block_2(idx)
                        cnt += 1
                    elif grid[i][j] == 3:
                        idx = block_3(idx)
                        cnt += 1
                    elif grid[i][j] == 4:
                        idx = block_4(idx)
                        cnt += 1
                    elif grid[i][j] == 5:
                        idx = block_5(idx)
                        cnt += 1
                elif grid[i][j] >= 6: # 웜홀
                    if grid[i][j] == 6:
                        inhole_idx = w_hole6.index([i,j])
                        if inhole_idx: # 인덱스가 1일 때
                            i, j = w_hole6[0][0], w_hole6[0][1]
                        else:
                            i, j = w_hole6[1][0], w_hole6[1][1]
                    elif grid[i][j] == 7:
                        inhole_idx = w_hole7.index([i,j])
                        if inhole_idx: # 인덱스가 1일 때
                            i, j = w_hole7[0][0], w_hole7[0][1]
                        else:
                            i, j = w_hole7[1][0], w_hole7[1][1]
                    elif grid[i][j] == 8:
                        inhole_idx = w_hole8.index([i,j])
                        if inhole_idx: # 인덱스가 1일 때
                            i, j = w_hole8[0][0], w_hole8[0][1]
                        else:
                            i, j = w_hole8[1][0], w_hole8[1][1]
                    elif grid[i][j] == 9:
                        inhole_idx = w_hole9.index([i,j])
                        if inhole_idx: # 인덱스가 1일 때
                            i, j = w_hole9[0][0], w_hole9[0][1]
                        else:
                            i, j = w_hole9[1][0], w_hole9[1][1]
                    elif grid[i][j] == 10:
                        inhole_idx = w_hole10.index([i,j])
                        if inhole_idx: # 인덱스가 1일 때
                            i, j = w_hole10[0][0], w_hole10[0][1]
                        else:
                            i, j = w_hole10[1][0], w_hole10[1][1]

    return cnt


def move(i,j,idx):
    if idx == 0:
        return i-1, j
    elif idx == 1:
        return i, j+1
    elif idx == 2:
        return i+1, j
    elif idx == 3:
        return i, j-1

def block_1(ball_idx):
    if ball_idx == 0:
        return 2
    elif ball_idx == 1:
        return 3
    elif ball_idx == 2:
        return 1
    elif ball_idx == 3:
        return 0

def block_2(ball_idx):
    if ball_idx == 0:
        return 1
    elif ball_idx == 1:
        return 3
    elif ball_idx == 2:
        return 0
    elif ball_idx == 3:
        return 2

def block_3(ball_idx):
    if ball_idx == 0:
        return 3
    elif ball_idx == 1:
        return 2
    elif ball_idx == 2:
        return 0
    elif ball_idx == 3:
        return 1

def block_4(ball_idx):
    if ball_idx == 0:
        return 2
    elif ball_idx == 1:
        return 0
    elif ball_idx == 2:
        return 3
    elif ball_idx == 3:
        return 1

def block_5(ball_idx):
    if ball_idx == 0:
        return 2
    elif ball_idx == 1:
        return 3
    elif ball_idx == 2:
        return 0
    elif ball_idx == 3:
        return 1

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    grid = [ list(map(int,input().split())) for _ in range(N) ]

    #웜홀 좌표 잡기
    w_hole6 = []
    w_hole7 = []
    w_hole8 = []
    w_hole9 = []
    w_hole10 = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] > 5:
                if grid[i][j] == 6:
                    w_hole6.append([i,j])
                elif grid[i][j] == 7:
                    w_hole7.append([i,j])
                elif grid[i][j] == 8:
                    w_hole8.append([i,j])
                elif grid[i][j] == 9:
                    w_hole9.append([i,j])
                elif grid[i][j] == 10:
                    w_hole10.append([i,j])

    #돌리기
    max_score = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if grid[i][j] == 0:
                    score = pinball(i,j,k)
                    #print('i:', i,'j:', j,'idx:', k,'score:', score)
                    if max_score < score:
                        max_score = score

    print(f'#{test_case}', max_score)


