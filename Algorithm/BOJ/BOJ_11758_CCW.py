p1 = list(map(int,input().split()))
p2 = list(map(int,input().split()))
p3 = list(map(int,input().split()))


if (p2[0] < p3[0] and p2[1] > p3[1] and p1[0] < p2[0] and p1[1] < p2[1] )\
        or (p2[0] > p3[0] and p2[1] > p3[1] and p1[0] < p2[0] and p1[1] > p2[1])\
        or (p2[0] > p3[0] and p2[1] < p3[1] and p1[0] > p2[0] and p1[1] > p2[1])\
        or (p2[0] < p3[0] and p2[1] < p3[1] and p1[0] > p2[0] and p1[1] < p2[1]):
    print(-1)
elif (p2[0] > p3[0] and p2[1] > p3[1] and p1[0] > p2[0] and p1[1] < p2[1])\
        or (p2[0] < p3[0] and p2[1] > p3[1] and p1[0] > p2[0] and p1[1] > p2[1])\
        or (p2[0] < p3[0] and p2[1] < p3[1] and p1[0] < p2[0] and p1[1] > p2[1])\
        or (p2[0] > p3[0] and p2[1] < p3[1] and p1[0] < p2[0] and p1[1] < p2[1]):
    print(1)
else:
    print(0)


