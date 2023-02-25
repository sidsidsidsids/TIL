test_case = int(input())
for tc in range(1,test_case+1):
    N, M = map(int,input().split())
    grid = [ list(map(int,input().split())) for _ in range(N) ]
    longest = 0; k=0

    # 가로
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and (j-1 < 0 or grid[i][j-1] == 0):
                while j+k < M:
                    if grid[i][j+k] == 1:
                        k += 1
                    else:
                        break
                if k > longest:
                    longest = k
                k = 0

    # 세로
    for j in range(M):
        for i in range(N):
            if grid[i][j] == 1 and (i-1 < 0 or grid[i-1][j] == 0):
                while i+k < N:
                    if grid[i+k][j] == 1:
                        k += 1
                    else:
                        break
                if k > longest:
                    longest = k
                k = 0
    
    print(f'#{tc} {longest}')