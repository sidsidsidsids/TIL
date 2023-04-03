N = int(input())
adjC = [ [0] * (N+1) for _ in range(N+1) ]
adjS = [ [] for _ in range(N+1) ]

M = int(input())
for _ in range(M):
    S, E, C = map(int,input().split())
    adjS[S].append(E)
    adjC[S][E] = C

startt, endd = map(int,input().split())

answers = []
def dijkstra(start,end,value):
    Q = [start]

    elem = Q.pop(0)
    if elem == end:
        answers.append(value)
    target = []
    for n in adjS[elem]:
        target.append(n)
    for t in target:
        value += adjC[elem][t]
        dijkstra(t,end,value)
        value -= adjC[elem][t]

dijkstra(startt,endd,0)

print(min(answers))



