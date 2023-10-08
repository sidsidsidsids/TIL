'''
택시에서 가장 가까운 승객 찾는 BFS
그 승객을 태우고 목적지로 가는 함수
모든 승객을 데려다 줄 때의 남는 연료 출력
그렇지 못하면 -1 출력
(모든 손님 불가, 이동 도중 연료 바닥, 출발지나 목적지가 불가한 곳)
'''
import sys
input = sys.stdin.readline
from collections import deque

N, M, fuel = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(N) ]
start_i, start_j = map(int,input().split())
start_i -= 1; start_j -= 1
passenger = [[] for _ in range(M)]
goal = [[] for _ in range(M)]
for i in range(M):
    a,b,c,d = map(int,input().split())
    passenger[i] = [a-1,b-1]
    goal[i] = [c-1,d-1]

def finding_passenger(si,sj):
    global fuel

    if [si, sj] in passenger:
        return [si, sj]

    Q = deque()
    Q.append([si,sj])
    V = [ [0]*N for _ in range(N) ]
    old = 1
    new = 0
    V[si][sj] = 1
    target = []

    while Q:
        move = Q.popleft()
        y,x = move[0],move[1]
        old -= 1
        for ny,nx in [[y-1,x],[y,x-1],[y,x+1],[y+1,x]]:
            if 0 <= ny < N and 0 <= nx < N:
                if V[ny][nx] == 0 and grid[ny][nx] != 1:
                    if [ny, nx] in passenger:
                        target.append([ny, nx])
                        V[ny][nx] = 1
                    else:
                        Q.append([ny, nx])
                        V[ny][nx] = 1
                        new += 1

        if old == 0:
            old = new
            new = 0
            fuel -= 1
            if target:
                target.sort(key=lambda X :(X[0],X[1]))
                return target[0]

        if fuel == 0:
            return False

def drive_to_goal(si,sj):
    global fuel

    goal_idx = passenger.index([si,sj])
    goal_i, goal_j = goal[goal_idx][0], goal[goal_idx][1]
    passenger[goal_idx] = [-2,-2]
    goal[goal_idx] = [-2,-2]
    reward = 0

    if si == goal_i and sj == goal_j:
        return 0, si, sj

    Q = deque()
    Q.append([si, sj])
    V = [[0] * N for _ in range(N)]
    old = 1
    new = 0
    V[si][sj] = 1

    while Q:
        move = Q.popleft()
        y,x = move[0],move[1]
        old -= 1
        for ny,nx in [[y-1,x],[y,x-1],[y,x+1],[y+1,x]]:
            if 0 <= ny < N and 0 <= nx < N:
                if V[ny][nx] == 0 and grid[ny][nx] != 1:
                    if ny == goal_i and nx == goal_j:
                        fuel -= 1
                        return reward+1, ny, nx
                    else:
                        Q.append([ny, nx])
                        V[ny][nx] = 1
                        new += 1

        if old == 0:
            old = new
            new = 0
            fuel -= 1
            reward += 1

        if fuel == 0:
            return False

available = 1
for _ in range(M):
    finding = finding_passenger(start_i,start_j)
    if finding:
        drive = drive_to_goal(finding[0],finding[1])
        if drive:
            fuel += drive[0]*2
            start_i = drive[1]
            start_j = drive[2]
        else:
            available = 0
            break
    else:
        available = 0
        break

if available:
    print(fuel)
else:
    print(-1)

