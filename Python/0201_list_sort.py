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