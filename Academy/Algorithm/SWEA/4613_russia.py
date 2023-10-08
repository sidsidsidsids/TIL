'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 3개의 구간으로 나누기
    minV = 2500 # 임의의 최댓값
    for a in range(N-2): # W
        for b in range(a+1,N-1): # B
            cnt = 0 # 칠하는 횟수
            for i in range(0, a+1): # W 영역에서
                for j in range(M):
                    if arr[i][j] != 'W':
                        cnt += 1
            for i in range(a+1, b+1): # B 영역에서
                for j in range(M):
                    if arr[i][j] != 'B':
                        cnt += 1
            for i in range(b+1, N): # R 영역에서
                for j in range(M):
                    if arr[i][j] != 'R':
                        cnt += 1
            if cnt < minV:
                minV = cnt
    print(f'#{tc} {minV}')
'''


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    flag = [ input() for _ in range(N) ]

    minV = N*M
    for a in range(N-2):
        for b in range(a+1,N-1):
            cnt = 0
            for i in range(0,a+1):
                for j in range(M):
                    if flag[i][j] != 'W':
                        cnt += 1
            for i in range(a+1,b+1):
                for j in range(M):
                    if flag[i][j] != 'B':
                        cnt += 1
            for i in range(b+1,N):
                for j in range(M):
                    if flag[i][j] != 'R':
                        cnt += 1
            if cnt < minV:
                minV = cnt

    if minV == N*M:
        minV = -1

    print(f'#{tc} {minV}')
