def tree_LVR(s):
    if s == 0:
        return
    tree_LVR(c1[s])
    print(dictionary[s], end='')
    tree_LVR(c2[s])

for tc in range(1,11):
    # 초기 설정
    dictionary = {}
    V = int(input())
    c1 = [0] * (V+1)
    c2 = [0] * (V+1)
    par = [0] * (V+1)

    for _ in range(V):
        # 입력값 input
        num, val, *c = input().split()
        # key 값 : 번호, value 값 : 문자 를 가지는 딕셔너리 선언
        dictionary[int(num)] = val
        # c input 상황에 따른 조건문
        if len(c) > 1:
            c1[int(num)] = int(c[0])
            par[int(c[0])] = int(num)
            c2[int(num)] = int(c[1])
            par[int(c[1])] = int(num)
        elif len(c) == 1:
            c1[int(num)] = int(c[0])
            par[int(c[0])] = int(num)
        else:
            pass
    # root 찾기
    for i in range(1, V+1):
        if par[i] == 0 and (c1[i] != 0 or c2[i] != 0):
            start = i

    print(f'#{tc}', end=' ')
    tree_LVR(start)
    print()



