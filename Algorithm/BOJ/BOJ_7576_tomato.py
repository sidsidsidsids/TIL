import sys
input = sys.stdin.readline
from collections import deque


M, N, = map(int,input().split()) # 가로 세로 층높이
tomato =[ list(map(int,input().split()) ) for _ in range(N) ]

ripen = []
w_cnt = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            ripen.append([i,j])
        elif tomato[i][j] == -1:
            w_cnt += 1

def ripping(lists):
    Q = deque()
    for l in lists:
        Q.append(l)
    # Q = [*lists]
    V = [ [0]*M for _ in range(N) ]
    for y, x in Q:
        V[y][x] = 1
    old = len(Q)
    new = 0
    cnt = 1
    maxima = 0

    while Q:
        elem = Q.popleft()
        y, x = elem[0], elem[1]
        old -= 1

        for ny, nx in [[y-1,x],[y,x+1],[y+1,x],[y,x-1]]:
            if 0 <= ny < N and 0 <= nx < M:
                if V[ny][nx] == 0 and tomato[ny][nx] == 0:
                    V[ny][nx] = cnt
                    maxima = V[ny][nx]
                    Q.append([ny,nx])
                    new += 1

        if old == 0:
            old = new
            new = 0
            cnt += 1

    cnt_0 = 0
    for b in range(N):
        for c in range(M):
            if V[b][c] == 0:
                cnt_0 += 1

    if w_cnt == cnt_0:
        return maxima
    else:
        if any(0 in row for row in tomato):
            return -1
        else:
            return 0

print(ripping(ripen))