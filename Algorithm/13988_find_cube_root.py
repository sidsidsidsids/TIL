test_case = int(input())
for tc in range(1, test_case+1):
    n = int(input())
    if round(n**(1/3),0) == n**(1/3):
        print(round(n**(1/3),1))
        print(n**(1/3))
        n = int(n**(1/3))
    else:
        print(round(n ** (1 / 3), 0))
        print(n ** (1 / 3))
        n = -1
    print(f'#{tc} {n}')
