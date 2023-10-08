def promising(i,j):
    for di, dj in [[-1,-1],[-1,0],[-1,1]]:
        ni, nj = i+di, j+dj
        while 0 <= ni < n and 0 <= nj < n:
            if board[ni][nj]: # 다른 퀸이 있으면
                return 0 # False
            ni, nj = ni+di, nj+dj
    return 1 # True
def f(i, N):
    global cnt
    if i == N: # N 개의 queen을 놓은 경우
        cnt += 1
    else:
        for j in range(N):
            if promising(i,j):
                board[i][j] = 1
                f(i+1, N)
                board[i][j] = 0

t = int(input())
for tc in range(1,1+t):
    n = int(input())
    board = [ [0]*n for _ in range(n) ]
    cnt = 0
    f(0,n)
    print(f'#{tc} {cnt}')