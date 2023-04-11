t = int(input())
for tc in range(t):
    N, M = map(int,input().split())
    time = [0] + list(map(int,input().split()))
    adjL = [ [] for _ in range(N+1) ]

    for _ in range(M):
        s, e = map(int,input().split())
        adjL[e].append(s)

    win = int(input())

    # 가능 건물 짓기
    result = [0] * N
    find = 0
    total = 0
    s = 0
    save = []

    while True:
        able = []
        for i in range(1,N+1):
            if i not in result:
                if not adjL[i]:
                    if i == win:
                        total += time[i]
                        s = 1
                        break
                    able.append(i)
                    result[find] = i
                    find += 1

        if s == 1:
            break

        if save:
            for elem in save:
                able.append(elem)
            save = []

        built = 100000
        for work_idx in able:
            if built > time[work_idx]:
                built = time[work_idx]
        finish = []
        for work_idx in able:
            time[work_idx] -= built
            if time[work_idx] == 0:
                finish.append(work_idx)
        total += built

        if len(finish) != len(able):
            for f in finish:
                able.remove(f)
            for a in able:
                save.append(a)

        for i in range(1,N+1):
            if adjL[i]:
                for f in finish:
                    if f in adjL[i]:
                        adjL[i].remove(f)
    print(total)



