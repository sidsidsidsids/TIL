M, N, H = map(int,input().split()) # 가로 세로 층높이
tomato = [ [ list(map(int,input().split()) ) for _ in range(N) ] for _ in range(H) ]

def infect(z,y,x):
    for a,b,c in [[z+1,y,x],[z-1,y,x],[z,y+1,x],[z,y-1,x],[z,y,x+1],[z,y,x-1]]:
        if 0 <= a < H and 0 <= b < N and 0 <= c < M:
            if tomato[a][b][c] == 0:
                tomato[a][b][c] = 2

def check_tomato():
    global s
    global change
    s = 0
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if tomato[k][i][j] == 2:
                    tomato[k][i][j] = 1
                    change = 1
                elif tomato[k][i][j] == 0:
                    s = 1

s = 1
time = 0

while s:
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if tomato[k][i][j] == 1:
                    infect(k,i,j)
    change = 0
    check_tomato()
    if change == 0:
        break
    time += 1

check_tomato()
if s == 1:
    print(-1)
else:
    print(time)