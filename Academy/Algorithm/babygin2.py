t = int(input())
for test_case in range(1,t+1):
    '''
    babyjin = str(input())
    cnt = [0] * 10
    for n in babyjin:
        cnt[int(n)] += 1

    triplet = 0
    run = 0

    for i in range(10):
        if cnt[i] >= 3:
            if cnt[i] == 6:
                triplet += 2
                cnt[i] = 0
            else:
                triplet += 1
                cnt[i] -= 3

    for i in range(8):
        if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:
            if cnt[i] == 2 and cnt[i+1] == 2 and cnt[i+2] == 2:
                run += 2
                cnt[i] = 0; cnt[i+1] = 0; cnt[i+2] = 0
            else:
                run += 1
                cnt[i] -= 1
                cnt[i + 1] -= 1
                cnt[i + 2] -= 1

    if triplet+run == 2:
        print(True)
    else:
        print(False)
    '''
    babyjin = input()
    babyjin_list = [0]*6
    for i in range(6):
        babyjin_list[i] = int(babyjin[i])
    p = [0]*6
    used = [0]*6
    ans = False

    def perm(i, k):
        global ans
        if i == k:
            if (p[0] + 2 == p[1] + 1 and p[1] + 1 == p[2]) or (p[0] == p[1] and p[1] == p[2]):
                if (p[3] + 2 == p[4] + 1 and p[4] + 1 == p[5]) or (p[3] == p[4] and p[4] == p[5]):
                    ans = True
        else:
            for j in range(k):  # 사용하지 않은 숫자를
                if used[j] == 0:  # used에서 순서대로 검색
                    p[i] = babyjin_list[j]
                    used[j] = 1  # j번 자리 숫자 사용으로 표시
                    perm(i + 1, k)
                    used[j] = 0  # j번 자리 숫자를 다른 자리에서 쓸 수 있게

    perm(0,6)
    print(ans)