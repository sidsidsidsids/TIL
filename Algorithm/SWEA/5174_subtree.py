def node_count(s):
    for i in range(1,E+1+1):
        # 시작점을 부모로 가지는 노드가 있다면
        if par[i] == s:
            # 카운트 +1
            global cnt
            cnt += 1
            # 그 노드로(자식 노드로) 재귀
            node_count(i)

test_case = int(input())
for tc in range(1,test_case+1):
    E, N = map(int,input().split())
    arr = list(map(int,input().split()))

    #c1 = [0] * (E+1 + 1)
    #c2 = [0] * (E+1 + 1)
    par = [0] * (E+1 + 1)
    #갯수를 셀 변수 선언
    cnt = 0

    # 자식 번호를 인덱스로 부모 번호를 저장
    for i in range(E):
        #c1[i], c2[i] = arr[2*i], arr[2*i + 1]
        par[arr[2*i + 1]] = arr[2*i]

    node_count(N)
    print(f'#{tc} {cnt+1}')

