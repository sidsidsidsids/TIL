N = int(input())
s = 1
for j in range(0,1700):
    if s == 0:
        break
    for i in range(0,1001):
        if 5*i + 3*j == N:
            print(i+j)
            s = 0
            break
else:
    print(-1)
