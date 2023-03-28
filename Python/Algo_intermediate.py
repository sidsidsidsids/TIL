
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
#'''
# 조합
# N = 10
# cnt=0
# for i in range(N-(3-1)):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             print(i, j, k)
#             cnt+=1
# print(cnt)

# n = 5
# r = 3
# comb = [0] * 3
# A = [i for i in range(n)]

# def nCr(n, r, s): # n개에서 r개를 고르는 조합, s는 시작할 인덱스
#     if r == 0:
#         print(*reversed(comb))
#     else:
#         for i in range(s, n-r+1):
#             comb[r-1] = A[i]
#             print(comb, end=' ')
#             nCr(n, r-1, i+1)

# nCr(n, r, 0)
#'''
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