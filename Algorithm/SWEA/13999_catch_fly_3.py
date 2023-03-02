# def spray(board,M):
#     pass


test_case = int(input())
for tc in range(1,test_case+1):
    N, M = map(int,input().split())
    grid = [ list(map(int,input().split())) for _ in range(N) ]


    kill_max = 0

    for i in range(N):
        for j in range(N):
            # 십자 스프레이
            kill_cnt = 0
            for k in range(-(M-1), (M-1)+1):
                if 0 <= j+k < N:
                    kill_cnt += grid[i][j+k]
                if 0 <= i+k < N:
                    kill_cnt += grid[i+k][j]
            kill_cnt -= grid[i][j]
            if kill_max < kill_cnt:
                kill_max = kill_cnt

            # 엑스자 스프레이
            kill_cnt = 0
            for k in range(-(M - 1), (M - 1) + 1):
                if 0 <= i + k < N and 0 <= j + k < N:
                    kill_cnt += grid[i + k][j + k]
                if 0 <= i+k < N and 0 <= j - k < N:
                    kill_cnt += grid[i + k][j - k]
            kill_cnt -= grid[i][j]
            if kill_max < kill_cnt:
                kill_max = kill_cnt

    print(f'#{tc} {kill_max}')
