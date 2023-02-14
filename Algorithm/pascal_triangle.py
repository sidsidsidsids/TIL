'''
1:      1
2:      1 1
3(4):   1 2 1
4(8):   1 3 3 1
5(16):  1 4 6 4 1
6(32):  1 5 10 10 5 1
7(64):  1 6 15 20 15 6 1
8(128): 1 7 21 35 35 21 7 1
9 256
10 512
'''

def pascal(n):
    if n == 1:
        return [1]
    f = [0] * n
    if n >= 2:
        f[0] = [1]
        f[1] = [1,1]
        for i in range(2, n):
            f[i] = [1]
            for j in range(len(f[i-1])-1):
                f[i].append(f[i-1][j]+f[i-1][j+1])
            f[i].append(1)
    return f

test_case = int(input())
for tc in range(test_case):
    num = int(input())
    answer = pascal(num)
    print(f'#{tc+1}')
    for i in range(len(answer)):
        if len(answer) == 1:
            print(1)
        else:
            print(*answer[i])
