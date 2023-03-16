from itertools import combinations

N, M = map(int,input().split())
lab = [ list(map(int,input().split())) for _ in range(N) ]

M_grid = []
w_cnt = 0
#v_cnt = 0

for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            M_grid.append([i, j])
            #v_cnt += 1
        elif lab[i][j] == 1:
            w_cnt += 1

subset = list(combinations(M_grid,M))

def BFS(a):
    Q = [*a]
    v = [ [0]*N for _ in range(N) ]
    max_val = 0
    oldQ = len(Q)
    newQ = 0
    cnt = 1

    while Q:
        loc = Q.pop(0)
        y, x = loc[0], loc[1]
        if v[y][x] == 0:
            v[y][x] = 1
        oldQ -= 1

        for ny, nx in [[y+1,x],[y-1,x],[y,x+1],[y,x-1]]:
            if 0 <= ny < N and 0 <= nx < N:
                if v[ny][nx] == 0 and lab[ny][nx] != 1:
                    if lab[ny][nx] == 2:
                        v[ny][nx] = -1
                    else:
                        v[ny][nx] += cnt
                        max_val = v[ny][nx]
                    Q.append([ny,nx])
                    newQ += 1

        if oldQ == 0:
            oldQ += newQ
            newQ = 0
            cnt += 1

    cnt_0 = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                cnt_0 += 1

    if cnt_0 != w_cnt:
        return -1
    else:
        if N**2 - w_cnt == M:
            return 0
        else:
            return max_val

m = 10000

for i in subset:
    ans = BFS(i)
    if ans == -1:
        continue
    if ans < m:
        m = ans

if m == 10000:
    print(-1)
else:
    print(m)
