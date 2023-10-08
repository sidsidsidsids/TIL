N = int(input())
times = [0] * N

for i in range(N):
    start, end = map(int,input().split())
    times[i] = [start, end]

times.sort(key=lambda X: [X[1],X[0]])

time = times[0][1]
cnt = 1
for i in range(1,N):
    if times[i][0] < time:
        pass
    else:
        time = times[i][1]
        cnt += 1
        if time > times[-1][1]:
            break

print(cnt)