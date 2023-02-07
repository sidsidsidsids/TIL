test_case = int(input())
for tc in range(test_case):
    N, M = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N-M+1):
            garo = []
            for k in range(M):
                garo.append(board[i][j+k])
            if sum(garo) == M:
                if j+M >= N and board[i][j-1] == 0:
                    
                    cnt += 1
                elif j-1 < 0 and board[i][j+M] == 0:
                    
                    cnt += 1
                elif 0 <= j+M < N and 0 <= j-1 < N and board[i][j+M] == 0 and board[i][j-1] == 0:
                    
                    cnt += 1
                else:
                    
                    pass
    for j in range(N):
        for i in range(N-M+1):
            sero = []
            for k in range(M):
                sero.append(board[i+k][j])
            if sum(sero) == M:
                if i+M >= N and board[i-1][j] == 0:
                    cnt += 1
                elif i-1 < 0 and board[i+M][j] == 0:
                    cnt += 1
                elif 0 <= i+M < N and 0 <= i-1 < N and board[i+M][j] == 0 and board[i-1][j] == 0:
                    cnt += 1
                else:
                    pass

    print(f'#{tc+1} {cnt}')