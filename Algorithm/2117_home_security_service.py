def security_range(i,j,k):
    s_r = set()
    for v in range(k):
        for y, x in [[i+v,j], [i-v,j], [i,j+v], [i,j-v]]:
            if 0 <= y < N and 0 <= x < N:
                s_r.add([y,x])
    return s_r

test_case = int(input())
for tc in range(1,test_case+1):
    N, M = map(int,input().split())
    city = [ list(map(int,input().split())) for _ in range(N) ]

    # K_cost = K**2 + (K-1)**2

    for i in range(N):
        for j in range(N):

