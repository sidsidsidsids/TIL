'''
택시에서 가장 가까운 승객 찾는 BFS
그 승객을 태우고 목적지로 가는 함수
모든 승객을 데려다 줄 때의 남는 연료 출력
그렇지 못하면 -1 출력
(모든 손님 불가, 이동 도중 연료 바닥, 출발지나 목적지가 불가한 곳)
'''
N, M, fuel = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(N) ]
start_i, start_j = map(int,input().split())
passenger = [[] for _ in range(M)]
goal = [[] for _ in range(M)]
for i in range(M):
    a,b,c,d = map(int,input().split())
    passenger[i] = [a,b]
    goal[i] = [c,d]