def cases(array, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(array)):
        element = array[i]
        for rest in cases(array[i+1:], n-1):
            result.append([element] + rest)
    return result

tall = []
for _ in range(9):
    tall.append(int(input()))

seven_list = cases(tall, 7)
for lists in seven_list:
    if sum(lists) == 100:
        lists = sorted(lists)
        for num in lists:
            print(num)
        break

# 합이 key인 부분집합의 수 구하기

# A = [0] * 9
# for i in range(9):
#     A[i] = int(input())
# key = 100
# bit = [0]*9
# answer = []

# def f(i, k, s, t): # i:원소, k:집합의 크기, s:부분집합의 합(=i-1까지 고려된), t:목표(찾고자하는값)
#     # 백트레킹
#     if s > t: # 고려한 원소의 합이 찾는 합보다 큰 경우
#         return
#     elif s == t: # 남은 원소를 고려할 필요가 없는 경우
#         if bit.count(1) == 7:
#             for j in range(k):
#                 if bit[j]:
#                     answer.append(A[j])
#             return
#         else:
#             return
#     # 탐색
#     elif i == k: # 모든 원소 고려
#         return
#     else:
#         bit[i] = 1
#         f(i+1, k, s+A[i], t) # A[i] 포함
#         bit[i] = 0
#         f(i+1, k, s, t) # A[i] 미포함

# f(0,9,0,key)
# answer.sort()
# for i in range(7):
#     print(answer[i])