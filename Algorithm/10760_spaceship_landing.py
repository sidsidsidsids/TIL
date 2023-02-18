T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    photo = [ list(map(int,input().split())) for _ in range(N)]

    candidate = 0

    for i in range(N):
        for j in range(M):
            search_range = [ [i-1, j-1],[i-1, j],[i-1, j+1],[i, j-1],[i, j+1],[i+1, j-1],[i+1, j],[i+1, j+1] ]
            cnt = 0
            for y, x in search_range:
                if 0 <= y < N and 0 <= x < M:
                    if photo[i][j] > photo[y][x]:
                        cnt += 1
            if cnt >= 4:
                candidate += 1
    
    print(f'#{tc} {candidate}')
