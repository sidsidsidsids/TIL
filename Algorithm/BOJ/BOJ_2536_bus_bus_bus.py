from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int,input().split())
b = int(input())
bus = [ [] for _ in range(b+1) ]

for _ in range(b):
    i, sx, sy, ex, ey = map(int,input().split())
    if sx > ex:
        sx, ex = ex, sx
    if sy > ey:
        sy, ey = ey, sy
    bus[i] = [[sx,sy],[ex,ey]]

start_x, start_y, end_x, end_y = map(int,input().split())
if start_x > end_x:
    start_x, end_x = end_x, start_x
if start_y > end_y:
    start_y, end_y = end_y, start_y

def hwanseung(idx):

    next = []

    if bus[idx][0][0] == bus[idx][1][0]: # 세로 버스일 때
        for n in range(1,b+1):
            if idx != n:
                # 가로 버스
                if bus[n][0][1] == bus[n][1][1]:
                    if bus[n][0][0] <= bus[idx][0][0] and bus[idx][0][0] <= bus[n][1][0] and bus[idx][0][1] <= bus[n][0][1] <= bus[idx][1][1]:
                        next.append(n)
                # 세로 버스
                elif bus[n][0][0] == bus[n][1][0]:
                    if (bus[idx][0][1] <= bus[n][0][1] <= bus[idx][1][1] and bus[idx][1][1] < bus[n][1][1]) or (bus[n][0][1] < bus[idx][0][1] and bus[idx][0][1] <= bus[n][1][1] <= bus[idx][1][1]):
                        next.append(n)

    else: # 가로 버스일 때
        for n in range(1,b+1):
            if idx != n:
                # 가로 버스
                if bus[n][0][1] == bus[n][1][1]:
                    if (bus[idx][0][0] <= bus[n][0][0] <= bus[idx][1][0] and bus[idx][1][0] < bus[n][1][0]) or (bus[n][0][0] < bus[idx][0][0] and bus[idx][0][0] <= bus[n][1][0] <= bus[idx][1][0]):
                        next.append(n)
                # 세로 버스
                elif bus[n][0][0] == bus[n][1][0]:
                    if bus[n][0][1] <= bus[idx][0][1] and bus[idx][0][1] <= bus[n][1][1] and bus[idx][0][0] <= bus[n][0][0] <= bus[idx][1][0]:
                        next.append(n)

    return next




def BFS(indexes):
    Q = deque()
    V = [0] * (b+1)
    for index in indexes:
        Q.append(index)
        V[index] = 1

    old = len(indexes)
    new = 0
    cnt = 0

    while Q:
        elem = Q.popleft()
        old -= 1
        next = hwanseung(elem)
        for nex in next:
            if bus[nex][0][0] <= end_x <= bus[nex][1][0] and bus[nex][0][1] <= end_y <= bus[nex][1][1]:
                cnt += 1
                return cnt
            if not V[nex]:
                Q.append(nex)
                new += 1
                V[nex] = 1

    if old == 0:
        old += new
        new = 0
        cnt += 1

start = []
for q in range(1,b+1):
    if bus[q][0][0] <= start_x <= bus[q][1][0] and bus[q][0][1] <= start_y <= bus[q][1][1]:
        start.append(q)

print(BFS(start))





'''
for _ in range(b):
    i, sx, sy, ex, ey = map(int,input().split())
    if sx == ex: # 세로로 움직이는 버스일 경우
        dist = abs(ey - sy) + 1
        bus[i] = [0] * dist
        if sy < ey:
            for k in range(dist):
                bus[i][k] = [sx,sy+k]
        else:
            for k in range(dist):
                bus[i][k] = [sx,sy-k]
    else: # 가로로 움직이는 버스일 경우
        dist = abs(ex - sx) + 1
        bus[i] = [0] * dist
        if sx < ex:
            for k in range(dist):
                bus[i][k] = [sx+k,sy]
        else:
            for k in range(dist):
                bus[i][k] = [sx-k,sy]

start_x, start_y, end_x, end_y = map(int,input().split())

#print(bus)

# BFS
# 멈출 곳 찾기
# 갈 수 있는 곳 중에 다른 노선으로 갈아탈 수 있거나 목적지이면 갈 수 있도록

def bus_route(j,i,n):
    target = []
    for l in range(b+1):
        if n != l and [j,i] in bus[l]:
            target.append(l)
    return target

def BFS(j,i,bn):
    Q = deque()
    V = [ [0] * (n+1) for _ in range(m+1) ]
    Q.append([j,i,bn])
    V[j][i] = 1
    old = 1
    new = 0
    cnt = 0

    while Q:
        elem = Q.popleft()
        old -= 1
        x,y = elem[0], elem[1]
        #print(x,y)
        able_bus = bus_route(x, y, bn)
        #print([x,y],able_bus)
        for idx in able_bus:
            for [nx,ny] in bus[idx]:
                #print(bus[idx])
                if nx == end_x and ny == end_y:
                    #print(nx,ny)
                    cnt += 1
                    return cnt
                #print(nx,ny)
                b_cnt = 0
                for l in range(b+1):
                    if [nx,ny] in bus[l]:
                        b_cnt += 1
                if b_cnt > 1:
                    if not V[nx][ny]:
                        Q.append([nx,ny,idx])
                        V[nx][ny] = 1
                        new += 1
                    else:
                        pass
        if old == 0:
            #print(Q)
            old += new
            new = 0
            cnt += 1
a = BFS(start_x,start_y,0)
print(a)
'''


