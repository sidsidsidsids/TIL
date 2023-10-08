import sys
input = sys.stdin.readline
from collections import deque


M, N, H = map(int,input().split()) # 가로 세로 층높이
tomato = [ [ list(map(int,input().split()) ) for _ in range(N) ] for _ in range(H) ]

ripen = []
w_cnt = 0

for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[k][i][j] == 1:
                ripen.append([k,i,j])
            elif tomato[k][i][j] == -1:
                w_cnt += 1

def ripping(lists):
    Q = deque()
    for l in lists:
        Q.append(l)
    # Q = [*lists]
    V = [ [ [0]*M for _ in range(N) ] for _ in range(H) ]
    for z, y, x in Q:
        V[z][y][x] = 1
    old = len(Q)
    new = 0
    cnt = 1
    maxima = 0

    while Q:
        elem = Q.popleft()
        z, y, x = elem[0], elem[1], elem[2]
        old -= 1

        for nz, ny, nx in [[z+1,y,x],[z-1,y,x],[z,y+1,x],[z,y-1,x],[z,y,x+1],[z,y,x-1]]:
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                if V[nz][ny][nx] == 0 and tomato[nz][ny][nx] == 0:
                    V[nz][ny][nx] = cnt
                    maxima = V[nz][ny][nx]
                    Q.append([nz,ny,nx])
                    new += 1

        if old == 0:
            old = new
            new = 0
            cnt += 1

    cnt_0 = 0
    for a in range(H):
        for b in range(N):
            for c in range(M):
                if V[a][b][c] == 0:
                    cnt_0 += 1

    if w_cnt == cnt_0:
        return maxima
    else:
        if any(0 in row for row in tomato):
            return 0
        else:
            return -1

print(ripping(ripen))
