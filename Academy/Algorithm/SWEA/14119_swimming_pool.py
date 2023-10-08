def swim_plan(i,v):
    global pivot
    if v > pivot:
        return
    if i >= 12:
        if v < pivot:
            pivot = v
    else:
        if plan[i]:
            v += quarter
            swim_plan(i+3,v)
            v -= quarter
            v += month
            swim_plan(i+1,v)
            v -= month
            v += day*plan[i]
            swim_plan(i+1,v)
            v -= day*plan[i]
        else:
            swim_plan(i+1,v)


t = int(input())
for tc in range(1,1+t):
    day, month, quarter, year = map(int,input().split())
    plan = list(map(int,input().split()))

    pivot = 0
    pivot += year

    swim_plan(0,0)

    print(f'#{tc} {pivot}')
