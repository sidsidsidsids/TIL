switch_amount = int(input())
switches = list(map(int,input().split()))
students = int(input())
for _ in range(students):
    S, N = map(int,input().split())
    if S == 1:
        for i in range(switch_amount):
            if (i+1) % N == 0:
                if switches[i] == 0:
                    switches[i] = 1
                else:
                    switches[i] = 0
            else:
                pass
    if S == 2:
        if switches[N-1] == 0:
            switches[N-1] = 1
        else:
            switches[N-1] = 0
        for K in range(1,switch_amount):
            if N-1 + K >= switch_amount or N-1 - K < 0:
                break
            else:
                if switches[N-1 + K] == 0 and switches[N-1 - K] == 0:
                    switches[N-1 + K] = switches[N-1 - K] = 1
                elif switches[N-1 + K] == 1 and switches[N-1 - K] == 1:
                    switches[N-1 + K] = switches[N-1 - K] = 0
                else:
                    break
for i in range(switch_amount):
    if (i+1) % 20 == 0:
        print(switches[i])
    else:
        print(switches[i], end=' ')

