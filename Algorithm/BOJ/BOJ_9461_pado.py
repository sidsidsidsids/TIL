t = int(input())
for _ in range(t):

    pado = [0, 1, 1]

    N = int(input())

    if N == 1 or N == 2:
        print(1)
    else:
        pado = pado + [0] * (N-2)

        for i in range(3,N+1):
            pado[i] = pado[i-3] + pado[i-2]

        print(pado[N])