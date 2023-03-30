def f(i,k,j_s):
    global ans

    if i == k:
        total = 0
        for c in choose:
            if total:
                total *= c/100
            else:
                total += c/100
        total *= 100
        if ans < total:
            ans = round(total,6)

    else:
        for j in range(n):
            if j_s[j]:
                if work[i][j]:
                    choose[i] = work[i][j]
                    j_s[j] = 0
                    f(i+1,k,j_s)
                    choose[i] = 0
                    j_s[j] = 1


t = int(input())
for tc in range(1,1+t):
    n = int(input())
    work = [ list(map(int,input().split())) for _ in range(n) ]

    choose = [0] * n
    ans = 0
    j_list = [1] * n

    f(0,n,j_list)

    print(f'#{tc} {ans}')