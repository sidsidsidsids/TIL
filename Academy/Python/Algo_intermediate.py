
'''
#순열

def perm(i, k): # i : 값을 결정할 자리, k : 결정할 개수
    if i == k:
        print(*p)
    else:
        for j in range(i,k): # 자신부터 오른쪽 원소들과 교환
            p[i], p[j] = p[j], p[i]
            perm(i+1,k)
            p[i], p[j] = p[j], p[i]

p = [1,2,3]
perm(0,3)

def perm(i,k):
    if i == k:
        print(*p)
    else:
        for j in range(k): # 사용하지 않은 숫자를
            if used[j] == 0: # used에서 순서대로 검색
                p[i] = A[j]
                used[j] = 1 # j번 자리 숫자 사용으로 표시
                perm(i+1, k)
                used[j] = 0 # j번 자리 숫자를 다른 자리에서 쓸 수 있게

A = [1,4,5]
p = [0]*3
used =[0]*3
perm(0,3)
'''

'''
# 부분집합

arr = [3,6,7,1,5,4]
n = len(arr)

for i in range(0,(1<<n)): # range(0,64) n=6이므로 1<<n = 2^6, 000000~111111의 경우 모두 확인
    for j in range(0,n): # 각 인덱스마다 해당 원소가 부분집합에 들어갈지 말지
        if i & (1<<j): # & : And 연산, 비트가 0이면 0, 1이면 != 0
            print('%d'%arr[j], end=' ')
    print()

def f(i,k): #bit[i]를 결정하는 함수
    if i==k:
        print(*bit)
    else:
        bit[i] = 0
        f(i+1, k)
        bit[i] = 1
        f(i+1, k)

A = [7, 2, 5, 4, 6]
N = len(A)
bit = [0] * N
f(0, N)
'''
'''
조합
N = 10
cnt=0
for i in range(N-(3-1)):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            print(i, j, k)
            cnt+=1
print(cnt)

n = 5
r = 3
comb = [0] * 3
A = [i for i in range(n)]

def nCr(n, r, s): # n개에서 r개를 고르는 조합, s는 시작할 인덱스
    if r == 0:
        print(*reversed(comb))
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            print(comb, end=' ')
            nCr(n, r-1, i+1)

nCr(n, r, 0)

n, r = input().split()
n = int(n)
r = int(r)

comb = [0] * r
A = [i+1 for i in range(n)]

def nCr(n, r, s):
    if r == 0:
        print(*reversed(comb))
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)

nCr(n, r, 0)
'''
'''
# 병합 정렬 (하다말음)
def merge(left, right):
    pass

def msort(s, e):
    if s == e:
        return
    # else: if에 return 있으니까 생략
    m = (s+e) // 2
    msort(s, m)
    msort(m+1, e)
    # merge()
    k = 0
    l, r = s, m+1 # 왼쪽과 오른쪽에서 가장 작은 숫자의 위치
    while l <= m or r <= e:
        if l <= m and r <= e:
            if arr[l] <= arr[r]:
                tmp[k] = arr[l]
                l += 1
            else:
                tmp[k] = arr[r]
                r += 1
            k += 1
        elif l <= m:
            while l <= m:
                tmp[k] = arr[l]
                l += 1
                k += 1
        elif r <= e:
            while r <= e:
                tmp[k] = arr[r]
                r += 1
                k += 1
    i = 0
    while i < k:
        arr[s + i] = tmp[i]
        i += 1



    return merge(left, right)



T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0]*N

    msort(0,N-1)
    print(arr)
'''
'''
# 퀵 정렬
def hoare(A, l, r):
    pivot = A[l] # 피봇을 맨 왼쪽 원소로
    i = l        # 피봇보다 큰 값을 찾아 오른쪽으로 이동
    j = r        # 피봇보다 작은 값을 찾아 왼쪽으로 이동

    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:# 교차하지 않은 경우
            A[i], A[j] = A[j], A[i]
    A[j], A[l] = A[l], A[j]

    return j


def qsort(A, l, r):
    if l < r:
        s = hoare(A, l, r)
        qsort(A, l, s-1)
        qsort(A, s+1, r)

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    qsort(arr,0,n-1)
    print(*arr)
'''
'''
# subset에서 key값 찾기 (부분집합)
def f(i,k,s,key, rs): # 시작 idx, 끝 idx, 현재 sum, 목표값, 오른쪽 나머지들의 sum
    global cnt
    global c
    c += 1
    if s == key:
        cnt += 1
        return
    elif i == k or s > key or s+rs < key:
        return
    else:
        bit[i] = 0
        f(i+1, k, s, key, rs - A[i])
        bit[i] = 1
        f(i+1, k, s+A[i], key, rs - A[i])

A = [i for i in range(1,11)]
N = 10
key = 42
cnt = 0
c = 0
bit = [0] * N
f(0, N, 0, key, sum(A))
print(cnt, c)
'''
#'''
# MST (최소 비용 신장 트리)
# kruskal (간선을 하나씩 선택해서 MST를 찾는 알고리즘)

def find_set(x): # x가 속한 집합의 대표 집합
    while x != rep[x]: # x == rep[x]가 될 때까지
        print(x,' become ', rep[x])
        x = rep[x]
    return x

def union(x,y): # y의 대표원소가 x의 대표원소를 가리키도록 함
    rep[find_set(y)] = find_set(x)
    print(rep)

rep = [i for i in range(6)]

'''

6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51

'''
V,E = map(int,input().split())

# makeset()
rep = [i for i in range(V+1)]
graph = []
for _ in range(E):
    v1, v2, w = map(int,input().split())
    graph.append([v1,v2,w])

# (1) 가중치 기준 오름차순 정렬
graph.sort(key = lambda X:X[2])

# (2) N개의 정점(V+1), N-1개의 간선 선택
N = V + 1
s = 0 # MST에 포함된 간선의 가중치 합
cnt = 0
MST = []
for u, v, w in graph: # 가중치가 작은 것부터(가중치로 정렬했으니까)
    if find_set(u) != find_set(v): # 사이클이 생기지 않으면
        cnt += 1
        s += w # 가중치 합
        MST.append([u,v,w])
        union(u, v)
        if cnt == N - 1: # MST 구성 완료
            break
print(s)
print(MST)
#'''
'''
# dijkstra (시작 정점에서 거리가 최소인 정점을 선택해 나가는 방법

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

'''
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

INF = 1000 # 임의의 큰 값
V, E = map(int,input().split()) # 0 ~ V번 정점, E 간선 수
adjM = [[INF] * (V+1) for _ in range(V+1)]
for i in range(V+1):
    adjM[i][i] = 0 # 자기 자신으로 가는 비용
for _ in range(E):
    u, v, w = map(int,input().split()) # u -> v, w 가중치
    adjM[u][v] = w

D = [0] * (V+1)

dijkstra(0,V)
print(D)
'''