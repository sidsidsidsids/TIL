import sys
sys.stdin = open("scanner.txt", "r")

def sixteen_to_two(n):
    n = int(n,16)
    if n == 1:
        c = '0001'
        return c
    elif n == 2:
        c = '0010'
        return c
    elif n == 3:
        c = '0011'
        return c
    elif n == 4:
        c = '0100'
        return c
    elif n == 5:
        c = '0101'
        return c
    elif n == 6:
        c = '0110'
        return c
    elif n == 7:
        c = '0111'
        return c
    elif n == 8:
        c = '1000'
        return c
    elif n == 9:
        c = '1001'
        return c
    elif n == 10: # A
        c = '1010'
        return c
    elif n == 11: # B
        c = '1011'
        return c
    elif n == 12: # C
        c = '1100'
        return c
    elif n == 13: # D
        c = '1101'
        return c
    elif n == 14: # E
        c = '1110'
        return c
    elif n == 15: # F
        c = '1111'
        return c
    else:
        return '0'

test_case = int(input())
for tc in range(1,test_case+1):
    N, M = map(int,input().split())
    password = [ list(input()) for _ in range(N) ]

    pw_idx = []
    for i in range(N):
        if password[i].count('0') != M:
            pw_idx.append(i)

    ans = 0
    pw_list = []

    for i in pw_idx:
        checker = ''
        for j in range(M):
            password[i][j] = sixteen_to_two(password[i][j])
            checker += password[i][j]

        checker = checker[::-1]
        num_list = []

        n = 0
        s = 0
        while n < len(checker) - 7:
            if checker[n] == '1':
                if checker[n + 1] == '0' and checker[n + 2] == '1' and checker[n + 3] == '1' and \
                        checker[n + 4] == '0' and checker[n + 5] == '0' and checker[n + 6] == '0':
                    num_list.append(0)
                    n += 7
                elif checker[n + 1] == '0' and checker[n + 2] == '0' and checker[n + 3] == '1' and \
                        checker[n + 4] == '1' and checker[n + 5] == '0' and checker[n + 6] == '0':
                    num_list.append(1)
                    n += 7
                elif checker[n + 1] == '1' and checker[n + 2] == '0' and checker[n + 3] == '0' and \
                        checker[n + 4] == '1' and checker[n + 5] == '0' and checker[n + 6] == '0':
                    num_list.append(2)
                    n += 7
                elif checker[n + 1] == '0' and checker[n + 2] == '1' and checker[n + 3] == '1' and \
                        checker[n + 4] == '1' and checker[n + 5] == '1' and checker[n + 6] == '0':
                    num_list.append(3)
                    n += 7
                elif checker[n + 1] == '1' and checker[n + 2] == '0' and checker[n + 3] == '0' and \
                        checker[n + 4] == '0' and checker[n + 5] == '1' and checker[n + 6] == '0':
                    num_list.append(4)
                    n += 7
                elif checker[n + 1] == '0' and checker[n + 2] == '0' and checker[n + 3] == '0' and \
                        checker[n + 4] == '1' and checker[n + 5] == '1' and checker[n + 6] == '0':
                    num_list.append(5)
                    n += 7
                elif checker[n + 1] == '1' and checker[n + 2] == '1' and checker[n + 3] == '1' and \
                        checker[n + 4] == '0' and checker[n + 5] == '1' and checker[n + 6] == '0':
                    num_list.append(6)
                    n += 7
                elif checker[n + 1] == '1' and checker[n + 2] == '0' and checker[n + 3] == '1' and \
                        checker[n + 4] == '1' and checker[n + 5] == '1' and checker[n + 6] == '0':
                    num_list.append(7)
                    n += 7
                elif checker[n + 1] == '1' and checker[n + 2] == '1' and checker[n + 3] == '0' and \
                        checker[n + 4] == '1' and checker[n + 5] == '1' and checker[n + 6] == '0':
                    num_list.append(8)
                    n += 7
                elif checker[n + 1] == '1' and checker[n + 2] == '0' and checker[n + 3] == '1' and \
                        checker[n + 4] == '0' and checker[n + 5] == '0' and checker[n + 6] == '0':
                    num_list.append(9)
                    n += 7
                else:
                    checker = checker[0::2]
                    n = 0
                    s += 1
                    if s == 2:
                        # print('error')
                        # s=0
                        break

                if len(num_list) == 8:
                    pw = ''
                    pw_sum = 0
                    if ((sum(num_list[1::2]) * 3) + sum(num_list[0::2])) % 10 == 0:
                        for num in num_list[::-1]:
                            pw_sum += num
                            pw += str(num)
                        if pw not in pw_list:
                            pw_list.append(pw)
                            ans += pw_sum
                        else:
                            pass
                    num_list = []
            else:
                n += 1

    print(f'#{tc} {ans}', N)