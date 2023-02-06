test_case = int(input())
test_cnt = 1
for _ in range(test_case):
    N = int(input())
    squares = [list(map(int,input().split())) for _ in range(N)]
    total_sum = 0
    for i in range(N):
        for j in range(N):
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni, nj = i + di, j + dj # 모든 좌표에 대해서 상하좌우 이동시킨 좌표
                if 0 <= ni < N and 0 <= nj < N: # 이동한 좌표가 지정 구역 안에 있다면
                    total_sum += abs(squares[i][j] - squares[ni][nj]) # 차 합산
    print(f'#{test_cnt} {total_sum}')
    test_cnt += 1