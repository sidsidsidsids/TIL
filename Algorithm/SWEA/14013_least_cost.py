def f(i, k, j_list, v):
    global ans

    if v > ans: # backtracking
        return

    if i == k: # end of function
        if v < ans:
            ans = v
        return
    else:
        for j in range(N):
            if j_list[j]:            # if not visited
                v += cost[i][j]      # value update
                j_list[j] = 0        # visited update
                f(i+1, k, j_list, v) # next step
                v -= cost[i][j]      # reset value
                j_list[j] = 1        # reset visit
t = int(input())
for tc in range(1,1+t):
    N = int(input())
    cost = [ list(map(int,input().split())) for _ in range(N) ]
    bit = [1] * N # visited
    ans = 100 * N # initial max value

    f(0, N, bit, 0)

    print(f'#{tc} {ans}')

