test_case = int(input())
for tc in range(1, test_case+1):
    N, M, L = map(int,input().split())

    # 딕셔너리
    dictionary = {}
    for i in range(1,N+1):
        dictionary[i] = []

    # 트리 만들기 (배열 만들기?)
    c1 = [0] * (N + 1)
    c2 = [0] * (N + 1)
    par = [0] * (N + 1)

    # par
    for i in range(N, 0, -1):
        if i == 1:
            par[i] = 0
        else:
            par[i] = i // 2

    # c1, c2
    for i in range(1, N + 1):
        for j in range(N + 1):
            if par[j] == i:
                if c1[i] == 0:
                    c1[i] = j
                else:
                    c2[i] = j

    # 리프 노드 번호 input
    for _ in range(M):
        node_num, node_val = map(int,input().split())
        dictionary[node_num] = node_val

    # 딕셔너리에 번호 채워가기
    for i in range(N,0,-1):
        if not dictionary[i]:
            if i*2 + 1 <= N:
                dictionary[i] = dictionary[i*2] + dictionary[i*2 + 1]
            else:
                dictionary[i] = dictionary[i*2]
        if i == L:
            break

    print(f'#{tc} {dictionary[L]}')
