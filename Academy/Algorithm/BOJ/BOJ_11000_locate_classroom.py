N = int(input())
schedule = [0] * N
for n in range(N):
    schedule[n] = list(map(int,input().split()))
schedule = sorted(schedule)
