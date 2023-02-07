test_case = int(input())
for tc in range(test_case):
    N, M = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N-M):
            if sum(board[i][j:j+M]) == M:
                if j+M+1 > N or j-1 < 0:
                    cnt += 1
                elif board[i][j+M+1] == 0 and board[i][j-1] == 0:
                    cnt += 1
                else:
                    pass

    print(cnt)