n, k = map(int,input().split())
homes = [[] for _ in range(n)]
for idx in range(n):
    homes[idx] = [idx] + list(map(int,input().split()))

homes = sorted(homes, key = lambda X:(X[2], X[1]), reverse=False)

answers = [[] for _ in range(n)]
dayCnt = 0
day = homes[0][1]
for idx in range(n):
    notPrint = True
    while notPrint:
        if homes[idx][1] <= day <= homes[idx][2]:
            if dayCnt >= k:
                day += 1
                dayCnt = 0
            else:
                answers[homes[idx][0]] = day
                dayCnt += 1
                notPrint = False
        else:
            day = homes[idx][1]
            answers[homes[idx][0]] = day
            dayCnt = 1
            notPrint = False
for a in answers:
    print(a)