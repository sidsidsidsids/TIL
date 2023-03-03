for tc in range(1,11):
    V, E = map(int,input().split())
    arr = list(map(int,input().split()))
    adjL = [ [] for _ in range(V+1) ]

    for i in range(E):
        adjL[arr[2*i]].append(arr[2*i+1])


