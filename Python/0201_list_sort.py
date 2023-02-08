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