# import sys
# sys.setrecursionlimit(10000)
#
# N = int(input())
# adjC = [ [0] * (N+1) for _ in range(N+1) ]
# adjS = [ [] for _ in range(N+1) ]
#
# M = int(input())
# for _ in range(M):
#     S, E, C = map(int,input().split())
#     adjS[S].append(E)
#     adjC[S][E] = C
#
# startt, endd = map(int,input().split())
#
# # answers = []
# minimum = 100000 * M
# def dijkstra(start,end,value):
#     # Q = [start]
#     global minimum
#
#     elem = start
#     if elem == end:
#         # answers.append(value)
#         if value < minimum:
#             minimum = value
#         return
#
#     if value >= minimum:
#         return
#
#     target = []
#     for n in adjS[elem]:
#         target.append(n)
#     for t in target:
#         value += adjC[elem][t]
#         dijkstra(t,end,value)
#         value -= adjC[elem][t]
#
# dijkstra(startt,endd,0)
#
# print(minimum)

import heapq  # 우선순위 큐 구현을 위함
import sys
input = sys.stdin.readline

# 입력
N = int(input())  # node 개수
M = int(input())  # edge 개수
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # 도착지, 가중치
start, end = map(int, input().split())  # 출발지 목적지

# 다익스트라 최적경로 탐색
def dijkstra(graph, start):
    distances = [int(1e9)] * (N+1)  # 처음 초기값은 무한대
    distances[start] = 0  # 시작 노드까지의 거리는 0
    queue = []
    heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작

    while queue:  # queue에 남아있는 노드가 없을 때까지 탐색
        dist, node = heapq.heappop(queue)  # 탐색할 노드, 거리

        # 기존 최단거리보다 멀다면 무시
        if distances[node] < dist:
            continue

        # 노드와 연결된 인접노드 탐색
        for next_node, next_dist in graph[node]:
            distance = dist + next_dist  # 인접노드까지의 거리
            if distance < distances[next_node]:  # 기존 거리 보다 짧으면 갱신
                distances[next_node] = distance
                heapq.heappush(queue, [distance, next_node])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    return distances

dist_start = dijkstra(graph, start)
print(dist_start[end])

'''
5 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3 
3 4 2
3 5 1
4 5 5
'''
'''
V = int(input()) # 0 ~ V번 정점
E = int(input()) # E 간선 수
INF = 100000*E # 임의의 큰 값
adjM = [[INF] * (V+1) for _ in range(V+1)]
for i in range(V+1):
    adjM[i][i] = 0 # 자기 자신으로 가는 비용
for _ in range(E):
    u, v, w = map(int,input().split()) # u -> v, w 가중치
    adjM[u][v] = w
s,e = map(int,input().split())
D = [0] * (V+1)

def dijkstra(s,V): # s : 출발, V : 마지막 정점 번호
    U = [0] * (V+1) # U 최소비용이 결정된 정점 집합
    U[s] = 1 # U = {s}
    for i in range(V+1): # s에서 정점 i로 가는 비용
        D[i] = adjM[s][i]

    # while U != V: 남은 정점의 비용 결정
    N = V + 1 # N개의 정점
    for _ in range(N-1): # N-1개 정점의 비용 결정
        # D[w]가 최소인 w 결정
        minV = INF
        w = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]: # 남은 정점 i 중, 최소
                w = i
                minV = D[i]
        U[w] = 1 # 최소인 w는 최소비용 D[w] 확정
        # w에 인접인 정점에 대해 기존비용 vs w를 거쳐가는 비용 비교
        for v in range(V+1):
            if 0 < adjM[w][v] < INF: # w에 인접인 v의 조건
                D[v] = min(D[v], D[w] + adjM[w][v])

dijkstra(s,e)
print(D[e])
'''

