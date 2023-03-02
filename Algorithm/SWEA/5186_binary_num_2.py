test_case = int(input())
for tc in range(1, test_case+1):
    n = input()
    n = float(n)
    s = -1
    ans = []
    while s > -13 and n != 0:
        if n - 2**s >= 0:
            n = n - 2**s
            ans.append(1)
        else:
            ans.append(0)
        s -= 1

    if n != 0:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc}', end= ' ')
        for n in ans:
            print(n,end='')
        print()