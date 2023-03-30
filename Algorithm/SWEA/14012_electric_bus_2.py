t = int(input())
for tc in range(1,1+t):
    energy = list(map(int,input().split()))

    loc = 1
    goal = energy[0]
    battery = energy[1]
    cnt = 0

    while loc < goal:
        if loc + battery < goal:
            max_value = 0
            loc_idx = 0
            for n_loc in range(loc+1,loc+battery+1):
                value = n_loc + energy[n_loc]
                if max_value <= value:
                    max_value = value
                    next = n_loc
                loc_idx += 1
            loc = next
            battery += energy[next] - loc_idx
            cnt += 1
        else:
            break

    print(f'#{tc} {cnt}')