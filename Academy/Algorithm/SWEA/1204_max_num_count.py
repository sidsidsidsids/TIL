test_case = int(input())
for _ in range(test_case):
    tc = int(input())
    scores = list(map(int,input().split()))

    counter = [0] * 1001

    for s in scores:
        counter[s] += 1

    print(f'#{tc} {1000 - counter[::-1].index(max(counter))}')