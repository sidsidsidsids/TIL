'''
출력 : 먹을 게 없어질 때까지 걸리는 시간

제약 : 아기 상어보다 큰 물고기는 벽으로 판별

먹을 수 있는 물고기 : 아기 상어 크기 미만의 물고기 (초기값 : 2)
자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가
(예: 처음에 2마리 먹으면 크기가 3이 되고 여기서 3마리 먹으면 4)
먹을 수 있는 물고기가 1마리면 그 물고기를 먹는다
먹을 수 있는 물고기가 1마리 초과이면 가장 가까운 거
(단 가장 위에 있는 물고기, y가 같으면 가장 왼쪽에 있는 물고기)
'''
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
ocean = [ list(map(int,input().split())) for _ in range(N) ]

for i in range(N):
    for j in range(N):
        if ocean[i][j] == 9:
            start_i = i
            start_j = j
            ocean[i][j] = 0

def baby_shark(i,j,size):
    cnt = 0
    target = []
    for r in range(N):
        for c in range(N):
            if 0 < ocean[r][c] < size:
                target.append([r,c])

    Q = deque()
    Q.append([i,j])
    V = [ [0]*N for _ in range(N) ]
    V[i][j] = 1
    old = 1
    new = 0
    try_to_eat = []

    while Q:
        elem = Q.popleft()
        y, x = elem[0], elem[1]
        old -= 1
        for ny, nx in [[y+1,x],[y-1,x],[y,x+1],[y,x-1]]:
            if 0 <= ny < N and 0 <= nx < N:
                if V[ny][nx] == 0 and ocean[ny][nx] <= size:
                    if [ny, nx] in target:
                        try_to_eat.append([ny,nx])
                    else:
                        Q.append([ny,nx])
                        V[ny][nx] = 1
                        new += 1

        if old == 0:
            if try_to_eat:
                try_to_eat.sort(key=lambda X: (X[0], X[1]))
                ocean[try_to_eat[0][0]][try_to_eat[0][1]] = 0
                return try_to_eat[0][0], try_to_eat[0][1], cnt + 1
            old += new
            new = 0
            cnt += 1
    return False

size = 2
eat = 0
answer = 0

while True:
    result = baby_shark(start_i,start_j,size)
    if result:
        eat += 1
        if eat == size:
            size += 1
            eat = 0
        start_i = result[0]
        start_j = result[1]
        answer += result[2]
    else:
        break

print(answer)

