t = int(input())
for tc in range(1,1+t):
    N = int(input())
    S = [ [] for _ in range(N) ]
    for i in range(N):
        S[i] = list(map(int,input().split()))

    foods = [i for i in range(N)]
    half = N // 2
    ables = []
    def divide_foods(n, first, second):
        if len(first) > half or len(second) > half:
            return
        if n == N:
            if len(first) == half and len(second) == half:
                ables.append([first, second])
            return

        divide_foods(n + 1, first + [foods[n]], second)
        divide_foods(n + 1, first, second + [foods[n]])


    divide_foods(0, [], [])

    # bit = [0] * N
    # half = N//2
    # foods = [ i for i in range(N) ]
    # ables = []
    # comb = []
    #
    # def cases(n,k,bit):
    #     if n > half and sum(bit) < half-n:
    #         return
    #     if sum(bit) == half:
    #         tmp = [0] * half
    #         tmp2 = [0] * half
    #         tmp_idx = 0; tmp2_idx = 0
    #         for j in range(N):
    #             if bit[j]:
    #                 tmp[tmp_idx] = foods[j]
    #                 tmp_idx += 1
    #             else:
    #                 tmp2[tmp2_idx] = foods[j]
    #                 tmp2_idx += 1
    #         if tmp in comb or tmp2 in comb:
    #             return
    #         else:
    #             comb.append(tmp)
    #             comb.append(tmp2)
    #             ables.append([tmp,tmp2])
    #             return
    #
    #     for i in range(n,N):
    #         bit[i] = 1
    #         cases(n+1,k,bit)
    #         bit[i] = 0
    #         cases(n+1,k,bit)
    #
    # cases(0,N,bit)

    minval = 20000 * half

    for able in ables:
        A = 0; B = 0
        for a in able[0]:
            for aa in able[0]:
                if a != aa:
                    A += S[a][aa]
        for b in able[1]:
            for bb in able[1]:
                if b != bb:
                    B += S[b][bb]
        value = abs(A-B)
        if minval > value:
            minval = value

    print(f'#{tc} {minval}')


