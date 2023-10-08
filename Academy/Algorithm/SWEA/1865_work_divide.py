def f(i,k,j_s,v):
    global ans
    if v <= ans:
        return
    if i == k:
        if ans < v:
            ans = v

    else:
        for j in range(n):
            if j_s[j]:
                if work[i][j]:
                    j_s[j] = 0
                    nv = v * (work[i][j] / 100)
                    f(i+1,k,j_s,nv)
                    j_s[j] = 1


t = int(input())
for tc in range(1,1+t):
    n = int(input())
    work = [ list(map(int,input().split())) for _ in range(n) ]

    ans = 0
    j_list = [1] * n

    f(0,n,j_list,1)

    ans = round(ans * 100, 6)

    print(f'#{tc} {ans:0.6f}')