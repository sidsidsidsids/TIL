'''
A에서 N개 만큼 원소를 뽑아서 합이 K를 찍을 수 있는 경우
조합을 어떻게 뽑을 것인지
'''
# 조합을 뽑기 위해 재귀를 이용한 함수를 정의하는 방법
# 왼쪽부터 하나하나 뽑는 방법
def cases(array, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(array)):
        element = array[i]
        for rest in cases(array[i + 1:], n-1):
            result.append([element] + rest)
    return result

test_case = int(input())
test_cnt = 1
A_list = [x for x in range(1,6)]

for _ in range(test_case):
    A, K = map(int, input().split())
    answer = 0
    possible_A = cases(A_list, A)
    for case in possible_A:
        if sum(case) == K:
            answer += 1
    print(f'#{test_cnt} {answer}')
    test_cnt += 1

# from itertools import combinations
#
# test_case = int(input())
# test_cnt = 1
#
# for _ in range(test_case):
#     A, K = map(int, input().split())
#     A_list = [x for x in range(1,13)]
#     combi = list(combinations(A_list,A))
#     answer = 0
#     for case in combi:
#         if sum(case) == K:
#             answer += 1
#
#     print(f'#{test_cnt} {answer}')
#     test_cnt += 1