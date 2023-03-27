t = int(input())
for _ in range(t):
    x, y = map(int,input().split())
    dist = y - x
    move = 0
    for i in range(2**31-1):
        move += 1+i
        if move >= dist:
            ans = i
            break
    print(i+1)