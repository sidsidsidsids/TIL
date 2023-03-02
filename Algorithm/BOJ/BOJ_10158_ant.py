garo, sero = map(int,input().split())
p, q = map(int,input().split())
t = int(input())

# garo_t = t - (garo - p)
# p = garo_t % garo
#
# sero_t = t - (sero - q)
# q = sero_t % sero
if t < 100:
    a = 1; b = 1
    while t > 0:
        p += a; q += b
        if p == garo or p == 0:
            a = -a
        if q == sero or q == 0:
            b = -b
        t -= 1
else:
    if (t // garo) % 2 == 0 and (t / garo) % 2 == 0:
        p = p
    elif t > garo and (t // garo) % 2: # 시간 나누기 가로의 몫이 홀수이면 진행방향 반대로?
        t -= garo * (t//garo)
        a = -1;b = 1
        while t > 0:
            p += a; q += b
            if p == garo or p == 0:
                a = -a
            if q == sero or q == 0:
                b = -b
            t -= 1




print(p, q)