from sys import stdin
N = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))
answer = 0
cnt = 0

for i in range(N-1):
    cnt += 1

    if numbers[i] > numbers[i+1]:
        k = 0
        while 0 <= i+k+1 < N and numbers[i+k] >= numbers[i+k+1]:
            cnt += 1
            k += 1
        if answer < cnt:
            answer = cnt
        cnt = 0
    elif numbers[i] < numbers[i+1]:
        k = 0
        while 0 <= i+k+1 < N and numbers[i+k] <= numbers[i+k+1]:
            cnt += 1
            k += 1
        if answer < cnt:
            answer = cnt
        cnt = 0
    else:
        if i == N-2 and numbers[i] == numbers[N-1]:
            cnt += 1
        if answer < cnt:
            answer = cnt

if N == 1:
    print(1)
else:
    print(answer)