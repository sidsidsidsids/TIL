test_case = int(input())
for tc in range(1,test_case+1):
    N = int(input())
    board = [ list(map(str,input())) for _ in range(N) ]

    ans = "NO"

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                # 세로
                cnt = 0
                for k in range(5):
                    if i + k == N:
                        break
                    else:
                        if board[i + k][j] == 'o':
                            cnt += 1
                if cnt == 5:
                    ans = "YES"
                    break

                # 가로
                cnt = 0
                for k in range(5):
                    if j + k == N:
                        break
                    else:
                        if board[i][j + k] == 'o':
                            cnt += 1
                if cnt == 5:
                    ans = "YES"
                    break

                # 대각 1
                cnt = 0
                for k in range(5):
                    if i+k == N or j+k == N:
                        break
                    else:
                        if board[i+k][j+k] == 'o':
                            cnt += 1
                if cnt == 5:
                    ans = "YES"
                    break

                # 대각 2
                cnt = 0
                for k in range(5):
                    if i + k == N or j - k == -1:
                        break
                    else:
                        if board[i + k][j - k] == 'o':
                            cnt += 1
                if cnt == 5:
                    ans = "YES"
                    break


    print(f'#{tc} {ans}')