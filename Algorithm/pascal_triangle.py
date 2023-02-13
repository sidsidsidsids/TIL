'''
1:              1
2:             1 1
3(4):         1 2 1
4(8):        1 3 3 1
5(16):      1 4 6 4 1
6(32):    1 5 10 10 5 1
7(64):   1 6 15 20 15 6 1
8(128): 1 7 21 35 35 21 7 1
9 256
10 512
'''

def pascal(n):
    if n <= 2:
        return [1] * n


test_case = int(input())
for tc in range(test_case):
    N = int(input())
    triangle = [[1],[1,1]]
    if N == 1:
        print(*triangle[0])
    elif N == 2:
        print(*triangle[0])
        print(*triangle[1])

    for i in range(N):
        new_row = [1]
        new_row[i]
