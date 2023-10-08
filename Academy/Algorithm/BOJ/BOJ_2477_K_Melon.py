'''
반시계 방향으로 도는데
     2(좌로)
3(아래로)   4(위로)
     1(우로)
'''
garo = []; sero = []; order = []
n = int(input())
for _ in range(6):
    l, k = map(int,input().split())
    order.append(l)
    order.append(k)
    if l == 1 or l == 2:
        garo.append(k)
    else:
        sero.append(k)

target = []
for i in range(2,9,2):
    if order[i-1] != max(garo) and order[i-1] != max(sero) and \
            order[i + 3] != max(garo) and order[i + 3] != max(sero):
        target.append(order[i+1])
        cnt = i

if not target:
    target.append(order[1])
    target.append(order[-1])
elif len(target) == 1:
    if cnt == 2:
        target.append(order[1])
    elif cnt == 8:
        target.append(order[-1])


print(n*(max(garo)*max(sero) - target[0]*target[1]))