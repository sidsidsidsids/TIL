test_case = int(input())
for tc in range(1,test_case+1):
    N, M = map(int,input().split())
    password = [ list(map(int,input())) for _ in range(N) ]

    for i in range(N):
        if 1 in password[i]:
            target = i
            break

    checker = password[target][::-1]

    num_list = []
    n = 0

    while len(num_list) < 8:
        if checker[n] == 1:
            if checker[n+1] == 0 and checker[n+2] == 1 and checker[n+3] == 1 and\
                checker[n+4] == 0 and checker[n+5] == 0 and checker[n+6] == 0:
                num_list.append(0)
                n += 7
            elif checker[n+1] == 0 and checker[n+2] == 0 and checker[n+3] == 1 and\
                checker[n+4] == 1 and checker[n+5] == 0 and checker[n+6] == 0:
                num_list.append(1)
                n += 7
            elif checker[n+1] == 1 and checker[n+2] == 0 and checker[n+3] == 0 and\
                checker[n+4] == 1 and checker[n+5] == 0 and checker[n+6] == 0:
                num_list.append(2)
                n += 7
            elif checker[n+1] == 0 and checker[n+2] == 1 and checker[n+3] == 1 and\
                checker[n+4] == 1 and checker[n+5] == 1 and checker[n+6] == 0:
                num_list.append(3)
                n += 7
            elif checker[n+1] == 1 and checker[n+2] == 0 and checker[n+3] == 0 and\
                checker[n+4] == 0 and checker[n+5] == 1 and checker[n+6] == 0:
                num_list.append(4)
                n += 7
            elif checker[n+1] == 0 and checker[n+2] == 0 and checker[n+3] == 0 and\
                checker[n+4] == 1 and checker[n+5] == 1 and checker[n+6] == 0:
                num_list.append(5)
                n += 7
            elif checker[n+1] == 1 and checker[n+2] == 1 and checker[n+3] == 1 and\
                checker[n+4] == 0 and checker[n+5] == 1 and checker[n+6] == 0:
                num_list.append(6)
                n += 7
            elif checker[n+1] == 1 and checker[n+2] == 0 and checker[n+3] == 1 and\
                checker[n+4] == 1 and checker[n+5] == 1 and checker[n+6] == 0:
                num_list.append(7)
                n += 7
            elif checker[n+1] == 1 and checker[n+2] == 1 and checker[n+3] == 0 and\
                checker[n+4] == 1 and checker[n+5] == 1 and checker[n+6] == 0:
                num_list.append(8)
                n += 7
            elif checker[n+1] == 1 and checker[n+2] == 0 and checker[n+3] == 1 and\
                checker[n+4] == 0 and checker[n+5] == 0 and checker[n+6] == 0:
                num_list.append(9)
                n += 7
        else:
            n += 1

    pw = num_list[::-1]

    if (sum(pw[0::2])*3 + sum(pw[1::2])) % 10 == 0:
        print(f'#{tc} {sum(pw)}')
    else:
        print(f'#{tc} 0')

