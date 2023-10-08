from collections import deque

I, J = map(int,input().split())
cheese = [ list(map(int,input().split())) for _ in range(I) ]

def find_target():
    Q = deque()
    Q.append([0,0])
    V = [ [0]*J for _ in range(I) ]
    V[0][0] = 1
    target = []
    while Q:
        elem = Q.popleft()
        i, j = elem[0], elem[1]
        for ni, nj in [[i-1,j],[i,j+1],[i+1,j],[i,j-1]]:
            if 0 <= ni < I and 0 <= nj < J:
                if cheese[ni][nj] == 0 and V[ni][nj] == 0:
                    Q.append([ni,nj])
                    V[ni][nj] = 1
                elif cheese[ni][nj] == 1 and V[ni][nj] == 0:
                    target.append([ni,nj])
                    V[ni][nj] = 1
    return target

ans = 0
while True:
    targets = find_target()
    for y,x in targets:
        cheese[y][x] = 0
    ans += 1
    s = 1
    for i in range(I):
        if s == 0:
            break
        for j in range(J):
            if cheese[i][j] == 1:
                s = 0
                break
    if s == 1:
        break

print(ans)
print(len(targets))