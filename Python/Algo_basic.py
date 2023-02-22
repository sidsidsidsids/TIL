'''
5
55 7 78 12 42
for i : N-1 -> 1 # 각 구간의 끝
    for j : 0 -> i-1 # 비교할 왼쪽 원소
        if arr[j] > arr[j+1]
            arr[j] <-> arr[j+1]  # 큰 원소

# N = int(input())
# arr = list(map(int, input().split()))
# for i in range(N-1,0,-1): # 각 구간의 끝
#     for j in range(i): # 비교할 왼쪽 원소
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j] # 큰 원소 오른쪽으로
#
# print(*arr)

'''
#리스트를 받아 최댓값을 출력하는 케이스 여러 개
'''
T=int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV = arr[0]
    for i in range(1, N):
        if maxV < arr[i]:
            maxV = arr[i]
    print(f'#{tc} {maxV}')
'''
'''
def Counting_Sort(A,B,k):
    C = [0] * (k+1)
    for i in range(0, len(A)):
        C[A[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i-1]
    for i in range (len(B)-1, -1, -1) :
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    print(B)

Counting_Sort([0,4,1,3,1,2,4,1],[0]*(5),4)
'''
'''
a = ['a','b','c','\0']
def strlen(a):
    i = 0
    while a[i] != '\0':
        i += 1
    return i 

print(strlen(a))
'''
'''
# 고지식한 패턴찾기
p = 'ab' # 찾을 패턴
t = 'aaabaaaabaab' # 전체 문장
M = len(p)
N = len(t)
def bf(p,t):
    i = 0
    j = 0 # 텍스트 비교위치들
    while i < N and j < M: # 비교할 문장이 남아있고 패턴을 찾기 전이면
        if t[i] != p[j]: # 서로 다른 글자를 만나면
            i -= j # 비교를 시작한 위치로
            j = -1 # 패턴의 시작 전으로
        i += 1
        j += 1
    if j == M : # 패턴을 찾은 경우
        return i - M
    else:
        return -1
    
print(bf(p,t))
'''
'''
# KMP Algorithm
# T : Target / P : Pattern

# lps longest prefix suffix
def pre_process(p):
    lps = [0] * len(p)

    # lps를 만들기 위한 패턴 인덱스
    j = 0

    # 처음부터 끝까지 순회
    for i in range(1, len(p)):
        # 패턴 발견 해당 인덱스에 있는 char 가 똑같다면
        if p[i] == p[j]:
            lps[i] = j + 1
            j += 1
            
        # 다르다면, j 인덱스를 초기화 => pattern의 가장 처음부터 다시 인식하도록
        else:
            j = 0
            if p[i] == p[j]:
                lps[i] = j + 1
                j += 1

    return lps

p = 'abcdabcef'

rlt = pre_process(p)

print(rlt)
'''
'''
# 스택
stack = [0] * 3
top = -1

top += 1 # push(10)
stack[top] = 10

top += 1 # push(20)
stack[top] = 20

top += 1 # push(30)
stack[top] = 30
if top > -1:
    top -= 1
    print(stack[top+1])
if top > -1:
    top -= 1
    print(stack[top+1])
if top > -1:
    top -= 1
    print(stack[top+1])
'''
'''
# bracket
test_case = int(input())
for tc in range(test_case):
    gwalho = input()

    stack = [0] * len(gwalho)
    top = -1
    s_result = 0

    for i in gwalho:
        if top == size:
            print('overflow')
'''
'''
def func2():
    print('함수 2 시작')
    print('함수 2 종료')

def func1():
    print('함수 1 시작')
    func2()
    print('함수 1 종료')

print('main 시작')
func1()
print('main 끝')
'''
'''
# i가 k가 될 때까지
def f(i, k):
    if i == k:
        print(B)
        return
    else:
        B[i] = A[i]
        f(i+1, k)
A = [10, 23, 30]
B = [0] * 3
f(0, 3)
'''
'''
#입력값 V, E / arr
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
'''
# 재귀 DFS
V, E = map(int, input().split())
arr = list(map(int, input().split()))

adjM = [[0] * (V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]

visited = [0] * (V+1)

for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adjM[v1][v2] = 1
    adjM[v2][v1] = 1 # v1과 v2는 인접해있다
    
    adjL[v1].append(v2)
    adjL[v2].append(v1)

def dfs(v):
    visited[v] = 1
    print(v, end=" ")
    # 현재 v는 시작정점, 인접한 정점 중 방문을 안한 곳
    for w in range(1, V+1):
        if adjM[v][w] == 1 and visited[w] == 0:
            dfs(w)



def dfs(v):
    stack = [v]
    # stack.append(v)
    while len(stack): # 스택이 빌 때까지 반복
        v = stack.pop()
        # v가 아직 방문하지 않았다면
        visited[v] = 1
        print(v, end=" ")
        for w in range(1, V+1):
            if adjM[v][w] == 1 and visited[w] == 0:
                stack.append(w)


dfs(1)
'''
'''
# 백트래킹을 통한 순열 구하기
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        for i in range(1, k+1):
            print(a[i], end=" ")
        print()

    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

def construct_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1,k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates

NMAX = 11
MAXCANDIDATES = 10
a = [0] * NMAX
backtrack(a, 0, 3)
'''

'''
# 조합 구하기
def f(i, k):
    if i == k:
        #print(bit)
        for j in range(k):
            if bit[j]:
                print(A[j], end = ' ')
        print(bit)
    else:
        bit[i] = 1
        f(i+1, k)
        bit[i] = 0
        f(i+1, k)
A = [1,2,3,5,9]
N = len(A)
bit = [0]*N
f(0, N)
'''
'''
# 조합 구하기 응용 부분집합의 합 구하기
def f(i, k, key):
    if i == k:
        s = 0
        for j in range(k):
            if bit[j]:
                s += A[j]
        if s == key:
            for j in range(k):
                if bit[j]:
                    print(A[j], end=' ')
            print(bit)
    else:
        bit[i] = 1
        f(i+1, k, key)
        bit[i] = 0
        f(i+1, k, key)
A = [r for r in range(1,11)]
N = len(A)
key = 10
bit = [0]*N
f(0, N, key)
'''
'''
# 합이 key인 부분집합의 수 구하기

N = 10 #len(A)
A = [r for r in range(1,N+1)]
key = 10
cnt = 0; fcnt=0
bit = [0]*N

def f(i, k, s, t): # i:원소, k:집합의 크기, s:부분집합의 합(=i-1까지 고려된), t:목표(찾고자하는값)
    global cnt
    global fcnt # 함수 호출 횟수 세는 변수 선언
    fcnt += 1
    # 백트레킹
    if s > t: # 고려한 원소의 합이 찾는 합보다 큰 경우
        return
    elif s == t: # 남은 원소를 고려할 필요가 없는 경우
        cnt += 1
        return
    # 탐색
    elif i == k: # 모든 원소 고려
        return
    else:
        bit[i] = 1
        f(i+1, k, s+A[i], t) # A[i] 포함
        bit[i] = 0
        f(i+1, k, s, t) # A[i] 미포함

f(0,N,0,key)
print(cnt, fcnt)
'''
'''
def f(i, k):
    if i == k:
        print(p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            # p[i] 결정, p[i]와 관련된 작업 가능
            f(i+1, k)
            p[i], p[j] = p[j], p[i]


p = [1,2,3]
f(0,3)
'''
'''
infix = '(7-2)*5+4+7*(4/2-2)'
stack = []
result = ''

# 변환할 식을 순회
for token in infix:
    # 토큰이 피연산자인 경우
    if token.isdecimal():
        result += token
        print(f'token : {token}, stack : {stack}, result : {result}')

    # 토큰이 연산자인 경우
    else:
        # 스택이 비어있는 경우, 스택에 push
        if not stack: # if len(stack) == 0
            stack.append(token)
            print(f'token : {token}, stack : {stack}, result : {result}')

        else:
            # (는 incoming 우선순위가 가장 높음
            if token == '(':
                stack.append(token)
                print(f'token : {token}, stack : {stack}, result : {result}')
            # )는 (가 나올때까지 스택에서 pop, result에 append
            elif token == ')':
                while stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
                print(f'token : {token}, stack : {stack}, result : {result}')

            # incoming 우선순위가 2인 경우
            elif token == '*' or token == '/':
                # 스택의 top 토큰이 우선순위가 낮을 때까지 스택에서 pop, result append
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    result += stack.pop()
                stack.append(token)
                print(f'token : {token}, stack : {stack}, result : {result}')

            # incoming 우선순위가 1인 경우
            elif token == '+' or token == '-':
                # 스택의 top 토큰이 우선순위가 낮을 때까지 스택에서 pop, result append
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(token)
                print(f'token : {token}, stack : {stack}, result : {result}')

while stack:
    result += stack.pop()
    print(f'stack : {stack}, result : {result}')

print(f'result : {result}')

# 피연산자
    # 스택에 push
# 연산자 (*, / 연산 순서 주의
    # 스택에 담겨있는 2개의 토큰을 pop 후 연산 후 스택에 push
'''

'''
def enqueue(data):
    global rear
    rear += 1
    queue[rear] = data

def dequeue():
    global front
    front += 1
    return queue[front]

queue = [0]*3
front = -1
rear = -1

rear += 1 #enqueue(1)
queue[rear] = 1
enqueue(2)
enqueue(3)

print(dequeue())
print(dequeue())
if front != rear:
    print(dequeue())
if front != rear:
    print(dequeue())
print(queue)
'''
'''
# 혼자 해본거
def BFS(G, v, n): # G : 그래프, v : 시작점, n : 정점의 갯수
    visited = [0] * (n+1)
    queue = []
    queue.append(v)
    visited[v] = 1

    while queue:
        t = queue.pop(0)
        if t == 0:
            continue
        print(t, end=' ')
        for i in G[t] :
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[n] + 1

V = 7; E = 8
arr = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
arrM = [ [0] * (V+1) for _ in range(V+1) ]

for i in range(E):
    v1, v2 = arr[2*i], arr[2*i + 1]
    arrM[v1][v2] = v2
    # arrM[v2][v1] = v1

#print(arrM)

BFS(arrM, 1, V)
'''
'''
def bfs(v, N):
    visited = [0] * (N+1) # visited 생성
    q = [v] # queue 생성 및 시작점 enQueue
    visited[v] = 1 # 시작점 enQueue 표시

    while q: # 큐가 비어질 때 까지
        t = q.pop(0) # deQueue
        print(t, end = ' ') # t 출력(t에서 처리할 일)
        for v in adjL[t]: # t에 인접하고 방문한 적 없는 w
            if visited[v] == 0:
                q.append(v) # v enQueue
                visited[v] = visited[t] + 1 # enQueue 표시(with distance)
    print()
    print(visited) # distance

V = 7; E = 8
arr = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[2*i], arr[2*i + 1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)
print(adjL)

bfs(1, V) # 시작정점 1, 마지막 정점 V


# # 예제 : 미로의 거리
# def bfs(i, j, N):
#     visited = [ [0] * N for _ in range(N) ]
#     q = [i, j] # q = [[i, j]]
#     visited[i][j] = 1
'''

#self
def tree_VLR(s):
    print(s, end=' ')
    visited[s] = 1

    for v in arrL[s]:
        if visited[v] == 0:
            tree_VLR(v)

def tree_LVR(s):
    visited[s] = 1
    for v in arrL[s]:
        if not arrL[s]:
            print(s)
        elif visited[v] == 0:
            tree_VLR(v)

    print(s, end=' ')


V = int(input())
arr = list(map(int,input().split()))
E = V - 1

arrL = [ [] for _ in range(V+1) ]
for i in range(E):
    v1, v2 = arr[2*i], arr[2*i + 1]
    arrL[v1].append(v2)
visited = [0] * (V+1)

tree_VLR(1)
#tree_LVR(1)

