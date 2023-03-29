
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
