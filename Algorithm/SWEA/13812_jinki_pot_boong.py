test_case = int(input())
for tc in range(1,test_case+1):
    N, M, K = map(int,input().split()) # 사람 수, 굽는 시간, 시간당 갯수
    time = list(map(int,input().split()))

    cook = M
    complete = 0
    time_cnt = 0
    s = 1

    if min(time) < M:
        print(f'#{tc} Impossible')
    else:
        while time:
            cook -= 1
            if cook == 0:
                complete += K
                cook = M
            time_cnt += 1

            if time_cnt in time and complete:
                while time.count(time_cnt) and complete:
                    idx = time.index(time_cnt)
                    del time[idx]
                    complete -= 1
                if time.count(time_cnt) and not complete:
                    print(f'#{tc} Impossible')
                    s = 0
                    break
            elif time_cnt in time and not complete:
                print(f'#{tc} Impossible')
                s = 0
                break

        if s == 1:
            print(f'#{tc} Possible')
