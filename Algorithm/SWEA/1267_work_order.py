for tc in range(1,11):
    V, E = map(int,input().split())
    arr = list(map(int,input().split()))
    adjL = [ [] for _ in range(V+1) ]

    for i in range(E):
        adjL[arr[2*i+1]].append(arr[2*i])

    find = 0
    result = [0] * V

    while True:
        # 가능한 일 찾기
        able = []
        for i in range(1, V+1):
            if i not in result:
                if not adjL[i]:
                    # for j in range(1,V+1):
                    #     if i in adjL[j]:
                    #         break
                    # else:
                    able.append(i)
                    result[find] = i
                    find += 1
                    # print(result)

        if find == V:
            break

        # 일하고 잠금 풀기
        for work in able:
            for j in range(1,V+1):
                if work in adjL[j]:
                    adjL[j].remove(work)

    print(f'#{tc}', *result)




