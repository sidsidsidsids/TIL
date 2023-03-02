def tree_LVR(s):
    if s:
        tree_LVR(c1[s])
        global cnt
        dictionary[cnt] = s
        cnt += 1
        tree_LVR(c2[s])

test_case = int(input())

for tc in range(1,test_case+1):
    N = int(input())

    # 딕셔너리를 이용하여 기록하기 위해 초기 셋팅
    dictionary = {}
    cnt = 1

    # 트리 만들기 (배열 만들기?)
    c1 = [0] * (N+1)
    c2 = [0] * (N+1)
    par = [0] * (N+1)

    # par
    for i in range(N,0,-1):
        if i == 1:
            par[i] = 0
        else:
            par[i] = i//2

    # c1, c2
    for i in range(1,N+1):
        for j in range(N+1):
            if par[j] == i:
                if c1[i] == 0:
                    c1[i] = j
                else:
                    c2[i] = j

    tree_LVR(1)
    # print(dictionary)
    # {1: 4, 2: 2, 3: 5, 4: 1, 5: 6, 6: 3}

    for key, value in dictionary.items():
        if value == 1:
            root = key
        if value == N//2:
            N2node = key

    print(f'#{tc} {root} {N2node}')